# PPC4 - Grafico de curvas de nivel e trajetorias
# Execute com:
#     gnuplot plot_ppc4.gp

# Gera arquivo auxiliar com as curvas de nivel
set contour base
set cntrparam levels 30
unset surface
set view map

set table 'outputs/contours.dat'
splot 'outputs/function.dat' using 1:2:3 with lines
unset table

# Grafico final
reset

set terminal pngcairo size 1200,850 enhanced font 'Arial,12'
set output 'outputs/trajetorias.png'

set title 'PPC4 - Curvas de nível e trajetórias'
set xlabel 'x'
set ylabel 'y'

set grid lc rgb '#DDDDDD'
set key outside right top
set size ratio -1

# Estilos do grafico
set style line 1 lc rgb '#B8B8B8' lw 1
set style line 2 lc rgb '#D95F02' lw 2 pt 7 ps 1.0
set style line 3 lc rgb '#1B9E77' lw 2 pt 5 ps 1.0
set style line 4 lc rgb '#111111' lw 0 pt 13 ps 1.8

plot 'outputs/contours.dat' using 1:2 with lines ls 1 title 'Curvas de nível', \
     'outputs/traj_aclive.dat' using 1:2 with linespoints ls 2 title 'Aclive Máximo', \
     'outputs/traj_fr.dat' using 1:2 with linespoints ls 3 title 'Gradientes Conjugados FR', \
     '-' using 1:2 with points ls 4 title 'Ótimo analítico'
2.0 1.0
e
