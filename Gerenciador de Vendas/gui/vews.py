from tkinter.ttk import*
from tkinter import*


def cadast_product():
    Cad_p = Tk()
    Cad_p.title('Cadastro de Produtos')
    Cad_p.geometry('550x640')
    Cad_p.resizable(height='FALSE', width='FALSE')
    
    f_p = Frame(Cad_p,height=380,width=550,background='#1E90FF')
    f_p.grid(row=0,column=0)
    
    f_s = Frame(Cad_p,height=260,width=550)
    f_s.grid(row=1,column=0)
    
    img = PhotoImage(file='../imgs/produt.png')
    l_img = Label(f_p,image=img,width=100,height=100,background='#1e90ff')
    l_img.place(x=220,y=18)
    
    l_prod = Label(f_p,text='Produto',background='#1e90ff',font='Arial 14')
    l_prod.place(x=35, y=120)
    
    e_prod = Entry(f_p,width=30)
    e_prod.place(x=35,y=150)
    
    l_prec = Label(f_p,text='Preço',background='#1e90ff',font='Arial 14')
    l_prec.place(x=315,y=120)
    
    e_prec = Entry(f_p,width=15)
    e_prec.place(x=315,y=150)
    
    c_categ = Combobox(f_p)
    c_categ['values'] = ('<CATEGORIA>','Suco','Drink','Cerveja','Dose','Petisco','Refeição','Sanduíche','Diversos')
    c_categ.current(0)
    c_categ.place(x=35,y=200)
    
    b_cad = Button(f_p,text="Cadastrar",width=20,height=2)
    b_cad.place(x=35,y=270)
    
    b_cans = Button(f_p,text="Finalizar",width=20,height=2)
    b_cans.place(x=285,y=270)
    
    Cad_p.mainloop()

def cadast_Client():
    pass

cadast_product()