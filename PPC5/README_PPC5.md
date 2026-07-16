# PPC5 - Equação de Blasius com Método do Tiro e RK4

Este notebook Jupyter contém a implementação, em Python, do Método do Tiro combinado com o método de Runge-Kutta de 4ª ordem para a solução numérica da equação de Blasius, conforme proposto no PPC5 da disciplina de Cálculo Numérico Aplicado do Departamento de Engenharia Mecânica da Universidade de Brasília, no primeiro semestre de 2026, ministrada pelo professor Rafael Gabler Gontijo.

O notebook foi desenvolvido para resolver o problema de valor de contorno associado à equação de Blasius, transformando-o em um problema de valor inicial por meio do ajuste numérico do parâmetro de tiro s = f''(0). A solução obtida é usada para analisar os perfis de similaridade, calcular grandezas físicas associadas à camada limite laminar e comparar os resultados numéricos com valores clássicos da literatura.

Objetivos

O trabalho tem como objetivo:

- implementar o Método do Tiro para a solução de um problema de valor de contorno;
- implementar o método de Runge-Kutta de 4ª ordem para integrar o sistema de EDOs;
- determinar numericamente o valor convergido de f''(0);
- verificar numericamente que f'(eta) tende a 1 para valores suficientemente grandes de eta;
- gerar um arquivo .dat contendo os valores de eta, f, f' e f'';
- plotar os perfis de similaridade f(eta), f'(eta) e f''(eta);
- calcular o coeficiente local de atrito na parede Cf;
- determinar numericamente eta99 e o coeficiente Cdelta;
- comparar o valor obtido de f''(0) com o valor clássico aproximado 0.332057;
- comparar o valor obtido de Cdelta com a correlação clássica da camada limite laminar.

Arquivo principal

- PPC5-FelipeLoureiro.ipynb

Arquivo de saída

- blasius_resultados.dat

O arquivo .dat contém quatro colunas:

- eta
- f
- fp
- fpp

Ambiente utilizado

O notebook foi desenvolvido e testado no Google Colab.

Por isso, a forma mais simples de abrir e executar o arquivo é:

1. acessar o Google Colab;
2. fazer upload do arquivo .ipynb;
3. executar as células em ordem, de cima para baixo.

O notebook também deve funcionar normalmente em um ambiente Jupyter padrão.

Pacotes utilizados

Foram utilizados apenas pacotes básicos da linguagem:

- math
  - sqrt
- matplotlib.pyplot

Organização do notebook

O notebook está organizado em blocos que correspondem diretamente aos itens pedidos no PPC, incluindo:

- apresentação do problema e formulação matemática;
- transformação da equação de Blasius em um sistema de três EDOs de primeira ordem;
- definição das funções auxiliares e do método numérico;
- implementação do Método do Tiro com atualização por secante;
- integração do sistema pelo método de Runge-Kutta de 4ª ordem;
- entrada dos parâmetros numéricos da simulação;
- apresentação dos resultados principais;
- salvamento dos resultados em arquivo .dat;
- geração dos gráficos dos perfis de similaridade;
- cálculo de Cf, eta99 e Cdelta;
- comparação com valores clássicos da literatura;
- discussão das principais fontes de erro numérico.

Parâmetros recomendados para teste

Uma execução inicial pode ser feita com os seguintes valores:

- chute inicial s = 0.3
- passo h = 0.01
- eta_max = 8
- tolerância = 1e-10
- número máximo de iterações = 30
- Rex = 100000

Com esses valores, espera-se obter um resultado próximo de:

- f''(0) ≈ 0.332057
- eta99 ≈ 4.91
- Cdelta ≈ 4.92

Observações

A condição de contorno original da equação de Blasius é imposta em eta tendendo ao infinito. Como isso não é possível numericamente, o programa utiliza um valor finito eta_max suficientemente grande para aproximar essa condição.

As principais fontes de erro numérico discutidas no notebook são:

- erro de discretização associado ao passo h;
- erro associado à substituição de infinito por eta_max;
- tolerância adotada no Método do Tiro;
- erro de interpolação na determinação de eta99.

O código foi escrito sem o uso de bibliotecas prontas para integração numérica, de modo que o RK4 e o Método do Tiro são implementados diretamente.
