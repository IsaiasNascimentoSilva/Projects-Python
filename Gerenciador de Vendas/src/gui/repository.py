
from utilitarios.utilyt import*


class Repository():
    
    
    # Cadastra Produto
    def cadastrar(id,name,preco,category):
        
        db = connectDB()
        myCursor = db.cursor()
        comand = "INSERT INTO Produtos(ID, Nome, Preço, Categoria) VALUES(%s, %s, %s, %s)"
        val = (id, name, preco, category)
        myCursor.execute(comand, val)
        db.commit()
        
    # Remover Produto
    def removeProd(id):
        db = connectDB()
        mycursor = db.cursor()
        comand = "DELETE FROM Produtos WHERE ID = %s"%(id)
        mycursor.execute(comand)
        db.commit()
    
    # Busca Produto
    def getProd(id):
        db = connectDB()
        mycursor = db.cursor()
        comand = "SELECT * FROM Produtos WHERE ID = %s"%(id)
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
    def addCli(name,id,phone,adress,conta):
        db  = connectDB()
        mycursor = db.cursor()
        cmd = "INSERT INTO Clientes(ID, Nome, Telefone, Endereço, Conta) VALUES(%s, %s, %s, %s, %s)"
        vlr = (id,name,phone,adress,conta)
        mycursor.execute(cmd,vlr)
        db.commit()
    
    # Busca Cliente
    def getCli(id):
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
        mycursor.execute(comand)
        db.commit()

    # Adiciona conta
    def addConta(id,saldo,date):
        db  = connectDB()
        mycursor = db.cursor()
        cmd = "INSERT INTO Contas(ID, Saldo, Data) VALUES(%s, %s, %s)"
        vlr = (id,saldo,date)
        mycursor.execute(cmd,vlr)
        db.commit()
        
    # Busca conta
    def getConta(id):
        db = connectDB()
        mycursor = db.cursor()
        cmd = "SELECT * FROM Contas WHERE ID = %s"%(id)
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
    
    # Exclui uma conta
    def delConta(id):
        db = connectDB()
        mycursor = db.cursor()
        comand = "DELETE FROM Contas WHERE ID = %s"%(id)
        mycursor.execute(comand)
        db.commit()
        
    # Adiciona Registro
    def addReg(cod,prod,valor,data,qtd,conta):
        db  = connectDB()
        mycursor = db.cursor()
        cmd = "INSERT INTO Registros(Codigo, Produto, Valor, Data, Quantidade, Conta) VALUES(%s, %s, %s, %s, %s, %s)"
        vlr = (cod,prod,valor,data,qtd,conta)
        mycursor.execute(cmd,vlr)
        db.commit()
        
    # Busca registros
    def getReg(conta):
        db = connectDB()
        mycursor = db.cursor()
        comand = "SELECT * FROM Registros WHERE Conta = %s"%(conta)
        mycursor.execute(comand)
        result = mycursor.fetchall()
        return result
    
    # Excluir Registos
    def delReg(conta):
        db = connectDB()
        mycursor = db.cursor()
        comand = "DELETE FROM Registros WHERE Conta = %s"%(conta)
        mycursor.execute(comand)
        db.commit()
        
# Auxiliares----------------------
def verific(id):
    pass
