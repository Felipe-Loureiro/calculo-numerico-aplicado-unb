# PPC4 - Otimização bidimensional sem restrições

Universidade de Brasília - UnB  
Faculdade de Tecnologia - FT  
Departamento de Engenharia Mecânica - ENM  
Disciplina: ENM0227 - Cálculo Numérico Aplicado  
Semestre: 2026/1  
Aluno: Felipe Tavares Loureiro  
Professor: Prof. Dr. Rafael Gabler Gontijo  

## 1. Resumo operacional

Este diretório contém a implementação do Programa para Casa 04, cujo objetivo é resolver numericamente um problema de maximização bidimensional sem restrições.

A função objetivo estudada é:

```text
f(x, y) = 2xy + 2x - x² - 2y²
```

O ótimo analítico informado no enunciado é:

```text
(x*, y*) = (2, 1)
```

com:

```text
f* = 2
```

Foram implementados dois métodos de otimização:

1. Aclive Máximo;
2. Gradientes Conjugados na variante Fletcher-Reeves.

Ambos os métodos utilizam a mesma estratégia de busca linear unidimensional baseada em interpolação quadrática de três pontos.

Caso a parábola interpoladora fique degenerada, o programa utiliza como alternativa o melhor passo entre os três valores testados.

O programa solicita ao usuário o ponto inicial `(x0, y0)`, executa os dois métodos em sequência, salva os logs numéricos em arquivos separados e gera os arquivos necessários para a construção de um gráfico com curvas de nível e trajetórias.

## 2. Objetivos

O PPC4 tem como objetivos:

1. implementar numericamente o método do Aclive Máximo;
2. implementar numericamente o método dos Gradientes Conjugados de Fletcher-Reeves;
3. implementar uma busca linear unidimensional por interpolação quadrática de três pontos;
4. comparar a convergência dos dois métodos;
5. comparar as trajetórias percorridas no plano `(x, y)`;
6. validar os resultados com o ótimo analítico conhecido;
7. registrar o histórico iterativo em arquivos `.dat`;
8. gerar uma representação gráfica com curvas de nível e trajetórias;
9. manter o código compatível com Python 3.5.2 ou superior;
10. evitar o uso de bibliotecas prontas de otimização ou solucionadores numéricos.

## 3. Estrutura do diretório

A estrutura esperada para este diretório é:

```text
PPC4/
├── main.py
├── plot_ppc4.gp
├── run_all.sh
├── README.md
└── outputs/
    ├── output1.dat
    ├── output2.dat
    ├── function.dat
    ├── traj_aclive.dat
    ├── traj_fr.dat
    ├── contours.dat
    └── trajetorias.png
```

## 4. Descrição dos arquivos

### `main.py`

Script principal do PPC4.

Ele implementa:

- a função objetivo;
- o cálculo do gradiente;
- a norma do gradiente;
- a busca linear por interpolação quadrática;
- o tratamento do caso de interpolação degenerada;
- o método do Aclive Máximo;
- o método dos Gradientes Conjugados de Fletcher-Reeves;
- a criação automática da pasta `outputs`;
- a gravação dos logs numéricos;
- a gravação dos pontos das trajetórias;
- a geração das amostras da função objetivo usadas pelo Gnuplot;
- a apresentação dos resultados finais no terminal.

### `plot_ppc4.gp`

Script do Gnuplot responsável por gerar o gráfico final com:

- curvas de nível da função objetivo;
- trajetória do método do Aclive Máximo;
- trajetória do método de Fletcher-Reeves;
- indicação do ponto ótimo analítico;
- legenda e identificação dos eixos.

O script utiliza os arquivos gerados previamente por `main.py`.

### `run_all.sh`

Script auxiliar em Bash criado para facilitar a execução completa do trabalho.

Ele pode:

- executar `main.py`;
- chamar o Gnuplot;
- gerar a imagem final;
- abrir a imagem produzida, quando o ambiente possuir um visualizador compatível.

O uso de `run_all.sh` é opcional.

O funcionamento essencial do trabalho depende de:

```text
main.py
plot_ppc4.gp
```

### `outputs/`

Diretório onde são armazenados:

- logs dos métodos;
- valores amostrados da função;
- trajetórias;
- curvas de nível auxiliares;
- imagem final.

A pasta é criada automaticamente pelo programa principal caso ainda não exista.

## 5. Formulação matemática

### 5.1 Função objetivo

A função a ser maximizada é:

```text
f(x, y) = 2xy + 2x - x² - 2y²
```

