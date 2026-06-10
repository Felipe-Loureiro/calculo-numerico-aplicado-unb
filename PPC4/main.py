# -*- coding: utf-8 -*-

"""
PPC4 - Otimizacao bidimensional sem restricoes

Aluno: Felipe Tavares Loureiro
Professor: Rafael Gabler Gontijo

Funcao objetivo:
    f(x, y) = 2xy + 2x - x^2 - 2y^2

Metodos implementados:
    1) Aclive Maximo
    2) Gradientes Conjugados Fletcher-Reeves

Arquivos gerados:
    outputs/output1.dat      -> log do Aclive Maximo
    outputs/output2.dat      -> log dos Gradientes Conjugados FR
    outputs/function.dat     -> amostras x y f(x,y) para curvas de nivel
    outputs/traj_aclive.dat  -> trajetoria do Aclive Maximo
    outputs/traj_fr.dat      -> trajetoria dos Gradientes Conjugados FR

Formato dos logs:
    iter erro h x y dfx dfy
"""

import os


TOLERANCIA_PADRAO = 1.0e-6       # criterio de parada: norma do gradiente menor que este valor
MAX_ITER_PADRAO = 100            # limite maximo de iteracoes para evitar execucao indefinida
NUMERO_PONTOS_GRAFICO = 121      # quantidade de pontos por eixo na malha de curvas de nivel


def f_obj(x, y):
    """Funcao objetivo a ser maximizada."""
    return 2.0*x*y + 2.0*x - x*x - 2.0*y*y  # f(x,y) definida no enunciado


def grad_f(x, y):
    """Gradiente da funcao objetivo."""
    dfx = 2.0*y + 2.0 - 2.0*x  # derivada parcial df/dx = 2y + 2 - 2x
    dfy = 2.0*x - 4.0*y        # derivada parcial df/dy = 2x - 4y
    return [dfx, dfy]          # vetor gradiente no ponto (x,y)


def produto_escalar(vetor_a, vetor_b):
    """Produto escalar entre dois vetores bidimensionais."""
    return vetor_a[0]*vetor_b[0] + vetor_a[1]*vetor_b[1]


def norma(vetor):
    """Norma euclidiana de um vetor bidimensional."""
    return (vetor[0]*vetor[0] + vetor[1]*vetor[1])**0.5


def preparar_pasta_outputs():
    """Cria a pasta outputs caso ela ainda nao exista."""
    if not os.path.exists("outputs"):
        os.mkdir("outputs")


def melhor_h_por_amostragem(amostras):
    """
    Escolhe o h que gera o maior valor de g(h)
    entre os pontos ja calculados.

    Essa funcao e usada como fallback quando a interpolacao
    quadratica nao consegue definir um vertice confiavel.
    """
    melhor_h = amostras[0][0]  # primeiro valor de h testado
    melhor_g = amostras[0][1]  # valor correspondente de g(h)

    for i in range(1, len(amostras)):
        h_atual = amostras[i][0]
        g_atual = amostras[i][1]

        if g_atual > melhor_g:  # em maximizacao, interessa o maior valor de g(h)
            melhor_h = h_atual
            melhor_g = g_atual

    return melhor_h


def passo_interpolacao_quadratica(x, y, direcao):
    """
    Linha de busca unidimensional por interpolacao quadratica.

    A funcao unidimensional analisada e:
        g(h) = f(x + h*px, y + h*py)

    Sao usados tres pontos:
        h0 = 0, h1 = 1, h2 = 2

    Caso a parabola fique degenerada, o metodo usa fallback:
    escolhe o melhor h entre h0, h1 e h2.
    """

    h0 = 0.0  # ponto atual: nao ha deslocamento na direcao de busca
    h1 = 1.0  # primeira tentativa de passo
    h2 = 2.0  # segunda tentativa de passo

    tolerancia_denominador = 1.0e-14  # evita divisao por numero praticamente nulo

    px = direcao[0]  # componente x da direcao de busca
    py = direcao[1]  # componente y da direcao de busca

    # Valores da funcao unidimensional g(h) nos tres pontos escolhidos.
    g0 = f_obj(x + h0*px, y + h0*py)  # g(h0)
    g1 = f_obj(x + h1*px, y + h1*py)  # g(h1)
    g2 = f_obj(x + h2*px, y + h2*py)  # g(h2)

    amostras = [
        [h0, g0],
        [h1, g1],
        [h2, g2]
    ]  # pares [h, g(h)] usados caso seja necessario aplicar fallback

    # Formula do vertice da parabola interpoladora definida pelos tres pontos.
    # O fator 0.5 aparece diretamente da expressao fornecida no enunciado.
    numerador = 0.5 * (
        (h0*h0 - h2*h2)*g1 +
        (h2*h2 - h1*h1)*g0 +
        (h1*h1 - h0*h0)*g2
    )

    denominador = (
        (h0 - h2)*g1 +
        (h2 - h1)*g0 +
        (h1 - h0)*g2
    )

    if abs(denominador) < tolerancia_denominador:
        return melhor_h_por_amostragem(amostras)  # fallback: parabola degenerada

    h_otimo = numerador / denominador  # passo associado ao vertice da parabola

    if h_otimo < 0.0:
        return melhor_h_por_amostragem(amostras)  # evita andar no sentido oposto da busca

    return h_otimo


