from tkinter import messagebox
from tkinter.ttk import*
from tkinter import*

from numpy import double
from gui.repository import Repository
from gui.utilitarios.utilyt import*

from gui.entities.produto import Produto


class CadastProduct(Tk):
    product : str
    price : str
    category : str
    
    def __init__(self):
        super().__init__()
        self.title('Cadastro de Produtos')
        self.geometry('630x640')
        self.resizable(height='FALSE', width='FALSE')

        f_p = Frame(self,height=380,width=630,background='#1E90FF')
        f_p.grid(row=0,column=0)

        f_s = Frame(self,height=260,width=550)
        f_s.grid(row=1,column=0)
    
        self.img = PhotoImage(master=self,file='imgs/produt.png')
        l_img = Label(f_p,image=self.img,width=100,height=100,background='#1e90ff')
        l_img.place(x=260,y=18)

        l_prod = Label(f_p,text='Produto',background='#1e90ff',font='Arial 14')
        l_prod.place(x=75, y=120)

        self.e_prod = Entry(f_p,width=30)
        self.e_prod.place(x=75,y=150)

        l_prec = Label(f_p,text='Preço',background='#1e90ff',font='Arial 14')
        l_prec.place(x=355,y=120)

        self.e_prec = Entry(f_p,width=15)
        self.e_prec.place(x=355,y=150)

        self.c_categ = Combobox(f_p)
        self.c_categ['values'] = ('<CATEGORIA>','Suco','Drink','Cerveja','Dose','Petisco','Refeição','Sanduíche','Diversos')
        self.c_categ.current(0)
        self.c_categ.place(x=75,y=200)

        b_cad = Button(f_p,text="Cadastrar",width=20,height=2,command=self.register)
        b_cad.place(x=75,y=270)

        b_cans = Button(f_p,text="Finalizar",width=20,height=2,command=self.close)
        b_cans.place(x=325,y=270)
        
        col = ('codigo','produto','preco')
        self.tree = Treeview(f_s,columns=col,show='headings')
        
        self.tree.heading('codigo',text='Código')
        self.tree.heading('produto',text='Produto')
        self.tree.heading('preco',text='Preço')
        
        self.tree.grid(column=0,row=0,sticky='nsew')
        
        scro = Scrollbar(f_s,orient=VERTICAL,command=self.tree.yview)
        self.tree.configure(yscroll=scro.set)
        scro.grid(row=0,column=1,sticky='ns')
        
        
    def register(self):
        if (not isNumber(self.e_prec.get())) or (not self.e_prod.get().strip()) or (not self.e_prec.get().strip()) or (self.c_categ.get() == '<CATEGORIA>'):
            messagebox.showerror('Cadastrar','Dado(s) inserido(s) inválido(s)')
            return
        self.product = self.e_prod.get()
        self.price = double(self.e_prec.get())
        self.category = self.c_categ.get()
        id = geraProd(self.product)

        prod = Produto(id,self.product,self.price,self.category)
        rep = Repository()
        result = rep.cadastrar(prod)
        self.e_prod.delete(0,END)
        self.e_prec.delete(0,END)
        self.c_categ.current(0)
        if result:
            pd = "       " + self.product
            pc = "       R$ " + str(self.price)
            datas = (id,pd,pc)
            messagebox.showinfo("Cadastrar","Cadastro realizado com sucesso!")
            self.tree.insert('',END,values=datas)
        else:
            messagebox.showwarning("Cadastrar","Produto já cadastrado!")
        
    def close(self):
        if self.e_prod.get().strip() or self.e_prec.get().strip() or (self.c_categ.get() != '<CATEGORIA>'):
            self.register()
        self.quit()