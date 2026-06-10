#!/bin/bash

# Script rapido para testar o PPC4:
# 1. executa main.py
# 2. gera o grafico com Gnuplot
# 3. abre a imagem final

if [ $# -ge 2 ]; then
    X0=$1
    Y0=$2

    echo "Rodando PPC4 com ponto inicial x0=$X0, y0=$Y0"
    echo ""

    printf "%s\n%s\ns\n" "$X0" "$Y0" | python3 main.py
else
    echo "Rodando PPC4 em modo interativo."
    echo ""
    python3 main.py
fi

if [ $? -ne 0 ]; then
    echo ""
    echo "Erro ao executar main.py"
    exit 1
fi

echo ""
echo "Gerando grafico com Gnuplot..."
gnuplot plot_ppc4.gp

if [ $? -ne 0 ]; then
    echo ""
    echo "Erro ao executar plot_ppc4.gp"
    exit 1
fi

echo ""
echo "Grafico gerado em outputs/trajetorias.png"

if command -v xdg-open > /dev/null; then
    xdg-open outputs/trajetorias.png > /dev/null 2>&1 &
fi