O ótimo analítico conhecido é:

```text
x* = 2
y* = 1
f* = 2
```

### 5.2 Gradiente

As derivadas parciais são:

```text
df/dx = 2y + 2 - 2x
```

e:

```text
df/dy = 2x - 4y
```

Portanto, o gradiente é:

```text
grad f(x, y) = [2y + 2 - 2x, 2x - 4y]
```

A norma euclidiana do gradiente é utilizada como medida do erro iterativo:

```text
erro = sqrt((df/dx)² + (df/dy)²)
```

A convergência é declarada quando:

```text
erro <= tolerancia
```

ou quando o número máximo de iterações é atingido.

### 5.3 Método do Aclive Máximo

Como o problema é de maximização, a direção de busca do Aclive Máximo é o próprio gradiente:

```text
p = grad f
```

A atualização do ponto é feita por:

```text
x(k+1) = x(k) + h(k) * px(k)
y(k+1) = y(k) + h(k) * py(k)
```

em que:

- `h(k)` é o passo calculado pela busca linear;
- `px(k)` é a componente da direção na coordenada `x`;
- `py(k)` é a componente da direção na coordenada `y`.

Como a direção é recalculada exclusivamente a partir do gradiente local, o método pode apresentar trajetória em zigue-zague em funções alongadas ou mal condicionadas.

### 5.4 Gradientes Conjugados de Fletcher-Reeves

No método de Fletcher-Reeves, a direção inicial é:

```text
p(0) = grad f(0)
```

Nas iterações seguintes, a direção é atualizada por:

```text
p(k+1) = grad f(k+1) + beta(k) * p(k)
```

com:

```text
beta(k) = ||grad f(k+1)||² / ||grad f(k)||²
```

Essa atualização combina:

- o gradiente atual;
- a direção usada na iteração anterior.

Para funções quadráticas, essa característica pode produzir uma trajetória mais direta e reduzir significativamente o número de iterações.

### 5.5 Busca linear

A busca linear é feita ao longo da direção `p`.

Define-se a função unidimensional:

```text
g(h) = f(x + h*px, y + h*py)
```

O valor de `h` é estimado por interpolação quadrática usando inicialmente três pontos:

```text
h0 = 0
h1 = 1
h2 = 2
```

Os valores correspondentes são:

```text
g0 = g(h0)
g1 = g(h1)
g2 = g(h2)
```

A partir desses três pares, é construída uma parábola interpoladora.

O vértice dessa parábola fornece uma estimativa para o passo que maximiza `g(h)` ao longo da direção escolhida.

Caso a interpolação fique degenerada, por exemplo quando o denominador da expressão do vértice fica nulo ou numericamente muito pequeno, o programa utiliza como alternativa o melhor passo entre os três valores avaliados.

Essa estratégia evita a introdução de constantes arbitrárias apenas para forçar a convergência.

## 6. Dicionário de variáveis

### `x`

Coordenada `x` do ponto atual.

Tipo:

```text
float
```

Unidade:

```text
não aplicável
```

### `y`

Coordenada `y` do ponto atual.

Tipo:

```text
float
```

Unidade:

```text
não aplicável
```

### `x0`

Coordenada `x` inicial fornecida pelo usuário.

Tipo:

```text
float
```

Unidade:

```text
não aplicável
```

### `y0`

Coordenada `y` inicial fornecida pelo usuário.

Tipo:

```text
float
```

Unidade:

```text
não aplicável
```

### `dfx`

Valor da derivada parcial:

```text
df/dx
```

avaliada no ponto atual.

Tipo:

```text
float
```

### `dfy`

Valor da derivada parcial:

```text
df/dy
```

avaliada no ponto atual.

Tipo:

```text
float
```

### `gradiente`

Vetor gradiente da função objetivo no ponto atual.

Formato conceitual:

```text
[dfx, dfy]
```

Tipo:

```text
lista de floats
```

### `gradiente_anterior`

Gradiente calculado na iteração anterior.

É usado no cálculo do parâmetro `beta` do método de Fletcher-Reeves.

Tipo:

```text
lista de floats
```

### `direcao`

Direção de busca utilizada na iteração atual.

No Aclive Máximo:

```text
direcao = gradiente
```

No método de Fletcher-Reeves:

```text
direcao = gradiente_atual + beta * direcao_anterior
```

Tipo:

```text
lista de floats
```

### `direcao_anterior`

Direção de busca utilizada na iteração anterior do método de Fletcher-Reeves.

Tipo:

```text
lista de floats
```

