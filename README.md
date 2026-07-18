# Cálculo Numérico Aplicado - ENM0227

**Universidade de Brasília - UnB**  
**Faculdade de Tecnologia - FT**  
**Departamento de Engenharia Mecânica - ENM**  
**Disciplina:** ENM0227 - Cálculo Numérico Aplicado  
**Semestre:** 2026/1  
**Discente:** Felipe Tavares Loureiro  
**Docente:** Prof. Dr. Rafael Gabler Gontijo

## Apresentação

Este repositório reúne os Programas para Casa (PPCs) desenvolvidos na disciplina de Cálculo Numérico Aplicado. Os trabalhos abordam problemas de equações diferenciais ordinárias e parciais, raízes de polinômios, sistemas lineares e otimização, sempre com ênfase na implementação explícita dos métodos numéricos, na interpretação física ou matemática dos resultados e na validação das soluções obtidas.

A organização adotada separa cada prática em um diretório próprio. Cada diretório contém o código principal, um `README.md` específico e, quando aplicável, arquivos de dados, gráficos e outros artefatos necessários para reproduzir ou verificar os resultados.

O objetivo geral é manter os códigos autoexplicativos, auditáveis e reprodutíveis, evitando o uso de rotinas prontas que substituam a implementação dos algoritmos estudados.

## Topologia do repositório

```text
calculo-numerico-aplicado-unb/
├── README.md
├── PPC1/
│   ├── README.md
│   └── PPC1_FelipeLoureiro.ipynb
├── PPC2/
│   ├── README.md
│   └── PPC2_FelipeLoureiro.ipynb
├── PPC3/
│   ├── README.md
│   └── PPC3_FelipeLoureiro.ipynb
├── PPC4/
│   ├── README.md
│   ├── main.py
│   ├── plot_ppc4.gp
│   ├── run_all.sh
│   └── outputs/
├── PPC5/
│   ├── README.md
│   └── PPC5_FelipeLoureiro.ipynb
└── PPC6/
    ├── README.md
    ├── PPC6_FelipeLoureiro.ipynb
    └── resultados_PPC6.zip
```

A pasta `outputs/` do PPC4 e a pasta `resultados_PPC6` criada durante a execução do PPC6 concentram os artefatos numéricos e gráficos de suas respectivas práticas.

## Conteúdo das práticas

| Diretório | Tema | Métodos principais | Produto principal |
|---|---|---|---|
| `PPC1` | Sedimentação de uma esfera | Runge-Kutta de 4ª ordem | Notebook com comparação analítica, estudo de passo e análise do efeito inercial |
| `PPC2` | Raízes de polinômios | Método de Bairstow | Notebook com validação, aplicação à APC2, estudo de convergência e fractal de Bairstow |
| `PPC3` | Condução transiente unidimensional | Diferenças finitas implícitas e algoritmo de Thomas | Notebook com solução exata de referência, geração interna e aplicação a parâmetros de uma vareta combustível |
| `PPC4` | Otimização bidimensional sem restrições | Aclive Máximo, Fletcher-Reeves e interpolação quadrática | Código Python, logs numéricos e gráfico de trajetórias |
| `PPC5` | Equação de Blasius | Método do Tiro, Secante e RK4 | Notebook, perfis de similaridade e arquivo `blasius_resultados.dat` |
| `PPC6` | Condução bidimensional em uma aleta | Diferenças finitas, eliminação de Gauss e Liebmann com e sem relaxação | Notebook, estudos de malha e relaxação, mapas térmicos e arquivos `.dat` |

## Dependências gerais

Os trabalhos foram escritos em Python. As dependências variam conforme a prática:

| Dependência | PPCs | Finalidade |
|---|---|---|
| Biblioteca padrão (`math`, `os`) | PPC1, PPC2, PPC4, PPC5 e PPC6 | Operações matemáticas, arquivos e criação de diretórios |
| `matplotlib` | PPC1, PPC2, PPC3, PPC5 e PPC6 | Geração de gráficos e visualização dos resultados |
| `numpy` | PPC3 | Armazenamento e manipulação de vetores; o sistema tridiagonal continua sendo resolvido pelo algoritmo de Thomas implementado no notebook |
| Gnuplot | PPC4 | Geração das curvas de nível e do gráfico final das trajetórias |
| Bash | PPC4 | Execução automatizada opcional por meio de `run_all.sh` |

Não são utilizados solucionadores prontos para substituir os métodos numéricos solicitados. Quando uma biblioteca é empregada para armazenamento, manipulação ou visualização, o algoritmo principal permanece implementado explicitamente.

## Execução geral

Cada diretório possui instruções detalhadas em seu próprio `README.md`.

### Notebooks Jupyter

Os PPCs 1, 2, 3, 5 e 6 podem ser executados em um ambiente Jupyter local:

```bash
jupyter notebook
```

Também é possível abrir os arquivos `.ipynb` no Google Colab e executar as células em ordem, do início ao fim.

### PPC4

Para executar o programa principal e gerar o gráfico:

```bash
cd PPC4
python3 main.py
gnuplot plot_ppc4.gp
```

Em sistemas Unix, o script auxiliar pode automatizar o processo:

```bash
cd PPC4
chmod +x run_all.sh
./run_all.sh 10 13
```

## Reprodutibilidade e validação

Cada prática documenta:

- o problema físico ou matemático abordado;
- os parâmetros de entrada;
- as estruturas e variáveis principais;
- os arquivos, valores e gráficos produzidos;
- o procedimento exato de execução;
- a solução analítica, benchmark ou teste-limite utilizado para validação;
- as referências específicas usadas na formulação e na verificação.

Antes da entrega, os notebooks devem ser executados do início ao fim em um kernel limpo, sem depender de variáveis criadas fora da ordem das células. Os arquivos de saída devem ser regenerados a partir dos códigos correspondentes sempre que necessário.

## Bibliografia geral

BURDEN, Richard L.; FAIRES, J. Douglas; BURDEN, Annette M. **Numerical Analysis**. 10. ed. Boston: Cengage Learning, 2016.

CHAPRA, Steven C.; CANALE, Raymond P. **Métodos numéricos para engenharia**. 5. ed. São Paulo: McGraw-Hill, 2008.

PRESS, William H. et al. **Numerical Recipes: The Art of Scientific Computing**. 3. ed. Cambridge: Cambridge University Press, 2007.

PYTHON SOFTWARE FOUNDATION. **Python 3 Documentation**. Disponível em: <https://docs.python.org/3/>. Acesso em: 18 jul. 2026.

HUNTER, John D. Matplotlib: A 2D Graphics Environment. **Computing in Science & Engineering**, v. 9, n. 3, p. 90-95, 2007.

HARRIS, Charles R. et al. Array programming with NumPy. **Nature**, v. 585, p. 357-362, 2020.

GONTIJO, Rafael Gabler. **Notas de aula e roteiros de Cálculo Numérico Aplicado**. Brasília: Universidade de Brasília, 2026.

## Autor

**Felipe Tavares Loureiro**  
Engenharia Mecânica - Universidade de Brasília
