
# Representa um produto.................................
class Produto:
    nome = ''
    id = ''
    valor = 0.0
    category = ''
    
    def __init__(self,name,id,valor,category):
        self.nome = name
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