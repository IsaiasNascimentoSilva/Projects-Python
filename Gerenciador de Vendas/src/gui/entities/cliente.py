
# Representa um cliente.......................................
class Client:
    nome = ''
    id = ''
    phone = ''
    adress = ''
    conta = None
    
    def __init__(self,name,id,phone,adress):
        self.nome = name
        self.id = id
        self.phone = phone
        self.adress = adress

#   Gets e Sets............................................
    def setName(self,newname):
        self.nome = newname
        
    def getName(self):
        return self.nome
        
    def getId(self):
        return self.id
    
    def setAdress(self,newadress):
        self.adress = newadress
        
    def getAdress(self):
        return self.adress
    
    def setPhone(self,newphone):
        self.phone = newphone
        
    def getPhone(self):
        return self.phone
    
    def getConta(self):
        return self.conta
    
    def setConta(self,newconta):
        self.conta = newconta