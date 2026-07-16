# PPC3: Condução transiente 1D com diferenças finitas implícitas

Este notebook Jupyter contém a implementação, em Python, de um modelo numérico para resolver o problema de condução de calor transiente em uma parede plana unidimensional.

O trabalho foi desenvolvido para o PPC3 da disciplina ENM0227 - Cálculo Numérico Aplicado, do Departamento de Engenharia Mecânica da Universidade de Brasília, no semestre 2026.1.

A ideia principal foi implementar o método das diferenças finitas com esquema implícito no tempo, resolvendo os sistemas lineares tridiagonais com o algoritmo de Thomas. O problema foi estudado primeiro sem geração interna de calor, com validação por comparação com a solução exata, e depois com a inclusão de um termo de geração interna.

## Objetivos

Este notebook foi montado para:

1. resolver numericamente o problema de condução transiente 1D sem geração interna;
2. implementar um esquema implícito de diferenças finitas;
3. resolver os sistemas tridiagonais pelo algoritmo de Thomas;
4. validar a solução numérica com base na solução exata fornecida no roteiro;
5. acrescentar o termo de geração interna de calor;
6. verificar a consistência da solução com geração no limite em que a geração tende a zero;
7. testar diferentes formas de visualização dos resultados;
8. aplicar o modelo a valores físicos representativos de uma vareta combustível de reator PWR/AP1000.

## Arquivo principal

- `PPC3_FelipeLoureiro.ipynb`

> Se o notebook estiver com outro nome, basta substituir esse nome pelo arquivo final antes de subir o projeto para o GitHub.

## Ambiente utilizado

O notebook foi desenvolvido para rodar em ambiente Jupyter, com foco em uso simples no Google Colab.

A forma mais prática de executar é:

1. abrir o Google Colab;
2. fazer upload do arquivo `.ipynb`;
3. executar as células em ordem, de cima para baixo.

Ele também deve funcionar normalmente em um Jupyter Notebook local.

## Pacotes utilizados

Foram usados apenas pacotes básicos de Python:

- `numpy`
- `matplotlib.pyplot`

Não foram usados solvers prontos de sistemas lineares, como `numpy.linalg.solve`, para resolver o sistema principal. A solução dos sistemas tridiagonais foi feita pelo algoritmo de Thomas implementado no próprio notebook.

## Organização do notebook

O notebook está dividido em quatro partes principais, seguindo os itens pedidos no PPC3.

### 1. Caso sem geração interna e validação

Nesta parte, o problema de condução transiente é resolvido sem geração interna de calor.

A equação do calor é discretizada no espaço por diferenças finitas e no tempo por um esquema implícito. A cada passo temporal, surge um sistema linear tridiagonal, resolvido pelo algoritmo de Thomas.

A solução numérica é comparada com a solução exata em série apresentada no roteiro, e o erro relativo é calculado para avaliar a qualidade da implementação.

### 2. Inclusão da geração interna

Depois da validação do caso sem geração, é acrescentado o termo de geração interna de calor.

Como a geração é considerada uniforme e independente da temperatura, ela entra apenas no vetor do lado direito do sistema linear. A matriz tridiagonal permanece a mesma.

Também é feito um teste no limite em que a geração interna tende a zero, verificando se a solução com geração retorna ao comportamento do caso sem geração.

### 3. Visualização dos resultados

Nesta etapa são geradas diferentes visualizações da solução numérica, incluindo:

- perfis de temperatura ao longo do domínio;
- comparação entre centro e superfície convectiva;
- mapa espaço-tempo da temperatura;
- análise da evolução temporal da temperatura máxima.

Esses gráficos ajudam a interpretar o comportamento físico do problema, principalmente o efeito da convecção na superfície e da geração interna no domínio.

### 4. Simulação com valores físicos realistas

Por fim, o modelo é aplicado usando valores representativos de uma vareta combustível de reator PWR/AP1000.

Foram usados dados de geometria, geração volumétrica, temperatura do refrigerante e coeficiente convectivo retirados de um estudo sobre pellet combustível AP1000. As propriedades termofísicas do dióxido de urânio foram baseadas em dados da IAEA.

Como o modelo implementado é unidimensional plano, os resultados devem ser interpretados como uma aproximação simplificada, não como uma representação completa da geometria real de uma vareta combustível.

## Observações sobre a implementação

- o método de Thomas foi implementado manualmente;
- a matriz do sistema foi armazenada por meio de suas três diagonais principais;
- o código foi organizado em funções para facilitar a reutilização no caso sem geração e com geração;
- a mesma função principal permite alterar o valor de `qdot` para ativar ou remover a geração interna;
- as células Markdown comentam os resultados numéricos e os gráficos obtidos.

## Como reproduzir os resultados

Para reproduzir o trabalho:

1. abra o notebook;
2. execute todas as células em ordem;
3. confira a validação do caso sem geração interna;
4. observe os erros calculados em relação à solução exata;
5. execute o caso com geração interna;
6. confira o teste do limite `qdot -> 0`;
7. gere os gráficos de visualização;
8. execute a simulação final com valores físicos realistas.

## Resultado esperado

Ao final da execução, o notebook deve permitir:

- verificar a implementação do método de diferenças finitas implícito;
- resolver sistemas tridiagonais usando o algoritmo de Thomas;
- validar o caso sem geração interna com base em uma solução exata;
- analisar o efeito da geração interna de calor;
- visualizar a evolução temporal da temperatura no domínio;
- testar o modelo em um cenário com parâmetros físicos representativos.

## Fontes utilizadas

As principais fontes usadas para os valores físicos realistas foram:

- IAEA, *Thermophysical Properties of Materials for Nuclear Engineering*;
- Timoteo, Rosa e Curi, *Transient Thermal Diffusion and Temperature Distribution of a Cylindrical Fuel Pellet Shifted Radially in Pressurized Water Reactor*.

## Autor

Felipe Tavares Loureiro  
ENM0227 - Cálculo Numérico Aplicado  
Universidade de Brasília - UnB
