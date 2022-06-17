
import random

# Representa a conta de um cliente........................
class Conta:
    id = None
    products = {}
    client = None
    saldo = 0.0
    register = {}
    
    def __init__(self) -> None:
        self.id = random.randint(10000,99999)
        
    def getProdut(self):
        return self.products
    
    def getId(self):
        return self.id
    
    def getSaldo(self):
        return self.saldo
    
    def getRegister(self):
        return self.register