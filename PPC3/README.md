# PPC3 - Condução transiente 1D com diferenças finitas implícitas

**Universidade de Brasília - UnB**  
**Faculdade de Tecnologia - FT**  
**Departamento de Engenharia Mecânica - ENM**  
**Disciplina:** ENM0227 - Cálculo Numérico Aplicado  
**Semestre:** 2026/1  
**Aluno:** Felipe Tavares Loureiro  
**Professor:** Prof. Dr. Rafael Gabler Gontijo

## Resumo operacional

Este notebook Jupyter contém a implementação, em Python, de um modelo numérico para resolver o problema de condução de calor transiente em uma parede plana unidimensional.

O espaço é discretizado por diferenças finitas e o avanço temporal utiliza um esquema implícito. A cada passo de tempo surge um sistema linear tridiagonal, resolvido pelo algoritmo de Thomas implementado diretamente no notebook.

O problema é estudado inicialmente sem geração interna de calor, com validação por comparação com a solução exata fornecida no roteiro. Em seguida é incluído um termo de geração volumétrica uniforme. A etapa final aplica o modelo a valores físicos representativos de uma vareta combustível de reator PWR/AP1000, reconhecendo que a geometria plana constitui uma aproximação simplificada.

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

## Ambiente utilizado

O notebook foi desenvolvido para rodar em ambiente Jupyter, com foco em uso simples no Google Colab:

1. abra o Google Colab;
2. faça upload do arquivo `.ipynb`;
3. execute as células em ordem, de cima para baixo.

Ele também deve funcionar normalmente em um Jupyter Notebook local.

## Formulação resumida

A equação de condução transiente unidimensional, com geração volumétrica uniforme, pode ser escrita como:

```text
rho * cp * ∂T/∂t = k * ∂²T/∂x² + qdot
```

Sem geração interna, utiliza-se `qdot = 0`. O esquema implícito gera, a cada passo temporal, um sistema tridiagonal. A geração uniforme e independente da temperatura altera o vetor do lado direito, mas não exige mudança na estrutura tridiagonal da matriz.

## Dicionário de variáveis

| Variável | Significado | Unidade | Tipo |
|---|---|---:|---|
| `L` | espessura ou comprimento do domínio | m | `float` |
| `nx` | número de nós espaciais | - | `int` |
| `dx` | espaçamento espacial | m | `float` |
| `dt` | passo temporal | s | `float` |
| `tempo_final` | duração da simulação | s | `float` |
| `alpha` | difusividade térmica | m²/s | `float` |
| `k` | condutividade térmica | W/(m·K) | `float` |
| `rho` | massa específica | kg/m³ | `float` |
| `cp` | calor específico | J/(kg·K) | `float` |
| `h_conv` ou `h` | coeficiente de convecção | W/(m²·K) | `float` |
| `T_inicial` | temperatura inicial do domínio | K ou °C | `float` |
| `T_inf` | temperatura do fluido externo | K ou °C | `float` |
| `qdot` | geração volumétrica de calor | W/m³ | `float` |
| `a`, `b`, `c` | diagonais inferior, principal e superior do sistema | - | arrays ou listas |
| `d` | vetor do lado direito | temperatura | array ou lista |
| `T` | campo de temperatura no passo atual | K ou °C | array |
| `Fo` | número de Fourier associado à discretização | adimensional | `float` |
| `Bi` | número de Biot discretizado | adimensional | `float` |
| `tempos` | instantes armazenados para análise | s | array ou lista |
| `historico_temperaturas` | solução ao longo do tempo | K ou °C | array ou lista de arrays |

## Dependências e bibliotecas

Foram usados apenas pacotes básicos de Python:

- Python 3;
- `numpy`;
- `matplotlib.pyplot`.

O NumPy é usado para armazenar e manipular vetores e matrizes. Não são usados solvers prontos de sistemas lineares, como `numpy.linalg.solve`, para resolver o sistema principal. A solução dos sistemas tridiagonais é feita pelo algoritmo de Thomas implementado no próprio notebook.

## Entradas

Os parâmetros são definidos em células do notebook:

- geometria e número de nós;
- propriedades termofísicas;
- temperaturas inicial e ambiente;
- coeficiente convectivo;
- geração interna `qdot`;
- duração e passo temporal.

Não há arquivo externo obrigatório.

## Organização do notebook

O notebook está dividido em quatro partes principais, seguindo os itens pedidos no PPC3.

### 1. Caso sem geração interna e validação

O problema de condução transiente é resolvido com `qdot = 0`. A equação é discretizada no espaço por diferenças finitas e no tempo por um esquema implícito. A cada passo temporal, o sistema tridiagonal é resolvido pelo algoritmo de Thomas.

