def calcular_unidade(pesos: list, valores: list):
    return sorted([(int(valores[i]/pesos[i]), pesos[i], valores[i]) for i, p in enumerate(pesos)], reverse=True)


def mochila_fracionaria(capacidade: int, pesos: list, valores: list):
    elementos = calcular_unidade(pesos, valores)
    total = 0
    for elemento in elementos:
        if capacidade - elemento[1] >= 0:
            capacidade -= elemento[1]
            total += elemento[2]
        else:
            total += elemento[2] * (capacidade / elemento[1])
            break
    return total


if __name__ == "__main__":
    c = int(input("Capacidade: "))
    pesos = list(map(int, input("Pesos (separados por espaço): ").split()))
    elementos = list(map(int, input("Valores (separados por espaço): ").split()))
    print("Total:", mochila_fracionaria(c, pesos, elementos))
