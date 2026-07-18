# PPC1 - Sedimentação de uma esfera com Runge-Kutta de 4ª ordem

**Universidade de Brasília - UnB**  
**Faculdade de Tecnologia - FT**  
**Departamento de Engenharia Mecânica - ENM**  
**Disciplina:** ENM0227 - Cálculo Numérico Aplicado  
**Semestre:** 2026/1  
**Aluno:** Felipe Tavares Loureiro  
**Professor:** Prof. Dr. Rafael Gabler Gontijo

## Resumo operacional

Este notebook Jupyter contém a implementação, em Python, do método de Runge-Kutta de 4ª ordem para a solução numérica do problema de sedimentação de uma esfera em forma adimensional, conforme proposto no PPC1 da disciplina de Cálculo Numérico Aplicado.

O notebook resolve o problema de valor inicial associado à equação diferencial do sistema, compara os resultados numéricos com soluções analíticas e discute a influência dos parâmetros pedidos no enunciado. O estudo avalia particularmente o número de Stokes, o passo temporal e o pequeno efeito inercial associado ao número de Reynolds da partícula.

## Objetivos

O trabalho tem como objetivo:

1. implementar diretamente o método de Runge-Kutta de 4ª ordem;
2. comparar a solução numérica com a solução analítica no caso assintótico `Re_s -> 0`;
3. analisar a influência do passo temporal `h`;
4. resolver o caso com pequeno efeito inercial;
5. validar os resultados numéricos com base na solução analítica apresentada no roteiro;
6. discutir o efeito de `Re_s` e o desvio em relação ao caso assintótico.

## Arquivo principal

- `PPC1_FelipeLoureiro.ipynb`

## Ambiente utilizado

O notebook foi desenvolvido e testado no Google Colab. A forma mais simples de executá-lo é:

1. acessar o Google Colab;
2. fazer upload do arquivo `.ipynb`;
3. executar as células em ordem, de cima para baixo.

O notebook também deve funcionar normalmente em um ambiente Jupyter local com o Matplotlib instalado.

## Formulação matemática

A equação adimensional utilizada é:

```text
St * dv/dt = 1 - v - (3/8) * Re_s * v²
```

ou, na forma utilizada pela função que fornece a derivada:

```text
dv/dt = (1/St) * [1 - v - (3/8) * Re_s * v²]
```

No limite assintótico `Re_s -> 0`, o termo quadrático desaparece e, para a condição inicial `v(0) = 0`, a solução analítica de referência é:

```text
v(t) = 1 - exp(-t/St)
```

Essa solução é usada para verificar a implementação do RK4 no regime em que o efeito inercial deixa de ser relevante.

## Dicionário de variáveis

| Variável | Significado | Unidade | Tipo |
|---|---|---:|---|
| `t` | tempo adimensional atual | adimensional | `float` |
| `y` ou `v` | velocidade adimensional da esfera | adimensional | `float` |
| `St` | número de Stokes | adimensional | `float` |
| `Re_s` | número de Reynolds da partícula | adimensional | `float` |
| `h` | passo temporal de integração | adimensional | `float` |
| `t_final` | limite final da integração | adimensional | `float` |
| `h_atual` | passo efetivamente usado, ajustado no último intervalo | adimensional | `float` |
| `k1`, `k2`, `k3`, `k4` | incrementos intermediários do RK4 | adimensional | `float` |
| `lista_tempo` | instantes calculados | adimensional | `list[float]` |
| `lista_velocidade` | velocidades calculadas | adimensional | `list[float]` |
| `erro` | diferença entre a solução numérica e a solução de referência | adimensional | `float` ou `list[float]` |

## Dependências e bibliotecas

Foram utilizados apenas pacotes básicos:

- Python 3;
- `math.exp`;
- `math.sqrt`;
- `matplotlib.pyplot`.

O RK4 é implementado no próprio notebook. Não é utilizado integrador pronto de equações diferenciais.

## Entradas

O notebook não exige arquivos externos. Os parâmetros são definidos nas células de configuração:

- valores do número de Stokes `St`;
- valores do número de Reynolds `Re_s`;
- passo temporal `h`;
- tempo final;
- condição inicial.

## Organização do notebook

O notebook está organizado em blocos que correspondem diretamente aos itens pedidos no PPC:

1. apresentação do problema e interpretação do limite assintótico `Re_s -> 0`;
2. definição da equação diferencial e das funções auxiliares;
3. implementação do método de Runge-Kutta de 4ª ordem;
4. comparação para diferentes valores de `St`;
5. comparação entre a solução numérica e a solução analítica;
6. estudo da influência do passo `h`;
7. resolução e análise do caso com pequeno efeito inercial;
8. discussão dos resultados em células Markdown.

## Saídas

A execução produz:

- valores numéricos impressos no notebook;
- curvas de velocidade adimensional em função do tempo;
- comparações entre solução numérica e solução analítica;
- gráficos do efeito do número de Stokes;
- gráficos do efeito do passo temporal;
- comparação entre o caso assintótico e o caso com pequeno efeito inercial;
- medidas de erro usadas na validação.

Os resultados são incorporados ao próprio arquivo `.ipynb`; não há arquivo externo obrigatório.

## Procedimento de execução

1. Abra `PPC1_FelipeLoureiro.ipynb` no Jupyter ou no Google Colab.
2. Reinicie o kernel ou o ambiente de execução.
3. Execute todas as células em ordem, de cima para baixo.
4. Verifique as comparações para diferentes valores de `St`.
5. Confira a concordância com a solução analítica no caso `Re_s = 0`.
6. Execute o estudo de passo e o caso com pequeno efeito inercial.

Em um ambiente Jupyter local:

```bash
jupyter notebook PPC1_FelipeLoureiro.ipynb
```

## Validação metodológica

A implementação é validada por três verificações principais:

1. comparação com `v(t) = 1 - exp(-t/St)` quando `Re_s = 0`;
2. redução do erro quando o passo `h` é refinado;
3. verificação de que o caso com pequeno `Re_s` se aproxima do caso assintótico à medida que `Re_s -> 0`.

A concordância deve ser avaliada por erro absoluto ou relativo nos mesmos instantes da malha temporal. O comportamento físico esperado também deve ser preservado: a velocidade parte da condição inicial, cresce de forma suave e tende ao valor terminal adimensional.

## Resultado esperado

Ao final da execução, o notebook deve permitir:

- verificar o funcionamento da implementação de RK4;
- reproduzir a solução analítica no limite `Re_s -> 0`;
- identificar a influência de `St` sobre o tempo de resposta da partícula;
- observar a redução do erro com o refinamento de `h`;
- quantificar o desvio introduzido pelo pequeno termo inercial.

## Bibliografia específica

CHAPRA, Steven C.; CANALE, Raymond P. **Métodos numéricos para engenharia**. 5. ed. São Paulo: McGraw-Hill, 2008.

GONTIJO, Rafael Gabler. **Roteiro do PPC1 e notas de aula de Cálculo Numérico Aplicado**. Brasília: Universidade de Brasília, 2026.

PYTHON SOFTWARE FOUNDATION. **Python 3 Documentation**. Disponível em: <https://docs.python.org/3/>. Acesso em: 18 jul. 2026.

## Autor

**Felipe Tavares Loureiro**  
**ENM0227 - Cálculo Numérico Aplicado**  
**Universidade de Brasília - UnB**
