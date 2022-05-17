from datetime import datetime
import random

# Representa a conta de um cliente........................
class Conta:
    id = None
    date = None
    produtos = {}
    pago = {}
    divida = {}
    
    def __init__(self) -> None:
        self.id = random.randint(10000,99999)
        self.date = datetime.now()
        
    def getProdut(self):
        return self.produtos
    
    def getPago(self):
        return self.pago
    
    def getDivida(self):
        return self.divida