### `px`

Componente da direção de busca associada à coordenada `x`.

Tipo:

```text
float
```

### `py`

Componente da direção de busca associada à coordenada `y`.

Tipo:

```text
float
```

### `h`

Passo calculado pela busca linear por interpolação quadrática.

Tipo:

```text
float
```

### `h0`, `h1` e `h2`

Três valores de passo usados para avaliar a função unidimensional `g(h)` e construir a interpolação quadrática.

Valores iniciais:

```text
h0 = 0
h1 = 1
h2 = 2
```

Tipo:

```text
float
```

### `g0`, `g1` e `g2`

Valores da função unidimensional `g(h)` nos passos `h0`, `h1` e `h2`.

Tipo:

```text
float
```

### `erro`

Norma euclidiana do gradiente.

É usada como critério de convergência.

Tipo:

```text
float
```

### `tolerancia`

Valor máximo aceitável para a norma do gradiente antes de encerrar o método.

Valor padrão:

```text
1.0e-6
```

Tipo:

```text
float
```

### `max_iter`

Número máximo de iterações permitido.

Valor padrão:

```text
100
```

Tipo:

```text
int
```

### `iteracao`

Contador da iteração atual.

Tipo:

```text
int
```

### `beta`

Parâmetro de Fletcher-Reeves usado para atualizar a direção conjugada.

É calculado por:

```text
beta = ||gradiente_atual||² / ||gradiente_anterior||²
```

Tipo:

```text
float
```

### `trajetoria`

Lista contendo os pontos percorridos por um método.

Formato conceitual:

```text
[[x0, y0], [x1, y1], ..., [xfinal, yfinal]]
```

É usada para gerar os arquivos de trajetória.

Tipo:

```text
lista de pares de floats
```

### `amostras`

Lista com os pares:

```text
[h, g(h)]
```

usados na interpolação quadrática e no tratamento alternativo do caso degenerado.

Tipo:

```text
lista de listas
```

### `limites`

Lista contendo os limites usados para gerar a malha da função objetivo:

```text
[xmin, xmax, ymin, ymax]
```

Tipo:

```text
lista de floats
```

### `xmin` e `xmax`

Limites inferior e superior da coordenada `x` usados na amostragem da função para o gráfico.

Tipo:

```text
float
```

### `ymin` e `ymax`

Limites inferior e superior da coordenada `y` usados na amostragem da função para o gráfico.

Tipo:

```text
float
```

### `nx` e `ny`

Número de pontos de amostragem usados em cada direção para construir `function.dat`.

Tipo:

```text
int
```

## 7. Dependências e bibliotecas

### 7.1 Programa principal

O programa principal foi implementado em Python.

Dependências de `main.py`:

```text
Python 3.5.2 ou superior
os
```

O módulo `os` pertence à biblioteca padrão do Python.

Ele é usado apenas para criar a pasta `outputs`, caso ela ainda não exista.

Não foram utilizadas:

- bibliotecas prontas de otimização;
- funções prontas de busca linear;
- solucionadores numéricos;
- NumPy;
- SciPy;
- bibliotecas que resolvam diretamente o problema proposto.

### 7.2 Geração do gráfico

Para gerar o gráfico, é necessário ter o Gnuplot instalado:

```text
gnuplot
```

O Gnuplot utiliza os arquivos `.dat` gerados por `main.py`.

### 7.3 Script auxiliar

O arquivo `run_all.sh` utiliza Bash.

Ele é opcional e serve apenas para facilitar a execução do programa e a geração do gráfico.

## 8. Entradas

O programa solicita inicialmente:

### `x0`

Coordenada inicial no eixo `x`.

Tipo esperado:

```text
número real
```

### `y0`

Coordenada inicial no eixo `y`.

Tipo esperado:

```text
número real
```

Depois disso, o programa pergunta se o usuário deseja utilizar os parâmetros padrão:

```text
tolerancia = 1.0e-6
max_iter = 100
```

Caso o usuário responda `n`, é possível fornecer manualmente:

- a tolerância;
- o número máximo de iterações.

Os mesmos valores de entrada são usados pelos dois métodos para permitir uma comparação direta.

## 9. Saídas

O programa gera os seguintes arquivos.

### `outputs/output1.dat`

Log numérico do método do Aclive Máximo.

Formato:

```text
iter erro h x y dfx dfy
```

As colunas representam:

