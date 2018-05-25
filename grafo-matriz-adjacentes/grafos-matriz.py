class Grafo:
    def __init__(self, quantVertices=0):
        self.quantVertices  = quantVertices
        self.matrizAdjacentes = [quantVertices * [0] for quant in range(quantVertices)]
    def grafoVazio(self):
        return self.quantVertices == 0
    def inserirArestas(self, verticeA, verticeB, grafoDirecionado = True):
        self.grafoDirecionado = grafoDirecionado
        if self.grafoVazio():
            return IndexError("o Grafo é vazio!")
        if self.grafoDirecionado is True:
            self.matrizAdjacentes[verticeA][verticeB] = 1
            self.matrizAdjacentes[verticeB][verticeA] = 1
        elif self.grafoDirecionado is False:
            self.matrizAdjacentes[verticeA][verticeB] = 1
        else:
            return IndexError("O índice é inválido!")
        
        