def escrever_log(arquivo, iteracao, erro, h, x, y, dfx, dfy):
    """
    Escreve uma linha no formato pedido:
        iter erro h x y dfx dfy
    """
    arquivo.write(
        "%d %.12e %.12e %.12e %.12e %.12e %.12e\n" %
        (iteracao, erro, h, x, y, dfx, dfy)
    )


def imprimir_iteracao(nome_metodo, iteracao, x, y, h, erro):
    """Imprime o estado atual da iteracao no terminal."""
    print(
        "%s | iter %3d | x = %.10f | y = %.10f | f = %.10f | h = %.10e | erro = %.10e" %
        (nome_metodo, iteracao, x, y, f_obj(x, y), h, erro)
    )


def metodo_aclive_maximo(x0, y0, tolerancia, max_iter):
    """
    Executa o metodo do Aclive Maximo.

    Neste metodo, a direcao de busca e sempre:
        p = grad(f)
    """

    x = x0  # coordenada x do ponto atual
    y = y0  # coordenada y do ponto atual

    trajetoria = []
    trajetoria.append([x, y])  # guarda o ponto inicial para plotagem posterior

    arquivo = open("outputs/output1.dat", "w")
    arquivo.write("# iter erro h x y dfx dfy\n")  # cabecalho do log pedido no enunciado

    print("")
    print("=== ACLIVE MAXIMO ===")

    for iteracao in range(max_iter):
        gradiente = grad_f(x, y)  # gradiente avaliado no ponto atual

        dfx = gradiente[0]  # componente x do gradiente
        dfy = gradiente[1]  # componente y do gradiente

        erro = norma(gradiente)  # criterio de erro: modulo do gradiente

        if erro < tolerancia:  # quando o gradiente e quase nulo, o ponto critico foi atingido
            print("Aclive Maximo convergiu.")
            break

        direcao = [dfx, dfy]  # no Aclive Maximo, a direcao e o proprio gradiente

        h = passo_interpolacao_quadratica(x, y, direcao)  # busca linear para escolher o passo

        escrever_log(arquivo, iteracao, erro, h, x, y, dfx, dfy)
        imprimir_iteracao("Aclive Maximo", iteracao, x, y, h, erro)

        x = x + h*direcao[0]  # atualizacao do ponto na direcao de busca
        y = y + h*direcao[1]

        trajetoria.append([x, y])  # salva o novo ponto para desenhar a trajetoria

    arquivo.close()

    print("")
    print("Resultado Aclive Maximo:")
    print("x = %.12f" % x)
    print("y = %.12f" % y)
    print("f = %.12f" % f_obj(x, y))
    print("erro = %.12e" % norma(grad_f(x, y)))
    print("iteracoes realizadas = %d" % (len(trajetoria) - 1))

    return trajetoria