A solução numérica é comparada com a solução exata em série apresentada no roteiro, e o erro relativo é calculado para avaliar a qualidade da implementação.

### 2. Inclusão da geração interna

É acrescentado o termo de geração interna uniforme. Como a geração é independente da temperatura, ela entra apenas no vetor do lado direito; a matriz tridiagonal permanece com a mesma estrutura.

Também é feito um teste no limite `qdot -> 0`, verificando se a solução com geração retorna ao comportamento do caso sem geração.

### 3. Visualização dos resultados

São geradas diferentes visualizações da solução numérica:

- perfis de temperatura ao longo do domínio;
- comparação entre centro e superfície convectiva;
- mapa espaço-tempo da temperatura;
- análise da evolução temporal da temperatura máxima.

Esses gráficos auxiliam a interpretação do efeito da convecção na superfície e da geração interna no domínio.

### 4. Simulação com valores físicos realistas

O modelo é aplicado usando valores representativos de uma vareta combustível de reator PWR/AP1000.

Os dados de geometria, geração volumétrica, temperatura do refrigerante e coeficiente convectivo são baseados em um estudo sobre pellet combustível AP1000. As propriedades termofísicas do dióxido de urânio são baseadas em dados da IAEA.

Como o modelo implementado é unidimensional plano, os resultados devem ser interpretados como uma aproximação simplificada, não como uma representação completa da geometria cilíndrica real de uma vareta combustível.

## Saídas

A execução produz:

- perfis de temperatura em tempos selecionados;
- evolução da temperatura no centro e na superfície;
- mapas espaço-tempo;
- evolução temporal da temperatura máxima;
- erros em relação à solução exata;
- comparação entre o caso sem geração e o limite `qdot -> 0`;
- simulação final com parâmetros físicos representativos.

Os gráficos e resultados ficam incorporados ao notebook.

## Observações sobre a implementação

- o método de Thomas foi implementado manualmente;
- a matriz do sistema foi armazenada por meio de suas três diagonais principais;
- o código foi organizado em funções para facilitar a reutilização nos casos sem geração e com geração;
- a mesma função principal permite alterar o valor de `qdot` para ativar ou remover a geração interna;
- as células Markdown comentam os resultados numéricos e os gráficos obtidos.

## Procedimento de execução

1. Abra `PPC3_FelipeLoureiro.ipynb`.
2. Reinicie o kernel.
3. Execute todas as células em ordem.
4. Confira a validação do caso sem geração interna.
5. Observe os erros calculados em relação à solução exata.
6. Execute o caso com geração interna.
7. Confira o teste do limite `qdot -> 0`.
8. Gere os gráficos de visualização.
9. Execute a simulação final com valores físicos realistas.

```bash
jupyter notebook PPC3_FelipeLoureiro.ipynb
```

## Validação metodológica

A validação é feita por:

1. comparação do caso sem geração com a solução exata em série fornecida no roteiro;
2. cálculo do erro em pontos equivalentes da malha espacial e temporal;
3. verificação de que a solução com geração converge para a solução sem geração quando `qdot -> 0`;
4. inspeção do comportamento físico: suavidade espacial, continuidade temporal e aproximação do regime permanente.

A solução do caso realista deve ser interpretada como modelo plano simplificado, não como descrição completa da geometria cilíndrica de uma vareta combustível.

## Resultado esperado

Ao final da execução, o notebook deve permitir:

- verificar a implementação do método de diferenças finitas implícito;
- resolver sistemas tridiagonais usando o algoritmo de Thomas;
- validar o caso sem geração interna com base em uma solução exata;
- analisar o efeito da geração interna de calor;
- verificar o limite `qdot -> 0`;
- visualizar a evolução temporal da temperatura no domínio;
- testar o modelo em um cenário com parâmetros físicos representativos.

## Bibliografia específica

CHAPRA, Steven C.; CANALE, Raymond P. **Métodos numéricos para engenharia**. 5. ed. São Paulo: McGraw-Hill, 2008.

INTERNATIONAL ATOMIC ENERGY AGENCY. **Thermophysical Properties of Materials for Nuclear Engineering: A Tutorial and Collection of Data**. Vienna: IAEA, 2008.

TIMOTEO, V. S.; ROSA, R.; CURI, E. **Transient Thermal Diffusion and Temperature Distribution of a Cylindrical Fuel Pellet Shifted Radially in Pressurized Water Reactor**. Referência utilizada no notebook para os parâmetros representativos do caso AP1000.

GONTIJO, Rafael Gabler. **Roteiro do PPC3 e notas de aula de Cálculo Numérico Aplicado**. Brasília: Universidade de Brasília, 2026.

## Autor

**Felipe Tavares Loureiro**  
**ENM0227 - Cálculo Numérico Aplicado**  
**Universidade de Brasília - UnB**

