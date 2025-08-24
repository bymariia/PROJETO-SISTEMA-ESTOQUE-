from defs import erro

class Pilha:
    def __init__(self):
        self.itens = []
    
    def __str__(self): #"To string" ;).
        return str(self.itens)

    def esta_vazia(self):
        return len(self.itens) == 0
    
    def empilhar(self, item):
        self.itens.append(item)
            
    def desempilhar(self):
        if self.esta_vazia():
            erro("Sem operações para serem desfeitas.")
        return self.itens.pop()
    
    def topo(self):
        if self.esta_vazia():
            erro("Sem operações.")
        return self.itens[-1]
    
    def tamanho(self):
        return len(self.itens)
    
class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0
    
    def enfileirar(self, item):
        if item is None:
            erro("Item inválido.")
        elif item in self.itens:
            erro("Esse item já existe.")
        self.itens.append(item)
    
    def desenfileirar(self):
        if self.esta_vazia():
            erro("Sem itens para serem retirados.")
        return self.itens.pop(0)
    
    def primeira(self):
        if self.esta_vazia():
            erro("Sem itens.")
        return self.itens(0)
    
    def tamanho(self):
        return len(self.itens)
    
    def listar(self):
        if self.esta_vazia():
            erro("Sem itens.")
        for item in self.itens:
            print(item)