- `iter`: número da iteração;
- `erro`: norma do gradiente;
- `h`: passo calculado pela busca linear;
- `x`: coordenada `x` do ponto;
- `y`: coordenada `y` do ponto;
- `dfx`: derivada parcial `df/dx`;
- `dfy`: derivada parcial `df/dy`.

### `outputs/output2.dat`

Log numérico do método dos Gradientes Conjugados Fletcher-Reeves.

Formato:

```text
iter erro h x y dfx dfy
```

As colunas possuem o mesmo significado de `output1.dat`.

### `outputs/function.dat`

Amostras da função objetivo.

Formato:

```text
x y f(x,y)
```

Esse arquivo é usado pelo Gnuplot para gerar as curvas de nível.

### `outputs/traj_aclive.dat`

Pontos da trajetória do método do Aclive Máximo.

Formato:

```text
x y
```

Cada linha representa um ponto visitado pelo método.

### `outputs/traj_fr.dat`

Pontos da trajetória do método de Fletcher-Reeves.

Formato:

```text
x y
```

Cada linha representa um ponto visitado pelo método.

### `outputs/contours.dat`

Arquivo auxiliar gerado pelo Gnuplot com os dados das curvas de nível.

Ele é criado durante a execução de `plot_ppc4.gp`.

### `outputs/trajetorias.png`

Imagem final contendo:

- curvas de nível da função;
- trajetória do Aclive Máximo;
- trajetória de Fletcher-Reeves;
- ponto ótimo analítico;
- legenda;
- identificação dos eixos.

Os arquivos de saída podem ser sobrescritos a cada nova execução.

## 10. Procedimento de execução

### 10.1 Execução manual do programa

Entre no diretório do PPC4:

```bash
cd PPC4
```

Execute o programa principal:

```bash
python3 main.py
```

Informe:

1. `x0`;
2. `y0`;
3. se deseja usar os parâmetros padrão;
4. a tolerância, caso escolha parâmetros personalizados;
5. o número máximo de iterações, caso escolha parâmetros personalizados.

Ao final da execução, os arquivos numéricos serão gravados na pasta:

```text
outputs/
```

### 10.2 Geração manual do gráfico

Depois de executar `main.py`, rode:

```bash
gnuplot plot_ppc4.gp
```

O gráfico será salvo em:

```text
outputs/trajetorias.png
```

O programa Python deve ser executado pelo menos uma vez antes do Gnuplot, pois o gráfico depende dos arquivos gerados por `main.py`.

### 10.3 Execução com o script auxiliar

Para executar de forma interativa:

```bash
./run_all.sh
```

Para executar diretamente com o ponto inicial `(10, 13)`:

```bash
./run_all.sh 10 13
```

Caso o arquivo ainda não possua permissão de execução:

```bash
chmod +x run_all.sh
```

O script é apenas uma ferramenta de conveniência.

A execução principal continua sendo formada por:

```bash
python3 main.py
gnuplot plot_ppc4.gp
```

## 11. Validação metodológica

### 11.1 Solução analítica

A solução analítica do problema é:

```text
x* = 2
y* = 1
f* = 2
```

Essa solução fornece uma referência direta para avaliar os resultados numéricos.

### 11.2 Caso de teste

Para validar a implementação, foi realizado um teste com o ponto inicial:

```text
x0 = 10
y0 = 13
```

Esse ponto inicial foi escolhido porque evidencia melhor a diferença entre as trajetórias dos dois métodos.

O Aclive Máximo apresenta comportamento em zigue-zague, enquanto o método de Fletcher-Reeves segue uma trajetória mais direta até o ponto ótimo.

### 11.3 Resultado do Aclive Máximo

Resultados obtidos:

```text
x final = 2.000000367740
y final = 1.000000204169
f final ≈ 2.000000000000
erro final ≈ 3.37e-7
iterações realizadas = 29
```

O resultado numérico fica muito próximo do ótimo analítico:

```text
(2, 1)
```

A pequena diferença observada está de acordo com a tolerância numérica adotada.

O método converge corretamente, mas utiliza mais iterações e apresenta uma trajetória em zigue-zague.

Isso ocorre porque a direção de busca é recalculada sempre como o gradiente local, podendo gerar mudanças bruscas de direção em funções alongadas ou mal condicionadas.

### 11.4 Resultado de Fletcher-Reeves

Resultados obtidos:

```text
x final = 2.000000000000
y final = 1.000000000000
f final = 2.000000000000
erro final = 0.0
iterações realizadas = 2
```

O método convergiu exatamente para o ótimo analítico dentro da precisão apresentada.

Nesse caso quadrático, a atualização da direção de busca incorpora informação da direção anterior por meio do parâmetro `beta`.

