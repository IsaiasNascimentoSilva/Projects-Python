
# Representa um produto.................................
from numpy import double


class Produto:
    nome : str
    id : str
    valor : double
    category : str
    
    def __init__(self,id,name,valor,category):
        self.nome = name.upper()
        self.id = id
        self.valor = valor
        self.category = category
        
    def setNome(self,nwname):
        self.nome = nwname
        
    def getNome(self):
        return self.nome
        
    def getid(self):
        return self.id
    
    def setValor(self,nwvalor):
        self.valor = nwvalor
        
    def getValor(self):
        return self.valor
    
    def setCategory(self,nwcategory):
        self.category = nwcategory
        
    def getCategory(self):
        return self.category