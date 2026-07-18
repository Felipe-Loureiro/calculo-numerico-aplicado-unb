# PPC2 - Método de Bairstow para raízes de polinômios

**Universidade de Brasília - UnB**  
**Faculdade de Tecnologia - FT**  
**Departamento de Engenharia Mecânica - ENM**  
**Disciplina:** ENM0227 - Cálculo Numérico Aplicado  
**Semestre:** 2026/1  
**Aluno:** Felipe Tavares Loureiro  
**Professor:** Prof. Dr. Rafael Gabler Gontijo

## Resumo operacional

Este notebook Jupyter contém a implementação, em Python, do método de Bairstow para determinação numérica de raízes de polinômios de grau arbitrário, incluindo raízes reais e pares complexos conjugados.

O método é implementado do zero, sem bibliotecas simbólicas ou resolvedores prontos. A implementação inclui divisão sintética quadrática, cálculo dos coeficientes auxiliares, atualização iterativa dos parâmetros, deflação do polinômio e tratamento analítico do fator final.

O algoritmo é aplicado tanto a casos de validação quanto ao polinômio característico obtido na APC2. Também são estudadas a sensibilidade aos chutes iniciais e a estrutura de convergência no plano dos parâmetros de Bairstow.

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

## Ambiente utilizado

O notebook foi desenvolvido para rodar em ambiente Jupyter, com foco em uso simples no Google Colab:

1. abra o Google Colab;
2. faça upload do arquivo `.ipynb`;
3. execute as células em ordem, de cima para baixo.

Ele também deve funcionar normalmente em um Jupyter Notebook local.

## Formulação resumida

O método procura fatores quadráticos da forma:

```text
x² - r*x - s
```

Os parâmetros `r` e `s` são corrigidos iterativamente a partir dos restos obtidos pela divisão sintética. Quando o fator quadrático converge, o polinômio é deflacionado e o processo continua até restar um fator de grau um ou dois, resolvido analiticamente.

## Dicionário de variáveis

| Variável | Significado | Unidade | Tipo |
|---|---|---:|---|
| `coeficientes` ou `a` | coeficientes do polinômio em ordem decrescente | não aplicável | `list[float]` |
| `grau` | grau atual do polinômio durante a deflação | não aplicável | `int` |
| `r`, `s` | parâmetros do fator quadrático `x² - r*x - s` | não aplicável | `float` |
| `r0`, `s0` | chutes iniciais para `r` e `s` | não aplicável | `float` |
| `b` | coeficientes da divisão sintética quadrática | não aplicável | `list[float]` |
| `c` | coeficientes auxiliares usados no sistema de correção | não aplicável | `list[float]` |
| `dr`, `ds` | correções iterativas dos parâmetros | não aplicável | `float` |
| `determinante` | determinante do sistema de correção de `r` e `s` | não aplicável | `float` |
| `tolerancia` | critério de parada do método | não aplicável | `float` |
| `max_iter` | número máximo de iterações | não aplicável | `int` |
| `raizes` | raízes reais ou complexas encontradas | não aplicável | `list[complex]` |
| `residuo` | valor de `|P(raiz)|` usado na verificação | não aplicável | `float` |
| `mapa_convergencia` | classificação da varredura de chutes | não aplicável | lista ou matriz |

## Dependências e bibliotecas

Foram usados apenas pacotes básicos:

- Python 3;
- `math`;
- `matplotlib.pyplot`;
- `matplotlib.colors`.

O código foi feito sem SymPy, `numpy.roots` ou outros resolvedores prontos de raízes polinomiais.

## Entradas

Não há arquivos externos obrigatórios. As entradas são definidas no notebook:

- lista de coeficientes do polinômio;
- chutes iniciais `r0` e `s0`;
- tolerância;
- número máximo de iterações;
- limites e resolução da varredura no plano `(r, s)`.

## Organização do notebook

O notebook está dividido em blocos que acompanham a lógica do trabalho.

### 1. Implementação do método de Bairstow

São definidas as rotinas principais do método:

