# PPC6 - Condução bidimensional em uma aleta por diferenças finitas

**Universidade de Brasília - UnB**  
**Faculdade de Tecnologia - FT**  
**Departamento de Engenharia Mecânica - ENM**  
**Disciplina:** ENM0227 - Cálculo Numérico Aplicado  
**Semestre:** 2026/1  
**Aluno:** Felipe Tavares Loureiro  
**Professor:** Prof. Dr. Rafael Gabler Gontijo

**Repositório:** <https://github.com/Felipe-Loureiro/calculo-numerico-aplicado-unb>

## Resumo operacional

Este notebook Jupyter contém a implementação, em Python, de um modelo numérico para determinar o campo bidimensional de temperatura em uma aleta retangular de seção transversal constante, em regime permanente.

A equação de Laplace é discretizada por diferenças finitas, com temperatura prescrita na base e condições convectivas de Robin nas superfícies superior, inferior e na extremidade livre. O sistema linear resultante é montado explicitamente e resolvido por três estratégias:

1. eliminação de Gauss com pivoteamento parcial;
2. método de Liebmann sem relaxação, equivalente ao Gauss-Seidel com `omega = 1`;
3. método de Liebmann com relaxação.

Também são estudados a influência do fator de relaxação, o refinamento da malha, a esparsidade do sistema e a comparação da linha central com a solução analítica unidimensional clássica para uma aleta de seção constante e extremidade convectiva.

## Objetivos

Este notebook foi montado para:

1. gerar automaticamente uma malha bidimensional uniforme;
2. discretizar a equação de Laplace por diferenças finitas;
3. aplicar a condição de Dirichlet na base aquecida;
4. aplicar condições convectivas de Robin nas demais superfícies;
5. montar o sistema linear correspondente;
6. resolver o sistema por eliminação de Gauss com pivoteamento parcial;
7. resolver o sistema pelo método de Liebmann sem relaxação;
8. resolver o sistema pelo método de Liebmann com relaxação;
9. comparar os resultados, resíduos e tempos dos três métodos;
10. estudar a influência do fator de relaxação `omega`;
11. estudar o efeito do refinamento da malha;
12. comparar a linha central com a solução analítica unidimensional;
13. gerar mapas de temperatura e contornos isotérmicos;
14. salvar os resultados numéricos em arquivos `.dat`.

## Arquivo principal

- `PPC6_FelipeLoureiro.ipynb`

## Ambiente utilizado

O notebook foi desenvolvido para rodar em ambiente Jupyter, com foco em uso simples no Google Colab:

1. abra o Google Colab;
2. faça upload do arquivo `.ipynb`;
3. execute as células em ordem, de cima para baixo;
4. acesse a pasta `resultados_PPC6` criada durante a execução.

Ele também deve funcionar normalmente em um Jupyter Notebook local, desde que o Matplotlib esteja instalado.

## Modelo físico

No interior da aleta, sem geração interna e com propriedades constantes:

```text
∂²T/∂x² + ∂²T/∂y² = 0
```

Condições de contorno:

- base aquecida: temperatura prescrita `T = T_base`;
- superfícies superior e inferior: convecção com coeficiente `h` e temperatura ambiente `T_inf`;
- extremidade livre: convecção com `h` e `T_inf`.

As condições convectivas são incorporadas às equações discretizadas por meio de nós fictícios eliminados com a própria condição de Robin.

## Dicionário de variáveis

| Variável | Significado | Unidade | Tipo |
|---|---|---:|---|
| `L` | comprimento da aleta | m | `float` |
| `espessura` ou `H` | espessura da aleta | m | `float` |
| `k` | condutividade térmica | W/(m·K) | `float` |
| `h_conv` ou `h` | coeficiente convectivo | W/(m²·K) | `float` |
| `T_base` | temperatura prescrita na base | °C ou K | `float` |
| `T_inf` | temperatura do fluido ambiente | °C ou K | `float` |
| `nx`, `ny` | número de nós nas direções `x` e `y` | - | `int` |
| `dx`, `dy` | espaçamentos da malha | m | `float` |
| `i`, `j` | índices locais do nó na malha | - | `int` |
| `N` | número total de incógnitas | - | `int` |
| `A_esparsa` | coeficientes não nulos do sistema | - | lista de estruturas esparsas |
| `A_densa` | matriz usada na eliminação de Gauss | - | `list[list[float]]` |
| `b` | vetor do lado direito | temperatura ou coeficientes | `list[float]` |
| `T_gauss` | solução pela eliminação de Gauss | °C ou K | `list[float]` |
| `T_liebmann` | solução iterativa sem relaxação | °C ou K | `list[float]` |
| `T_relaxado` | solução iterativa relaxada | °C ou K | `list[float]` |
| `omega` | fator de relaxação | adimensional | `float` |
| `tolerancia` | critério de convergência | temperatura | `float` |
| `max_iter` | máximo de iterações | - | `int` |
| `residuo_maximo` | norma máxima de `A*T - b` | temperatura ou coeficientes | `float` |
| `historico_erro` | maior alteração nodal por iteração | temperatura | `list[float]` |