def metodo_gradientes_conjugados_fr(x0, y0, tolerancia, max_iter):
    """
    Executa o metodo dos Gradientes Conjugados de Fletcher-Reeves.

    Como o problema e de maximizacao, a primeira direcao e o gradiente.

    Depois, a direcao e atualizada por:
        p_{k+1} = grad(f_{k+1}) + beta_k*p_k

    com:
        beta_k = |grad(f_{k+1})|^2 / |grad(f_k)|^2
    """

    x = x0  # coordenada x do ponto atual
    y = y0  # coordenada y do ponto atual

    trajetoria = []
    trajetoria.append([x, y])  # guarda o ponto inicial para plotagem posterior

    arquivo = open("outputs/output2.dat", "w")
    arquivo.write("# iter erro h x y dfx dfy\n")  # cabecalho do log pedido no enunciado

    gradiente_anterior = [0.0, 0.0]  # usado no calculo de beta a partir da segunda iteracao
    direcao = [0.0, 0.0]             # direcao de busca atual

    print("")
    print("=== GRADIENTES CONJUGADOS FLETCHER-REEVES ===")

    for iteracao in range(max_iter):
        gradiente = grad_f(x, y)  # gradiente avaliado no ponto atual

        dfx = gradiente[0]  # componente x do gradiente atual
        dfy = gradiente[1]  # componente y do gradiente atual

        erro = norma(gradiente)  # criterio de erro: modulo do gradiente

        if erro < tolerancia:  # convergencia quando o gradiente se aproxima de zero
            print("Gradientes Conjugados FR convergiu.")
            break

        if iteracao == 0:
            direcao = [dfx, dfy]  # primeira direcao do FR: gradiente inicial
        else:
            denominador_beta = produto_escalar(
                gradiente_anterior,
                gradiente_anterior
            )  # |grad_k|^2 no denominador de Fletcher-Reeves

            if denominador_beta == 0.0:
                beta = 0.0  # evita divisao por zero caso o gradiente anterior seja nulo
            else:
                beta = produto_escalar(gradiente, gradiente) / denominador_beta
                # beta = |grad_{k+1}|^2 / |grad_k|^2

            direcao = [
                dfx + beta*direcao[0],
                dfy + beta*direcao[1]
            ]  # atualizacao da direcao: gradiente atual + parcela da direcao anterior

        h = passo_interpolacao_quadratica(x, y, direcao)  # mesma busca linear do Aclive Maximo

        escrever_log(arquivo, iteracao, erro, h, x, y, dfx, dfy)
        imprimir_iteracao("Grad. Conj. FR", iteracao, x, y, h, erro)

        x = x + h*direcao[0]  # avanca na direcao calculada pelo metodo FR
        y = y + h*direcao[1]

        trajetoria.append([x, y])  # salva o novo ponto para comparar as trajetorias

        gradiente_anterior = gradiente  # prepara o calculo de beta da proxima iteracao

    arquivo.close()

    print("")
    print("Resultado Gradientes Conjugados FR:")
    print("x = %.12f" % x)
    print("y = %.12f" % y)
    print("f = %.12f" % f_obj(x, y))
    print("erro = %.12e" % norma(grad_f(x, y)))
    print("iteracoes realizadas = %d" % (len(trajetoria) - 1))

    return trajetoria


def encontrar_limites(trajetoria_aclive, trajetoria_fr):
    """
    Determina os limites do dominio usado para gerar function.dat.

    Os limites consideram:
        - trajetoria do Aclive Maximo
        - trajetoria dos Gradientes Conjugados FR
        - ponto otimo analitico (2, 1)
    """

    pontos = trajetoria_aclive + trajetoria_fr + [[2.0, 1.0]]
    # inclui as duas trajetorias e o otimo analitico para enquadrar o grafico

    xs = [ponto[0] for ponto in pontos]  # todas as coordenadas x consideradas
    ys = [ponto[1] for ponto in pontos]  # todas as coordenadas y consideradas

    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)

    margem = 0.25 * max(xmax - xmin, ymax - ymin)  # margem visual ao redor da trajetoria

    if margem < 1.0:
        margem = 1.0  # garante uma margem minima mesmo se a trajetoria for curta

    return [
        xmin - margem,
        xmax + margem,
        ymin - margem,
        ymax + margem
    ]