- divisão sintética quadrática;
- cálculo dos coeficientes auxiliares;
- atualização dos parâmetros `r` e `s`;
- critério de parada;
- deflação polinomial;
- tratamento das raízes finais.

### 2. Construção e validação com um polinômio de teste

É montado um polinômio com raízes previamente conhecidas para verificar se o método consegue recuperá-las com boa precisão numérica.

### 3. Estudo de convergência

É analisada a influência dos valores iniciais `r0` e `s0` sobre:

- número de iterações;
- convergência ou divergência;
- sensibilidade do método aos chutes iniciais.

### 4. Aplicação ao polinômio característico da APC2

O método é aplicado ao polinômio característico obtido analiticamente na atividade anterior. As raízes encontradas correspondem aos autovalores do sistema dinâmico estudado.

### 5. Interpretação física dos resultados

As raízes são interpretadas considerando:

- estabilidade;
- amortecimento;
- presença ou ausência de comportamento oscilatório;
- efeito da parte real e da parte imaginária dos autovalores.

### 6. Varredura no plano `(r, s)`

Uma rotina testa vários pares iniciais `(r0, s0)` e registra o comportamento do método em diferentes regiões do plano.

### 7. Fractal de Bairstow

Os dados da varredura são usados para construir o fractal de Bairstow, permitindo visualizar regiões de convergência, divergência e padrões estruturais do método para o polinômio estudado.

## Saídas

A execução produz:

- raízes do polinômio de teste;
- raízes do polinômio característico da APC2;
- número de iterações e indicação de convergência;
- resíduos `|P(raiz)|`;
- mapas e fractais de convergência;
- interpretações físicas dos autovalores.

Os resultados e gráficos são armazenados nas células do notebook.

## Observações sobre a implementação

- o código foi feito sem SymPy;
- a proposta foi usar apenas estruturas básicas de Python;
- as funções foram separadas para deixar claro o papel de cada etapa do algoritmo;
- as células Markdown comentam os resultados numéricos e gráficos obtidos;
- as varreduras gráficas mais refinadas podem demorar mais, especialmente quando o passo escolhido é muito pequeno.

## Procedimento de execução

1. Abra `PPC2_FelipeLoureiro.ipynb`.
2. Reinicie o kernel.
3. Execute todas as células em ordem.
4. Observe as saídas numéricas da validação com raízes conhecidas.
5. Confira as raízes calculadas para o polinômio da APC2.
6. Analise a interpretação dos autovalores.
7. Gere os gráficos e o fractal a partir da rotina de varredura.

```bash
jupyter notebook PPC2_FelipeLoureiro.ipynb
```

## Validação metodológica

A validação usa um polinômio construído a partir de raízes conhecidas. Para cada raiz calculada, devem ser verificados:

- proximidade em relação à raiz de referência;
- pequeno valor do resíduo `|P(raiz)|`;
- reconstrução coerente do polinômio após a deflação;
- aparecimento de pares complexos conjugados quando os coeficientes são reais.

No caso da APC2, as raízes também são interpretadas como autovalores do sistema dinâmico, verificando estabilidade, amortecimento e caráter oscilatório.

## Resultado esperado

Ao final da execução, o notebook deve permitir:

- verificar se o método de Bairstow foi implementado corretamente;
- recuperar as raízes do polinômio de teste;
- resolver o polinômio característico da APC2;
- analisar numericamente a convergência do método;
- identificar a sensibilidade aos chutes iniciais;
- visualizar o fractal de Bairstow associado ao problema estudado.

## Bibliografia específica

CHAPRA, Steven C.; CANALE, Raymond P. **Métodos numéricos para engenharia**. 5. ed. São Paulo: McGraw-Hill, 2008.

GONTIJO, Rafael Gabler. **Roteiro do PPC2 e notas de aula de Cálculo Numérico Aplicado**. Brasília: Universidade de Brasília, 2026.

BURDEN, Richard L.; FAIRES, J. Douglas; BURDEN, Annette M. **Numerical Analysis**. 10. ed. Boston: Cengage Learning, 2016.

## Autor

**Felipe Tavares Loureiro**  
**ENM0227 - Cálculo Numérico Aplicado**  
**Universidade de Brasília - UnB**
