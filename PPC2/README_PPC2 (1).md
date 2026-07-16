# PPC2: Método de Bairstow para raízes de polinômios

Este notebook Jupyter contém a implementação, em Python, do método de Bairstow para determinação numérica de raízes de polinômios de grau arbitrário, incluindo raízes reais e complexas conjugadas.

O trabalho foi desenvolvido para o **PPC2** da disciplina **ENM0227 - Cálculo Numérico Aplicado**, do **Departamento de Engenharia Mecânica da Universidade de Brasília**, no semestre **2026.1**.

A ideia aqui foi implementar o método do zero, sem usar bibliotecas simbólicas, e aplicar essa implementação tanto em casos de validação quanto no polinômio característico obtido na **APC2**.

## Objetivos

Este notebook foi montado para:

1. implementar o método de Bairstow para encontrar raízes de polinômios de grau arbitrário;
2. validar a implementação com um polinômio de raízes conhecidas;
3. analisar como os chutes iniciais `r0` e `s0` afetam a convergência do método;
4. aplicar o método ao polinômio característico obtido na APC2;
5. interpretar as raízes encontradas do ponto de vista físico;
6. fazer uma varredura no plano `(r, s)` para estudar o comportamento de convergência;
7. construir o fractal de Bairstow associado ao polinômio analisado.

## Arquivo principal

- `PPC2_FelipeLoureiro.ipynb`

> Se você ainda não renomeou o arquivo, pode trocar esse nome pelo nome final do notebook antes de subir pro GitHub.

## Ambiente utilizado

O notebook foi desenvolvido para rodar em ambiente Jupyter, com foco em uso simples no **Google Colab**.

A forma mais prática de executar é:

1. abrir o Google Colab;
2. fazer upload do arquivo `.ipynb`;
3. executar as células em ordem, de cima para baixo.

Ele também deve funcionar normalmente em um Jupyter Notebook local.

## Pacotes utilizados

Foram usados apenas pacotes básicos:

- `math`
- `matplotlib.pyplot`
- `matplotlib.colors`

## Organização do notebook

O notebook está dividido em blocos que acompanham a lógica do trabalho:

### 1. Implementação do método de Bairstow
Nesta parte são definidas as rotinas principais do método, incluindo:

- divisão sintética quadrática;
- cálculo dos coeficientes auxiliares;
- atualização dos parâmetros `r` e `s`;
- critério de parada;
- deflação polinomial;
- tratamento das raízes finais.

### 2. Construção e validação com um polinômio de teste
Aqui é montado um polinômio com raízes previamente conhecidas para verificar se o método consegue recuperar essas raízes com boa precisão numérica.

### 3. Estudo de convergência
Nesta etapa é analisada a influência dos valores iniciais `r0` e `s0` sobre:

- número de iterações;
- convergência ou divergência;
- sensibilidade do método aos chutes iniciais.

### 4. Aplicação ao polinômio característico da APC2
Depois da validação, o método é aplicado ao polinômio característico obtido analiticamente na atividade anterior.

As raízes encontradas correspondem aos autovalores do sistema dinâmico estudado.

### 5. Interpretação física dos resultados
Com base nas raízes obtidas, é feita uma leitura física do sistema, discutindo pontos como:

- estabilidade;
- amortecimento;
- presença ou ausência de comportamento oscilatório;
- efeito da parte real e da parte imaginária dos autovalores.

### 6. Varredura no plano `(r, s)`
É implementada uma rotina que testa vários pares iniciais `(r0, s0)` para registrar o comportamento do método em diferentes regiões do plano.

### 7. Fractal de Bairstow
Por fim, os dados da varredura são usados para construir o fractal de Bairstow, permitindo visualizar regiões de convergência, divergência e padrões estruturais do método para o polinômio em estudo.

## Observações sobre a implementação

- o código foi feito **sem SymPy**;
- a proposta foi usar apenas estruturas básicas de Python;
- as funções foram separadas para deixar mais claro o papel de cada etapa do algoritmo;
- ao longo do notebook, as células Markdown comentam os resultados numéricos e gráficos obtidos.

## Como reproduzir os resultados

Para reproduzir o trabalho:

1. abra o notebook;
2. execute todas as células em ordem;
3. observe as saídas numéricas da validação;
4. confira as raízes calculadas para o polinômio da APC2;
5. gere os gráficos e o fractal a partir da rotina de varredura.

> Observação: as varreduras gráficas mais refinadas podem demorar mais para rodar, especialmente quando o passo escolhido é muito pequeno.

## Resultado esperado

Ao final da execução, o notebook deve permitir:

- verificar se o método de Bairstow foi implementado corretamente;
- recuperar raízes de polinômios de teste;
- resolver o polinômio característico da APC2;
- analisar numericamente a convergência do método;
- visualizar o fractal de Bairstow associado ao problema estudado.

## Autor

**Felipe Tavares Loureiro**  
**ENM0227 - Cálculo Numérico Aplicado**  
**Universidade de Brasília - UnB**