def gerar_function_dat(limites):
    """
    Gera o arquivo function.dat com amostras de x, y e f(x,y).

    Esse arquivo e usado pelo Gnuplot para desenhar as curvas de nivel.
    """

    xmin = limites[0]
    xmax = limites[1]
    ymin = limites[2]
    ymax = limites[3]

    arquivo = open("outputs/function.dat", "w")
    arquivo.write("# x y f(x,y)\n")  # Gnuplot ignora linhas iniciadas por #

    for j in range(NUMERO_PONTOS_GRAFICO):
        y = ymin + (ymax - ymin)*j/(NUMERO_PONTOS_GRAFICO - 1.0)
        # coordenada y da linha atual da malha

        for i in range(NUMERO_PONTOS_GRAFICO):
            x = xmin + (xmax - xmin)*i/(NUMERO_PONTOS_GRAFICO - 1.0)
            # coordenada x da coluna atual da malha

            z = f_obj(x, y)  # valor da funcao objetivo neste ponto da malha

            arquivo.write("%.12e %.12e %.12e\n" % (x, y, z))

        arquivo.write("\n")  # linha em branco separa blocos da malha para o Gnuplot

    arquivo.close()


def salvar_trajetoria(nome_arquivo, trajetoria):
    """Salva uma trajetoria em arquivo .dat com duas colunas: x y."""

    arquivo = open(nome_arquivo, "w")
    arquivo.write("# x y\n")  # cabecalho simples para identificar as colunas

    for i in range(len(trajetoria)):
        arquivo.write(
            "%.12e %.12e\n" %
            (trajetoria[i][0], trajetoria[i][1])
        )

    arquivo.close()


def ler_float(mensagem):
    """Le um numero real digitado pelo usuario."""
    while True:
        texto = input(mensagem)

        try:
            return float(texto)
        except ValueError:
            print("Valor invalido. Digite um numero real.")


def ler_int(mensagem):
    """Le um numero inteiro digitado pelo usuario."""
    while True:
        texto = input(mensagem)

        try:
            return int(texto)
        except ValueError:
            print("Valor invalido. Digite um numero inteiro.")


def main():
    preparar_pasta_outputs()  # garante que os arquivos de saida possam ser salvos

    print("PPC4 - Aclive Maximo e Gradientes Conjugados Fletcher-Reeves")
    print("Funcao: f(x,y) = 2xy + 2x - x^2 - 2y^2")
    print("Otimo analitico esperado: x = 2, y = 1, f = 2")
    print("")

    x0 = ler_float("Digite x0: ")  # coordenada inicial x
    y0 = ler_float("Digite y0: ")  # coordenada inicial y

    print("")
    print("Parametros padrao:")
    print("tolerancia = %.1e" % TOLERANCIA_PADRAO)
    print("max_iter = %d" % MAX_ITER_PADRAO)

    usar_padrao = input("Usar parametros padrao? [s/n]: ")

    if usar_padrao == "n" or usar_padrao == "N":
        tolerancia = ler_float("Digite a tolerancia: ")
        max_iter = ler_int("Digite o numero maximo de iteracoes: ")
    else:
        tolerancia = TOLERANCIA_PADRAO
        max_iter = MAX_ITER_PADRAO

    trajetoria_aclive = metodo_aclive_maximo(
        x0,
        y0,
        tolerancia,
        max_iter
    )  # executa o metodo do Aclive Maximo

    trajetoria_fr = metodo_gradientes_conjugados_fr(
        x0,
        y0,
        tolerancia,
        max_iter
    )  # executa o metodo dos Gradientes Conjugados FR

    limites = encontrar_limites(trajetoria_aclive, trajetoria_fr)
    # define o dominio usado para gerar as curvas de nivel

    gerar_function_dat(limites)  # amostra a funcao objetivo no dominio definido

    salvar_trajetoria(
        "outputs/traj_aclive.dat",
        trajetoria_aclive
    )  # salva a trajetoria do Aclive Maximo

    salvar_trajetoria(
        "outputs/traj_fr.dat",
        trajetoria_fr
    )  # salva a trajetoria dos Gradientes Conjugados FR

    print("")
    print("Arquivos gerados:")
    print("outputs/output1.dat")
    print("outputs/output2.dat")
    print("outputs/function.dat")
    print("outputs/traj_aclive.dat")
    print("outputs/traj_fr.dat")
    print("")
    print("Para gerar o grafico:")
    print("gnuplot plot_ppc4.gp")
    print("")
    print("O grafico sera salvo como:")
    print("outputs/trajetorias.png")


if __name__ == "__main__":
    main()
