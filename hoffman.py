# contar freq dos símbolos, depois fazer a ordenação da menos para mais freq
# montar árvore binária, agrupando símbolos e freq
#   removemos os dois primeiros elementos da fila de prioridade e agrupamos eles em um nó pai
# percorrer a árvore para montar o dicionário com o novo códifo de cada símbolo
#   esquerda 0 e direita 1
# re-codificar os dados usando o dicionário
# decodificação, percorre a árvore e sempre volra para a raíz quando encontra a letra

import heapq
from time import time
from collections import Counter


class No:
    def __init__(self, valor, frequencia):
        self.valor = valor
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __repr__(self):
        return f"Valor: {self.valor} - Freq: {self.frequencia}"

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia


class Huffman:
    """ Huffman é um algoritmo de compressão de dados sem perdas

    Complexidade de O(m + nlog(n))
    m: comprimento da mensagem
    n: número de caracteres distintos
    """
    def __init__(self, texto):
        self.texto = texto
        self.texto_frequencia = self.frequencia(texto)
        self.arvore = self.montar_arvore(self.texto_frequencia)
        self.raiz = heapq.heappop(self.arvore)
        self.codigos = {}
        self.montar_codigos()

    def frequencia(self, texto):
        return Counter(texto)

    def montar_arvore(self, texto_frequencia):
        arv = []
        for letra, freq in texto_frequencia.items():
            heapq.heappush(arv, No(letra, freq))
        
        while len(arv) > 1:
            no_esquerda = heapq.heappop(arv)
            no_direita = heapq.heappop(arv)

            no = No(None, no_esquerda.frequencia + no_direita.frequencia)
            no.esquerda = no_esquerda
            no.direita = no_direita

            heapq.heappush(arv, no)

        return arv

    def __codigo(self, no, codigo):
        if no is None:
            return
        elif no.valor is not None:
            self.codigos[no.valor] = codigo
            self.codigos[codigo] = no.valor
        else:
            self.__codigo(no.esquerda, codigo + "0")
            self.__codigo(no.direita, codigo + "1")

    def montar_codigos(self):
        self.__codigo(self.raiz, "")

    def pad(self, binario):
        binario = "1" + binario
        faltante = 8 - len(binario) % 8
        return binario.zfill(len(binario) + faltante)

    def comprimir(self):
        return self.pad("".join([self.codigos[letra] for letra in self.texto]))

    def remover_pad(self, binario):
        for index, valor in enumerate(binario):
            if valor == "1":
                break

        return binario[index+1:]

    def descompactar(self, binario):
        codigo, texto = "", ""
        for b in self.remover_pad(binario):
            codigo += b
            letra = self.codigos.get(codigo, None)
            if letra is not None:
                texto += letra
                codigo = ""

        return texto


if __name__ == "__main__":
    print(Huffman.__doc__)

    texto = input("Digite o texto: ")
    hff = Huffman(texto)
    binario_original = "".join([str(bin(ord(letra)))[2:].zfill(8) for letra in texto])
    print("Quantidade binário original:", len(binario_original))
    print("Binário:", binario_original)

    print()

    binario_comprimido = hff.comprimir()
    print("Quantidade binário comprimido:", len(binario_comprimido))
    print("Binário Comprimido:", binario_comprimido)

    print()

    print("Texto descomprimido:", hff.descompactar(binario_comprimido))