Isso produz uma trajetória mais direta e reduz o número de iterações.

### 11.5 Comparação dos métodos

Para o caso testado:

- os dois métodos convergem para o ótimo analítico;
- o Aclive Máximo realiza 29 iterações;
- Fletcher-Reeves realiza 2 iterações;
- o Aclive Máximo apresenta trajetória em zigue-zague;
- Fletcher-Reeves apresenta trajetória mais direta;
- os valores finais da função concordam com `f* = 2`.

A diferença de desempenho observada não implica que Fletcher-Reeves será superior em qualquer problema.

Ela mostra que, para esta função quadrática específica e para o ponto inicial usado, a direção conjugada aproveita melhor a estrutura do problema.

### 11.6 Verificação gráfica

A imagem:

```text
outputs/trajetorias.png
```

permite verificar qualitativamente:

- a forma das curvas de nível;
- a posição do ótimo;
- o caminho percorrido pelo Aclive Máximo;
- o caminho percorrido por Fletcher-Reeves;
- a diferença entre as duas trajetórias.

![Trajetórias dos métodos](outputs/trajetorias.png)

## 12. Observações sobre a implementação

- a função objetivo foi implementada diretamente;
- o gradiente foi implementado analiticamente;
- a norma euclidiana do gradiente é usada como critério de convergência;
- a busca linear foi implementada sem funções prontas;
- a interpolação quadrática utiliza três pontos;
- existe tratamento para o caso de interpolação degenerada;
- o Aclive Máximo utiliza diretamente a direção do gradiente;
- Fletcher-Reeves combina o gradiente atual com a direção anterior;
- os dois métodos usam as mesmas condições iniciais;
- os logs são salvos separadamente;
- as trajetórias são salvas separadamente;
- a malha da função é exportada para o Gnuplot;
- não há uso de aleatoriedade;
- não há uso de fatores arbitrários para forçar a convergência;
- não há uso de bibliotecas prontas de otimização.

## 13. Observações sobre reprodutibilidade

Os arquivos de saída são sobrescritos a cada nova execução.

A pasta `outputs` é criada automaticamente pelo programa principal caso não exista.

O gráfico final depende dos arquivos gerados por `main.py`.

Portanto, antes de executar o Gnuplot, é necessário rodar o programa Python pelo menos uma vez.

O script `run_all.sh` é apenas uma ferramenta de conveniência.

O funcionamento principal do projeto depende de:

```text
main.py
plot_ppc4.gp
```

O código não usa aleatoriedade.

Assim, para um mesmo:

- ponto inicial;
- valor de tolerância;
- número máximo de iterações;

os resultados devem ser reprodutíveis.

## 14. Resultado esperado

Ao final da execução, deve ser possível:

1. executar os dois métodos a partir do mesmo ponto inicial;
2. verificar a convergência para `(2, 1)`;
3. confirmar numericamente que `f(x*, y*) = 2`;
4. comparar os erros finais;
5. comparar o número de iterações;
6. observar o zigue-zague do Aclive Máximo;
7. observar a trajetória mais direta de Fletcher-Reeves;
8. consultar os históricos iterativos;
9. reproduzir os arquivos de trajetória;
10. gerar as curvas de nível;
11. produzir a imagem final;
12. repetir a simulação com outros pontos iniciais e parâmetros.

## 15. Limitações

A análise apresentada corresponde ao problema bidimensional específico definido no enunciado.

Os resultados de convergência dependem de fatores como:

- função objetivo;
- ponto inicial;
- tolerância;
- número máximo de iterações;
- comportamento da busca linear.

O fato de Fletcher-Reeves convergir em duas iterações neste caso está relacionado à estrutura quadrática da função.

Esse resultado não deve ser interpretado como garantia de desempenho idêntico para funções gerais não lineares.

## 16. Bibliografia específica

CHAPRA, Steven C.; CANALE, Raymond P. Métodos numéricos para engenharia. 5. ed. São Paulo: McGraw-Hill, 2008.

GONTIJO, Rafael Gabler. Notas de aula do curso de Cálculo Numérico Aplicado. Brasília: Universidade de Brasília, 2026.

PYTHON SOFTWARE FOUNDATION. Python 3 Documentation. Disponível em: <https://docs.python.org/3/>. Acesso em: 18 jul. 2026.

GNUPLOT. Gnuplot Documentation. Disponível em: <http://www.gnuplot.info/documentation.html>. Acesso em: 18 jul. 2026.
