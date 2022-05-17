from tkinter.ttk import*
from tkinter import*

from numpy import record
from produto import Produto

# Atributos------------------------------------
products = [Produto]


root = Tk()
root.title('Gerency')
root.geometry('1400x700')

# Topo
f_top = Frame(root,width=700,height=60,background='#32cd32')
f_top.grid(row=0,column=0)

# Botão Menu
menuB = Menubutton(f_top,text='Menu',font='Arial 14',background='#32cd32')
menu = Menu(menuB,tearoff=0)
menus = ('Cadastrar','Deletar','Vendas')
for vary in menus:
    menu.add_radiobutton(label=vary,value=vary)
menuB['menu'] = menu
menuB.place(x=15,y=10)

# Botão Configuração
confB = Menubutton(f_top,text='Configuração',font='Arial 14',background='#32cd32')
conf = Menu(confB,tearoff=0)
menus = ('Conta','Senha','Sair')
for vary in menus:
    conf.add_radiobutton(label=vary,value=vary)
confB['menu'] = conf
confB.place(x=130,y=10)

# Botão Ajuda
ajudaB = Menubutton(f_top,text='Ajuda',font='Arial 14',background='#32cd32')
ajuda = Menu(ajudaB,tearoff=0)
menus = ('Sobre','Suporte')
for vary in menus:
    ajuda.add_radiobutton(label=vary,value=vary)
ajudaB['menu'] = ajuda
ajudaB.place(x=280,y=10)

# Seletor de Categorias
c_categ = Combobox(root,justify='center')
c_categ['values'] = ('<CATEGORIA>','Suco','Drink','Cerveja','Dose','Petisco','Refeição','Sanduíche','Diversos')
c_categ.current(0)
c_categ.grid(row=1,column=0)

# frame de Produtos
f_prod = Frame(root,width=700,height=240,background='#dcdcdc')
f_prod.grid(row=2,column=0)

# Exibi os Produtos-------------------------------------------
# Definir as colunas
col = ('nome','codigo','valor')
tree = Treeview(f_prod,columns=col,show='headings')

# Define os titulos
tree.heading('nome',text='Nome')
tree.heading('codigo',text='Código')
tree.heading('valor',text='Valor')

# Inserir dados na treeview

# função de evento 
def selected(event):
    for item_select in tree.selection():
        item = tree.item(item_select)
        record = item['values']
        
tree.bind('<<TreeviewSelet>>', selected)
tree.grid(row=0,column=0,sticky='nsew')

# Add deslizadores auxiliar
scrollbar = Scrollbar(f_prod,orient=VERTICAL,command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0,column=1,sticky='ns')

root.mainloop()