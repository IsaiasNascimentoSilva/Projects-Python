# Utilitário 
import mysql.connector as conect





# Cores.......................................
def paleta(indice):
    cores = ['#3cd371','#dcdcdc','#1e90ff','#ff4500','#ff00ff','#ffd700','#32cd32',
             '#adff2f','#006400','#2f4f4f','#f0ffff','#ffe4b5','#00ffff','#00ff7f',
             '#191970','#6495ed','#483d8b','#8b8378','#ffe4c4','#ff4040','#8b1a1a',
             '#ff8c69','#8b4c39','#ffa500','#8b5a00','#ff7256','#8b3e2f','#ff4590',
             '#ff1493','#8b0a50','#eec900','#8b658b','#90ee90','#8b008b','#008b8b',
             '#00008b','#a9a9a9','#e8e8e8','#828282','#1c1c1c','#8968cd','#bf3eff',
             '#e066ff','#eeaeee','#ff3e96','#ff34b3','#ffb5c5','#54ff9f','#b4eeb4',
             '#76eec6','#8deeee','#00868b','#daa520','#ffff00','#ffffe0','#00fa9a',
             '#20b2aa','#556b2f','#4682b4','#b0c4de','#00ced1','#e0ffff','#cd2626']
    return cores[indice]
    
 # 
def verifiq(cedenc1,credenc2):
     pass
    
# Gera hash code...........................................
def hashCode(str):
     return hash(str)
    
# Verifica se duas string são iguais
def equals(str1,str2):
     return str1 == str2
    
# Conecta banco de dados
def connectDB():
     db = conect.connect(
        host="localhost",
        user="isaias2022",
        password="isaias160199",
        database="dbSystem"
    )
     return db

# Gera o código do produto
def geraProd(name):
     result = "55"
     for i in name.upper():
          result += str(ord(i))
     
     return pattern(result)

# Verifica se é numero
def isNumber(num:str):
     lista = '012345679'
     for i in num:
          if i != '.':
               if not i in lista:
                    return False
     return True

# Deixa o código do produto no tamanho padrão
def pattern(cod:str):
     newCod = ''
     if len(cod) >= 13:
          newCod = cod[0:13]
     else:
          newCod = cod
          for cd in range(len(cod),13,1):
               newCod += '0'
     return newCod
