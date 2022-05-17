
# Representa um produto.................................
class Produto:
    nome = ''
    cod = ''
    valor = 0.0
    category = ''
    
    def __init__(self,name,cod,valor,category):
        self.nome = name
        self.cod = cod
        self.valor = valor
        self.category = category
        
    def setNome(self,nwname):
        self.nome = nwname
        
    def getNome(self):
        return self.nome

    def setCod(self,nwcod):
        self.cod = nwcod
        
    def getCod(self):
        return self.cod
    
    def setValor(self,nwvalor):
        self.valor = nwvalor
        
    def getValor(self):
        return self.valor
    
    def setCategory(self,nwcategory):
        self.category = nwcategory
        
    def getCategory(self):
        return self.category