from tkinter.ttk import*
from tkinter import*
from gui.utilitarios.utilyt import*


root = Tk()
root.title('Gerency')
root.geometry('1400x700')

#------------------------Topo------------------------------
f_top = Frame(root,width=700,height=60,background=paleta(6))
f_top.grid(row=0,column=0)

# Botão Menu
menuB = Menubutton(f_top,text='Menu',font='Arial 14',background=paleta(6))
menu = Menu(menuB,tearoff=0)
menus = ('Cadastrar','Deletar','Vendas')
for vary in menus:
    menu.add_radiobutton(label=vary,value=vary)
menuB['menu'] = menu
menuB.place(x=15,y=10)

# Botão Configuração
confB = Menubutton(f_top,text='Configuração',font='Arial 14',background=paleta(6))
conf = Menu(confB,tearoff=0)
menus = ('Conta','Senha','Sair')
for vary in menus:
    conf.add_radiobutton(label=vary,value=vary)
confB['menu'] = conf
confB.place(x=130,y=10)

# Botão Ajuda
ajudaB = Menubutton(f_top,text='Ajuda',font='Arial 14',background=paleta(6))
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
c_categ.grid(column=0,row=1)

#-----------------------------------frame de Produtos----------------------------------------
f_prod = Frame(root,width=700,height=240,background=paleta(1))
f_prod.grid(row=2,column=0)

#....................................Exibi os Produtos........................................
# Definir as colunas
col = ('nome','codigo','valor')
tree = Treeview(f_prod,columns=col,show='headings')

# Define os titulos
tree.heading('nome',text='Nome')
tree.heading('codigo',text='Código')
tree.heading('valor',text='Valor')

# Inserir dados na treeview
data = [('AÇUCAR','22222222',2.60)]
for dt in data:
    tree.insert('',END,values=dt)
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

#--------------------------------frame de clientes------------------------------------------
f_client = Frame(root,width=700,height=320,bg=paleta(1))
f_client.grid(row=3,column=0)

# Botões 
b_exebir = Button(f_client,text='Exibir Pendências',font='Arial 12')
b_exebir.place(x=40, y=20)

b_ocutar = Button(f_client,text='Ocultar Pendências',font='Arial 12')
b_ocutar.place(x=220, y=20)

#....................................Tabela de pendências........................................
# Definir as colunas
col = ('nome','cpf')
pedence = Treeview(f_client,columns=col,show='headings')

# Define os titulos
pedence.heading('nome',text='Nome')
pedence.heading('cpf',text='Cpf')

# Inserir dados na treeview

# função de evento 
def selected1(event):
    for item_select in pedence.selection():
        item = pedence.item(item_select)
        selec = item['values']
        
pedence.bind('<<TreeviewSelet>>', selected1)
pedence.place(x=40,y=80)

# Add deslizadores auxiliar
scrollbar1 = Scrollbar(f_client,orient=VERTICAL,command=pedence.yview)
pedence.configure(yscroll=scrollbar1.set)
scrollbar1.place(x=440,y=80)

root.mainloop()