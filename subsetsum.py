# Um programa para verificar se no conjunto existe um somatório que dê 
# a capacidade

# 1) Informa se tem ou não
# 2) Se tiver mostra o primeiro encontrado
# 3) Se tiver mostra todos encontrados

# CAPACIDADE = 19
# Exemplo: A = {5,4,10,8,9,6}
#           Sub = {5,4,10} = 19


def subsets(conjunto: list, matriz_resposta: list, capacidade: int) -> list:
    """ Retorna todos os subconjuntos encontrados resultam na capacidade

    Parameters
    ----------
    conjunto: list
        lista com os valores do conjunto
    matriz_resposta: list
        matriz com o resultado do subset_sum
    capacidade: int
        soma procurada

    Returns
    -------
    list
        lista com os subconjuntos encontrados
    """

    starts = [linha for linha in range(len(conjunto)+1) if matriz_resposta[linha][capacidade]]

    resultados = list()
    append = resultados.append
    for linha in starts:
        coluna = capacidade
 
        subconjunto = set()
        add = subconjunto.add

        while coluna >= 0 and linha >= 0:
            if (coluna - conjunto[linha-1]) > 0 and coluna == capacidade:
                coluna -= conjunto[linha-1]
                linha -= 1
                add(conjunto[linha])
            elif matriz_resposta[linha][coluna] == 1:
                linha -= 1
            else:
                coluna -= conjunto[linha]
                add(conjunto[linha])

        if sum(subconjunto) == capacidade and subconjunto not in resultados:
            append(subconjunto)

    return resultados


# Complexidade = O(max_linha*max_coluna)
def subset_sum(conjunto: list, capacidade: int) -> list:
    """ Gera a matriz que verifica que se a capacidade existe no conjunto

    Parameters
    ----------
    conjunto: list
        lista com os valores do conjunto
    capacidade: int
        soma procurada

    Returns
    -------
    list
        matriz com o resultado da busca
    """
    max_coluna = capacidade + 1
    max_linha = len(conjunto) + 1

    matriz_resposta = [[0]*max_coluna for i in range(max_linha)]

    for linha in range(max_linha):
        matriz_resposta[linha][0] = 1

    for linha in range(1, max_linha):
        for coluna in range(1, max_coluna):
            if conjunto[linha-1] > coluna:
                resposta = matriz_resposta[linha-1][coluna]
            else:
                resposta = matriz_resposta[linha-1][coluna] or matriz_resposta[linha-1][coluna-conjunto[linha-1]]

            matriz_resposta[linha][coluna] = resposta

    return matriz_resposta


def subsetsum_backtracking(conjunto: list, soma: int, selecao: list, resultados: list, pos: int = 0):
    """ Verifica se a soma existe no conjunto e guarda todas as possibilidades

    Foi usado a técninca de backtracking

    Parameters
    ----------
    conjunto: list
        lista com os valores do conjunto
    soma: int
        soma procurada
    selecao: list
        lista para armazena o subconjunto
    resultados: list
        lista para armazenar os resultados
    pos: int
        posição do valor que será acessado
    """
    if soma == 0:
        resultados.append(set(selecao))
    elif pos < len(conjunto):
        selecao.append(conjunto[pos])
        subsetsum_backtracking(conjunto, soma - conjunto[pos], selecao, resultados, pos + 1)
        selecao.pop()
        subsetsum_backtracking(conjunto, soma, selecao, resultados, pos + 1)


if __name__ == "__main__":
    conjunto = list(map(int, input("Digite os valores do conjunto separado por espaço: ").split()))
    capacidade = int(input("Soma: "))
    tecninca = int(input("Qual algoritmo?\n1 - DP\n2 - Backtracking\nOpção (1/2): "))
    todos = input("Mostrar todos os encontrados (s/n)? ")

    subconjuntos = []
    if tecninca == 1:
        matriz_resposta = subset_sum(conjunto, capacidade)
        if matriz_resposta[len(conjunto)][capacidade]:
            subconjuntos = subsets(conjunto, matriz_resposta, capacidade)
    elif tecninca == 2:
        subsetsum_backtracking(conjunto, capacidade, [], subconjuntos)
    else:
        print("Opção inválida!")

    if 1 <= tecninca <= 2:
        print("="*5)
        if subconjuntos:
            print("SOMA ENCONTRADA")
            if todos == "s":
                print("SubConjuntos: ", subconjuntos)
            else:
                print("SubConjunto: ", subconjuntos[0])
        else:
            print("SOMA NÃO ENCONTRADA")
