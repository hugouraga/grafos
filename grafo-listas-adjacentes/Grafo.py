from Lista import Lista

class Matriz:
    def __init__(self,quantVertices = 0):
        self.quantVertices = quantVertices
        self.listaVertices = Lista()

        for elemento in range(quantVertices):
            self.listaVertices.inserir([])
    def vazia(self):
        return self.quantVertices == 0
    def inserirAresta(self,verticeA,verticeB,grafoDirecionado=True):
        self.listaVertices.inserirAres(verticeA,verticeB)
        
    def __str__(self):
        return self.listaVertices.__str__()
 