## Dependências e bibliotecas

Foram usados apenas módulos básicos:

- `math`;
- `os`;
- `matplotlib.pyplot`.

Não foram utilizados NumPy, SciPy, solvers prontos de sistemas lineares ou bibliotecas que realizem diretamente a discretização do problema.

A montagem da matriz, a eliminação de Gauss, os métodos iterativos, o cálculo dos resíduos e a exportação dos dados foram implementados no próprio notebook.

## Parâmetros de entrada

O programa permite definir:

- comprimento da aleta;
- espessura da aleta;
- condutividade térmica;
- coeficiente convectivo;
- temperatura da base;
- temperatura ambiente;
- número de nós em cada direção;
- tolerância de convergência;
- número máximo de iterações;
- fator de relaxação `omega`.

Por padrão, o notebook usa valores previamente definidos para facilitar a reprodução. Para solicitar os valores durante a execução, altere:

```python
usar_entrada_interativa = True
```

## Organização do notebook

O notebook está dividido em blocos que acompanham a lógica do PPC6.

### 1. Modelo físico e parâmetros

São apresentadas a equação de Laplace, as hipóteses do modelo e as condições de contorno. Também são definidos os parâmetros geométricos, térmicos e numéricos e criada a pasta `resultados_PPC6`.

### 2. Discretização e numeração global

A malha cartesiana uniforme é gerada automaticamente e cada nó `(i, j)` recebe um índice global único.

São desenvolvidas equações específicas para:

- nós internos;
- nós da base aquecida;
- nós das superfícies superior e inferior;
- nós da extremidade livre;
- nós de canto.

As condições convectivas são incorporadas por meio de nós fictícios eliminados com a condição de Robin.

### 3. Montagem e solução do sistema

O sistema linear é inicialmente armazenado de forma esparsa, mantendo apenas os coeficientes não nulos de cada linha.

São comparados:

- eliminação de Gauss, usada como solução direta de referência;
- Liebmann sem relaxação, equivalente a Gauss-Seidel com `omega = 1`;
- Liebmann com relaxação, usando o valor definido pelo usuário.

Para os métodos são analisados o tempo computacional, o número de iterações, o erro iterativo, o resíduo máximo e a diferença em relação à solução de Gauss.

### 4. Exportação dos resultados

Os campos de temperatura e as principais métricas são gravados em arquivos `.dat`. A matriz também é exportada em formato esparso, evitando o armazenamento de todos os coeficientes nulos da matriz densa.

### 5. Comparação com a solução analítica

A distribuição numérica ao longo da linha central da aleta é comparada com a solução analítica unidimensional clássica para uma aleta de seção transversal constante e extremidade convectiva.

Também é calculado o erro percentual médio entre as duas soluções. Como a referência analítica é unidimensional, a diferença inclui tanto o erro de discretização quanto as diferenças físicas entre os modelos 2D e 1D.

### 6. Estudo do fator de relaxação

Vários valores de `omega` são testados para avaliar sua influência sobre:

- número de iterações;
- tempo computacional;
- erro final;
- resíduo;
- convergência ou divergência.

O melhor valor testado é identificado com base no menor número de iterações entre os casos convergentes.

### 7. Estudo de refinamento de malha

O problema é resolvido em uma malha grosseira, na malha principal e em uma malha refinada. São comparados o número de nós, os espaçamentos, o custo iterativo, o tempo computacional e o erro em relação à solução unidimensional.

### 8. Visualização do campo

São gerados gráficos de:

- distribuição de temperatura na linha central;
- comparação entre os modelos 2D e 1D;
- efeito de `omega` sobre a convergência;
- efeito do refinamento da malha;
- mapa bidimensional de temperatura;
- contornos isotérmicos.

A simetria do campo em relação à linha central horizontal também é usada como verificação qualitativa da implementação.

### 9. Conclusões

A parte final discute a concordância entre os métodos, a esparsidade da matriz, o efeito da relaxação, o custo do refinamento e as diferenças entre os modelos bidimensional e unidimensional.

## Arquivos de saída

A execução cria a pasta `resultados_PPC6`, contendo:

