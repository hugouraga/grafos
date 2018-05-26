class No:
    def __init__(self,item = None,proximo = None):
        self.item = item
        self.proximo = proximo
        
class Lista:
    def __init__(self):
        self.primeiro = self.ultimo = No()
        self.tamanhoLista = 0
    def vazia(self):
        return self.primeiro == self.ultimo
    def inserir(self,item):
        self.ultimo.proximo = No(item)
        self.ultimo = self.ultimo.proximo
        self.tamanhoLista += 1
    def inserirInicio(self, item):
        self.primeiro.proximo = No(item,self.primeiro.proximo)
        if self.vazia():
            self.ultimo = self.primeiro.proximo
        self.tamanhoLista += 1 
    def inserirOrdenado(self,item):
        if vazia():
            self.inserir(item)
        anteiror = self.primeiro
        atual = self.primeiro.proximo
        while not atual is None and atual.item < item:
            anterior = atual
            atual = anteiror.proximo
        anterior.proximo = No(item,atual)
        if atual is None:
            self.ultimo = anteiror.proximo
        self.tamanhoLista += 1
    def inserirAres(self,verticeA,verticeB):
        aux = self.primeiro.proximo
        verificador = 0
        while verificador < verticeA and not aux is None:
            aux = aux.proximo
            verificador += 1
        aux.item.append(verticeB)
        verificador = 0
        aux = self.primeiro.proximo
        while verificador < verticeB and not aux is None:
            aux = aux.proximo
            verificador += 1
        aux.item.append(verticeA)
    def pesquisa(self, item):
        aux = self.primeiro.proximo
        while not aux is None and aux.item != item:
            aux = aux.proximo
        return aux is None and None or aux.item
    def removerInicio(self):
        if self.vazia():
            return None
        aux = self.primeiro.proximo
        self.primeiro.proximo = aux.proximo
        item = aux.item
        if aux == self.ultimo:
            self.ultimo = self.primeiro
        aux.proximo = None
        del aux
        return item
    def removerFim(self):
        if self.vazia():
            return None
        aux = self.primeiro
        while aux.proximo != self.ultimo:
            aux = aux.proximo
        item = self.ultimo.item
        ultimo = aux
        aux = ultimo.proximo
        ultimo.proximo = None
        del aux
        return item
    def __str__(self):
        s = "["
        aux = self.primeiro.proximo
        while not aux is None:
            s += str(aux.item) + ','
            aux = aux.proximo
        s = s.strip(",")
        s += "]"
        return s
    def __getitem__(self, index):
        if self.vazia():
            return IndexError("A lista se encontra vazia")
        if index > tamanhoLista or index < 0:
            return IndexError("index inválido")
        aux = self.primeiro.proximo
        ponteiro = 0
        while index > ponteiro:
            aux = aux.proximo
            ponteiro += 1
        if ponteiro == index:
            return aux.valor
    def __len__(self):
        return self.tamanhoLista
