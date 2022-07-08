
from gui.utilitarios.utilyt import*
from gui.entities.produto import Produto


class Repository():
    
    
    # Cadastra Produto
    def cadastrar(self,product:Produto):
        id = product.getid()
        if contains("Produtos",id):
            return False
        
        db = connectDB()
        myCursor = db.cursor()
        comand = "INSERT INTO Produtos(ID, Nome, Preço, Categoria) VALUES(%s, %s, %s, %s)"
        prod = product.getNome()
        price = str(product.getValor())
        categ = product.getCategory()
        val = (id,prod,price,categ)
        myCursor.execute(comand, val)
        db.commit()
        return True
        
    # Remover Produto
    def removeProd(id):
        db = connectDB()
        mycursor = db.cursor()
        comand = "DELETE FROM Produtos WHERE ID = %s"%(id)
        mycursor.execute("DELETE FROM Registros WHERE Produto = %s"%(id))
        db.commit()
        mycursor.execute(comand)
        db.commit()
        return True
    
    # Busca Produto por código
    def getProd(id):
        if not contains("Produtos",id):
            return "Produto não cadastrado!"
        db = connectDB()
        mycursor = db.cursor()
        comand = "SELECT * FROM Produtos WHERE ID = %s"%(id)
        mycursor.execute(comand)
        result = mycursor.fetchone()
        return result
    
    # Buscar Produto por nome
    def getProdN(str):
        strM = str.upper()
        db = connectDB()
        mycursor = db.cursor()
        comand = "SELECT * FROM Produtos WHERE Nome LIKE '%"+strM+"%'"
        mycursor.execute(comand)
        result = mycursor.fetchone()
        return result
    
    # Busca Produtos
    def getProds():
        db = connectDB()
        mycursor = db.cursor()
        comand = "SELECT * FROM Produtos"
        mycursor.execute(comand)
        result = mycursor.fetchall()
        return result
    
    # Adicionar Cliente
    def addCli(name,id,phone,adress):
        if contains("Clientes",id):
            return False
        db  = connectDB()
        mycursor = db.cursor()
        cmd = "INSERT INTO Clientes(ID, Nome, Telefone, Endereço) VALUES(%s, %s, %s, %s)"
        vlr = (id,name,phone,adress)
        mycursor.execute(cmd,vlr)
        db.commit()
        return True
    
    # Busca Cliente
    def getCli(id):
        if not contains("Clientes",id):
            return "Cliente não registrado!"
        db = connectDB()
        mycursor = db.cursor()
        cmd = "SELECT * FROM Clientes WHERE ID = %s"%(id)
        mycursor.execute(cmd)
        result = mycursor.fetchone()
        return result
    
    # Busca Clientes
    def getClis():
        db = connectDB()
        mycursor = db.cursor()
        comand = "SELECT * FROM Clientes"
        mycursor.execute(comand)
        result = mycursor.fetchall()
        return result
    
    # Excluir Cliente
    def delCli(id):
        db = connectDB()
        mycursor = db.cursor()
        comand = "DELETE FROM Clientes WHERE ID = %s"%(id)
        delConta(id)
        mycursor.execute(comand)
        db.commit()
        return True

    # Adiciona conta
    def addConta(id,saldo,client):
        if contains("Contas",id):
            return False
        db  = connectDB()
        mycursor = db.cursor()
        cmd = "INSERT INTO Contas(ID, Saldo, Cliente) VALUES(%s, %s, %s)"
        vlr = (id,saldo,client)
        mycursor.execute(cmd,vlr)
        db.commit()
        return True
        
    # Busca conta
    def getConta(id):
        if not contains("Clientes",id):
            return "Cliente não registrado!"
        db = connectDB()
        mycursor = db.cursor()
        cmd = "SELECT * FROM Contas WHERE Cliente = %s"%(id)
        mycursor.execute(cmd)
        result = mycursor.fetchone()
        return result
    
    # Busca contas
    def getContas():
        db = connectDB()
        mycursor = db.cursor()
        comand = "SELECT * FROM Contas"
        mycursor.execute(comand)
        result = mycursor.fetchall()
        return result
        
    # Adiciona Registro
    def addReg(prod,valor,qtd,conta):
        
        db  = connectDB()
        mycursor = db.cursor()
        cmd = "INSERT INTO Registros(Produto, Valor, Quantidade, Conta) VALUES(%s, %s, %s, %s)"
        vlr = (prod,valor,qtd,conta)
        mycursor.execute(cmd,vlr)
        db.commit()
        return True
        
    # Busca registros
    def getReg(conta):
        if  not contains("Contas",conta):
            return "Conta não registrada!"
        db = connectDB()
        mycursor = db.cursor()
        comand = "SELECT * FROM Registros WHERE Conta = %s"%(conta)
        mycursor.execute(comand)
        result = mycursor.fetchall()
        return result    
        
# --------------------------Auxiliares----------------------
# Verifica se o dado já está registrado no db
def contains(table,id):
    db = connectDB()
    mycursor = db.cursor()
    cmd = "SELECT ID FROM %s WHERE EXISTS (SELECT * FROM %s WHERE ID = %s) LIMIT 1"%(table,table,id)
    mycursor.execute(cmd)
    list = mycursor.fetchall()
    if list.__len__() < 1:
        return False
    return True

# Exclui uma conta
def delConta(id):
    
    db = connectDB()
    mycursor = db.cursor()
    comand = "DELETE FROM Contas WHERE Cliente = %s"%(id)
    mycursor.execute("SELECT ID FROM Contas WHERE EXISTS (SELECT * FROM Contas WHERE Cliente = %s) LIMIT 1"%(id))
    conta = mycursor.fetchall()
    if conta.__len__() > 1:
        delReg(conta[0])
    mycursor.execute(comand)
    db.commit()
    return True

# Excluir Registos
def delReg(conta):
    db = connectDB()
    mycursor = db.cursor()
    comand = "DELETE FROM Registros WHERE Conta = %s"%(conta)
    mycursor.execute(comand)
    db.commit()
    return True