# PPC1 - Sedimentação de uma esfera com RK4

Este notebook Jupyter contém a implementação, em Python, do método de Runge-Kutta de 4ª ordem para a solução numérica do problema de sedimentação de uma esfera em forma adimensional, conforme proposto no PPC1 da disciplina de Cálculo Numérico Aplicado do Departamento de Engenharia Mecânica da Universidade de Brasília, no primeiro semestre de 2026, ministrada pelo professor Rafael Gabler Gontijo.

O notebook foi desenvolvido para resolver o problema de valor inicial associado à equação diferencial do sistema, comparar resultados numéricos com soluções analíticas e discutir a influência dos parâmetros pedidos no enunciado.

Objetivos

O trabalho tem como objetivo:

- implementar o método de Runge-Kutta de 4ª ordem;
- comparar a solução numérica com a solução analítica no caso assintótico Re_s -> 0;
- analisar a influência do passo temporal h;
- resolver o caso com pequeno efeito inercial;
- validar os resultados numéricos com base na solução analítica apresentada no roteiro;
- discutir o efeito de Re_s e o desvio em relação ao caso assintótico.

Arquivo principal

- PPC1_FelipeLoureiro.ipynb

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
  - exp
  - sqrt
- matplotlib.pyplot

Organização do notebook

O notebook está organizado em blocos que correspondem diretamente aos itens pedidos no PPC, incluindo:

- definição das funções e do método numérico;
- comparação para diferentes valores de St;
- estudo da influência do passo h;
- validação no caso com pequeno efeito inercial;
- discussão dos resultados em células Markdown.
