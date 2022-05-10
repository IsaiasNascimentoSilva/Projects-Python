from tkinter.ttk import*
from tkinter import*

root = Tk()
root.title('OpenBar')
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

# Exibe Produtos
f_prod = Frame(root,width=700,height=240,background='#dcdcdc')
f_prod.grid(row=2,column=0)

root.mainloop()