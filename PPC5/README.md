# PPC5 - Equação de Blasius com Método do Tiro e RK4

**Universidade de Brasília - UnB**  
**Faculdade de Tecnologia - FT**  
**Departamento de Engenharia Mecânica - ENM**  
**Disciplina:** ENM0227 - Cálculo Numérico Aplicado  
**Semestre:** 2026/1  
**Aluno:** Felipe Tavares Loureiro  
**Professor:** Prof. Dr. Rafael Gabler Gontijo

## Resumo operacional

Este notebook Jupyter contém a implementação, em Python, do Método do Tiro combinado com o método de Runge-Kutta de 4ª ordem para a solução numérica da equação de Blasius.

O problema de valor de contorno de terceira ordem é transformado em um sistema de três equações diferenciais de primeira ordem. O valor desconhecido `s = f''(0)` é ajustado pelo Método do Tiro, usando atualização por secante, e cada problema de valor inicial é integrado por RK4.

A solução é usada para analisar os perfis de similaridade, verificar que `f'(eta)` tende a 1, determinar `eta99`, calcular o coeficiente local de atrito e comparar os resultados com valores clássicos da literatura para a camada limite laminar sobre placa plana.

## Objetivos

O trabalho tem como objetivo:

1. implementar o Método do Tiro para a solução de um problema de valor de contorno;
2. implementar o método de Runge-Kutta de 4ª ordem para integrar o sistema de EDOs;
3. determinar numericamente o valor convergido de `f''(0)`;
4. verificar numericamente que `f'(eta)` tende a 1 para valores suficientemente grandes de `eta`;
5. gerar um arquivo `.dat` contendo os valores de `eta`, `f`, `f'` e `f''`;
6. plotar os perfis de similaridade `f(eta)`, `f'(eta)` e `f''(eta)`;
7. calcular o coeficiente local de atrito na parede `Cf`;
8. determinar numericamente `eta99` e o coeficiente `Cdelta`;
9. comparar o valor obtido de `f''(0)` com o valor clássico aproximado `0,332057`;
10. comparar o valor obtido de `Cdelta` com a correlação clássica da camada limite laminar.

## Arquivo principal

- `PPC5_FelipeLoureiro.ipynb`

## Arquivo de saída principal

- `blasius_resultados.dat`

O arquivo contém quatro colunas:

```text
eta  f  fp  fpp
```

## Ambiente utilizado

O notebook foi desenvolvido e testado no Google Colab:

1. acesse o Google Colab;
2. faça upload do arquivo `.ipynb`;
3. execute as células em ordem, de cima para baixo.

O notebook também deve funcionar normalmente em um ambiente Jupyter local.

## Formulação matemática

A equação de Blasius é:

```text
f''' + (1/2) * f * f'' = 0
```

com as condições de contorno:

```text
f(0) = 0
f'(0) = 0
f'(infinito) = 1
```

Como não é possível integrar numericamente até o infinito, utiliza-se um valor finito suficientemente grande `eta_max`, impondo:

```text
f'(eta_max) ≈ 1
```

Definindo:

```text
y1 = f
y2 = f'
y3 = f''
```

obtém-se o sistema:

```text
y1' = y2
y2' = y3
y3' = -(1/2) * y1 * y3
```

No Método do Tiro, o parâmetro desconhecido é:

```text
s = f''(0)
```

As condições iniciais do PVI são:

```text
y1(0) = 0
y2(0) = 0
y3(0) = s
```

O valor de `s` é ajustado até que o resíduo da condição final satisfaça a tolerância escolhida.

## Dicionário de variáveis

| Variável | Significado | Unidade | Tipo |
|---|---|---:|---|
| `eta` | variável de similaridade | adimensional | `float` ou `list[float]` |
| `f` | função de corrente de similaridade | adimensional | `float` ou `list[float]` |
| `fp` | primeira derivada `f'`, perfil de velocidade adimensional | adimensional | `float` ou `list[float]` |
| `fpp` | segunda derivada `f''` | adimensional | `float` ou `list[float]` |
| `s` | parâmetro de tiro `f''(0)` | adimensional | `float` |
| `s0`, `s1` | aproximações consecutivas usadas pela secante | adimensional | `float` |
| `h` | passo de integração em `eta` | adimensional | `float` |
| `eta_max` ou `etamax` | truncamento numérico do infinito | adimensional | `float` |
| `tol` | tolerância da condição `f'(eta_max) = 1` | adimensional | `float` |
| `maxit` | máximo de iterações do ajuste do tiro | - | `int` |
| `erro_tiro` | resíduo `f'(eta_max) - 1` | adimensional | `float` |
| `Rex` | número de Reynolds local | adimensional | `float` |
| `eta99` | valor de `eta` em que `f' = 0,99` | adimensional | `float` |
| `Cdelta` | constante usada na correlação da espessura da camada limite | adimensional | `float` |
| `Cf` ou `Cf_x` | coeficiente local de atrito na parede | adimensional | `float` |
| `lista_eta`, `lista_f`, `lista_fp`, `lista_fpp` | histórico da solução integrada | adimensional | `list[float]` |

## Dependências e bibliotecas

Foram utilizados apenas pacotes básicos:

- Python 3;
- `math.sqrt`;
- `matplotlib.pyplot`.

O RK4, o Método do Tiro, a atualização por Secante e a interpolação necessária para determinar `eta99` são implementados diretamente. Não são usadas bibliotecas prontas de integração numérica.

## Entradas

Os parâmetros numéricos são definidos no notebook:

- chute inicial para `s`;
- passo `h`;
- limite `eta_max`;
- tolerância;
- número máximo de iterações;
- número de Reynolds local usado no cálculo do atrito.

Não há arquivo de entrada externo.

## Organização do notebook

O notebook está organizado em blocos que correspondem diretamente aos itens pedidos no PPC:

1. apresentação do problema e formulação matemática;
2. transformação da equação de Blasius em um sistema de três EDOs de primeira ordem;
3. definição das funções auxiliares e do método numérico;
4. implementação do Método do Tiro com atualização por secante;
5. integração do sistema pelo método de Runge-Kutta de 4ª ordem;
6. entrada dos parâmetros numéricos da simulação;
7. apresentação dos resultados principais;
8. salvamento dos resultados em arquivo `.dat`;
9. geração dos gráficos dos perfis de similaridade;
10. cálculo de `Cf`, `eta99` e `Cdelta`;
11. comparação com valores clássicos da literatura;
12. discussão das principais fontes de erro numérico.

## Saídas

A execução produz:

- valor convergido de `s = f''(0)`;
- erro final da condição de contorno;
- perfis `f`, `f'` e `f''`;
- valor numérico de `eta99`;
- valor de `Cdelta`;
- coeficiente local de atrito `Cf`;
- gráficos dos perfis de similaridade;
- arquivo `blasius_resultados.dat`.

Formato do arquivo:

```text
eta  f  fp  fpp
```

## Parâmetros recomendados para teste

Uma execução inicial pode ser feita com:

```text
s = 0.3
h = 0.01
eta_max = 8
tolerância = 1e-10
número máximo de iterações = 30
Rex = 100000
```

Com esses valores, espera-se obter aproximadamente:

```text
f''(0) ≈ 0.332057
eta99 ≈ 4.91
Cdelta ≈ 4.92
```

## Procedimento de execução

1. Abra `PPC5_FelipeLoureiro.ipynb`.
2. Reinicie o kernel.
3. Execute todas as células em ordem.
4. Verifique a convergência do parâmetro de tiro.
5. Analise os perfis de similaridade.
6. Confira os valores de `Cf`, `eta99` e `Cdelta`.
7. Confirme a criação de `blasius_resultados.dat` no diretório de execução.

```bash
jupyter notebook PPC5_FelipeLoureiro.ipynb
```

## Validação metodológica

A validação deve verificar:

- `f''(0)` próximo do valor clássico de Blasius, aproximadamente `0,332057`;
- `f'(eta_max)` próximo de `1` dentro da tolerância adotada;
- `eta99` próximo de `4,91`;
- `Cdelta` próximo de `4,92`;
- redução do erro com o refinamento de `h` e escolha adequada de `eta_max`;
- resíduo pequeno na condição de contorno final.

As diferenças devem ser discutidas considerando as principais fontes de erro numérico:

- erro de discretização associado ao passo `h`;
- erro associado à substituição de infinito por `eta_max`;
- tolerância adotada no Método do Tiro;
- erro de interpolação na determinação de `eta99`.

## Observações sobre a implementação

A condição de contorno original da equação de Blasius é imposta em `eta` tendendo ao infinito. Como isso não é possível numericamente, o programa utiliza um valor finito `eta_max` suficientemente grande para aproximar essa condição.

O código foi escrito sem o uso de bibliotecas prontas para integração numérica, de modo que o RK4 e o Método do Tiro são implementados diretamente.

## Resultado esperado

Ao final da execução, o notebook deve permitir:

- determinar numericamente `f''(0)`;
- verificar a aproximação de `f'(eta)` para 1;
- visualizar os perfis de similaridade;
- calcular `Cf`, `eta99` e `Cdelta`;
- reproduzir o arquivo `.dat`;
- comparar os resultados com os valores clássicos da literatura;
- identificar as principais fontes de erro numérico.

## Bibliografia específica

BLASIUS, H. Grenzschichten in Flüssigkeiten mit kleiner Reibung. **Zeitschrift für Mathematik und Physik**, v. 56, p. 1-37, 1908.

SCHLICHTING, Hermann; GERSTEN, Klaus. **Boundary-Layer Theory**. 9. ed. Berlin: Springer, 2017.

WHITE, Frank M. **Viscous Fluid Flow**. 3. ed. New York: McGraw-Hill, 2006.

CHAPRA, Steven C.; CANALE, Raymond P. **Métodos numéricos para engenharia**. 5. ed. São Paulo: McGraw-Hill, 2008.

GONTIJO, Rafael Gabler. **Roteiro do PPC5 e notas de aula de Cálculo Numérico Aplicado**. Brasília: Universidade de Brasília, 2026.

## Autor

**Felipe Tavares Loureiro**  
**ENM0227 - Cálculo Numérico Aplicado**  
**Universidade de Brasília - UnB**
