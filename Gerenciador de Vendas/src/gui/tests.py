

from cadProduct import CadastProduct
from repository import*

# -----------------------------Repository-----------------------------------

# Cadastros.................

# * Produtos

print(Repository.cadastrar('11111111','Biscoito',2.30,'Comida'))
print(Repository.cadastrar('22222222','Sorvete',4.00,'Diverso'))
print(Repository.cadastrar('33333333','Bolacha',3.50,'Comida'))
print(Repository.cadastrar('44444444','Laranja',2.25,'Suco'))
print(Repository.cadastrar('55555555','Cerveja',7.00,'Bebida'))
print(Repository.cadastrar('66666666','Pastel',3.00,'Comida'))

# * Clientes
Repository.addCli('André','00000000000','9832-6789','São Paulo')
Repository.addCli('Paulo','00123400111','9806-6729','Areia')
Repository.addCli('Gessica','34560000000','9152-6701','Alagoa Grande')
Repository.addCli('Thiago','0000006790','9322-8889','Juarez')
Repository.addCli('Marcos','75392000000','9860-6049','Guarabira')

# * Contas
Repository.addConta('00000',63.90,'00000000000')
Repository.addConta('11111',24.00,'34560000000')
Repository.addConta('22222',92.30,'00123400111')
Repository.addConta('33333',50.50,'0000006790')
Repository.addConta('44444',12.60,'75392000000')

# Deletar.................

# *Produtos

#print(Repository.removeProd(55555555))
print(delConta("00000000000"))
print(Repository.delCli("00000000000"))

# Exibir................................

# *Produtos
print(Repository.getProd('22222222'))
print(Repository.getProd('55555555'))
print(Repository.getProds())
print(Repository.getProdN("cerv"))

# *Clientes
print(Repository.getCli('00123400111'))