| Arquivo | Conteúdo |
|---|---|
| `campo_gauss.dat` | campo obtido por eliminação de Gauss |
| `campo_liebmann.dat` | campo obtido por Liebmann sem relaxação |
| `campo_relaxado.dat` | campo obtido por Liebmann com relaxação |
| `sistema_linear_esparso.dat` | coeficientes não nulos da matriz |
| `comparacao_metodos.dat` | comparação entre os três métodos |
| `historico_convergencia.dat` | histórico dos erros iterativos |
| `linha_central_comparacao.dat` | comparação entre as soluções 2D e 1D |
| `estudo_relaxacao.dat` | resultados da varredura de `omega` |
| `estudo_malha.dat` | resultados do refinamento |
| `resumo_resultados.dat` | síntese dos parâmetros e resultados principais |

Os arquivos de campo possuem as colunas:

```text
x  y  T
```

Linhas em branco separam as fileiras da malha.

O repositório também contém `resultados_PPC6.zip`, que preserva os artefatos gerados em uma execução de referência.

São produzidos ainda:

- perfis de temperatura;
- comparação 2D x 1D;
- histórico de convergência;
- estudo do fator de relaxação;
- estudo de refinamento;
- mapa bidimensional e contornos isotérmicos.

## Observações sobre a implementação

- a matriz foi montada manualmente a partir das equações discretizadas;
- os coeficientes não nulos são armazenados em uma estrutura esparsa baseada em listas;
- a matriz densa é criada apenas para a eliminação de Gauss;
- a eliminação de Gauss utiliza pivoteamento parcial;
- o método de Liebmann atualiza os valores segundo a lógica de Gauss-Seidel;
- a relaxação é aplicada durante a atualização de cada nó;
- a maior mudança nodal é usada como critério de convergência;
- o resíduo de `A*T - b` é calculado como verificação adicional;
- as condições convectivas são aplicadas por eliminação de nós fictícios;
- as células Markdown apresentam as equações e discutem os resultados obtidos.

## Procedimento de execução

1. Abra `PPC6_FelipeLoureiro.ipynb` no Jupyter ou Google Colab.
2. Reinicie o kernel.
3. Mantenha `usar_entrada_interativa = False` para usar os parâmetros padrão.
4. Execute todas as células em ordem.
5. Confira a comparação entre os três métodos.
6. Observe os resíduos e os históricos de convergência.
7. Analise a comparação com a solução analítica.
8. Execute os estudos de relaxação e refinamento.
9. Observe os mapas e contornos de temperatura.
10. Consulte os arquivos gerados na pasta `resultados_PPC6`.

```bash
jupyter notebook PPC6_FelipeLoureiro.ipynb
```

> A eliminação de Gauss utiliza uma matriz densa e pode se tornar lenta para malhas muito grandes. Para o estudo de refinamento, o método iterativo relaxado aproveita melhor a estrutura esparsa do sistema.

## Validação metodológica

A implementação é verificada por:

1. concordância entre Gauss, Liebmann e Liebmann relaxado dentro da tolerância;
2. cálculo do resíduo máximo de `A*T - b`;
3. simetria do campo em relação à linha central horizontal;
4. temperatura máxima na base e queda em direção à extremidade livre;
5. comparação da linha central 2D com a solução analítica 1D de aleta com extremidade convectiva;
6. estudo de refinamento de malha;
7. estudo de convergência e estabilidade para diferentes valores de `omega`.

A diferença entre os modelos 2D e 1D não representa apenas erro numérico: também inclui a diferença física entre as formulações.

## Resultado esperado

Ao final da execução, o notebook deve permitir:

- obter o campo bidimensional de temperatura da aleta;
- verificar a concordância entre os três métodos;
- analisar a convergência dos métodos iterativos;
- identificar a influência do fator de relaxação;
- avaliar o custo do refinamento da malha;
- comparar o modelo bidimensional com a solução unidimensional;
- visualizar a queda de temperatura da base até a extremidade livre;
- exportar os resultados para análise posterior.

## Bibliografia específica

INCROPERA, Frank P. et al. **Fundamentos de transferência de calor e de massa**. 7. ed. Rio de Janeiro: LTC, 2014.

PATANKAR, Suhas V. **Numerical Heat Transfer and Fluid Flow**. Boca Raton: CRC Press, 1980.

CHAPRA, Steven C.; CANALE, Raymond P. **Métodos numéricos para engenharia**. 5. ed. São Paulo: McGraw-Hill, 2008.

GONTIJO, Rafael Gabler. **Roteiro do PPC6 e notas de aula de Cálculo Numérico Aplicado**. Brasília: Universidade de Brasília, 2026.

PYTHON SOFTWARE FOUNDATION. **Python 3 Documentation**. Disponível em: <https://docs.python.org/3/>. Acesso em: 18 jul. 2026.

## Autor

**Felipe Tavares Loureiro**  
**ENM0227 - Cálculo Numérico Aplicado**  
**Universidade de Brasília - UnB**
