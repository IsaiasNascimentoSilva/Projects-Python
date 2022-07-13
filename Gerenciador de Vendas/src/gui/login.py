from tkinter import messagebox
from gui.utilitarios.utilyt import*
from tkinter import*
from gui.repository import Repository
 

class Login(Tk):
    status = 0
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry('500x300')
        self.resizable(height='FALSE',width='FALSE')
        self.iconphoto(False,PhotoImage(file='imgs/icons8-locked-with-key-96.png'))

        # Parte de cima..............................................................
        f_cima = Frame(self, height=100,width=500, background=paleta(0))
        f_cima.grid(row=0,column=0)

        # Parte de  baixo............................................................
        f_baixo = Frame(self, height=200, width=500,background=paleta(6))
        f_baixo.grid(row=1,column=0)

        # Adicionando imagem.........................................................
        f_cima.img = PhotoImage(file='imgs/icons8-login-67.png')
        l_logo = Label(f_cima, image=f_cima.img, width=100, height=90,background=paleta(0))
        l_logo.place(x=200,y=15)

        # Credenciais................................................................
        l_usuario = Label(f_baixo, text='Usuário', background=paleta(6))
        l_usuario.place(x=15, y=30)

        self.e_usuario = Entry(f_baixo,width=40,justify='left',bg=paleta(7))
        self.e_usuario.place(x=80, y=30)

        l_pass = Label(f_baixo, text='Senha', background=paleta(6))
        l_pass.place(x=15, y=80)

        self.e_pass = Entry(f_baixo,width=20,justify='left',show='*',bg=paleta(7))
        self.e_pass.place(x=80, y=80)

        # Botões......................................................................
        b_ent = Button(f_baixo,text='Confirmar',bg=paleta(2),command=self.check)
        b_ent.place(x=110,y=150)

        b_exit = Button(f_baixo,text='Cancelar',bg=paleta(62),command=self.close)
        b_exit.place(x=250,y=150)
        
        
    def check(self):
        user = self.e_usuario.get()
        passw = self.e_pass.get()
        rep = Repository()
        result = rep.checkout(user,passw)
        if not result:
            messagebox.showerror("Login Erro", "Usuário ou Senha inválidos!")
            self.e_usuario.delete(0,END)
            self.e_pass.delete(0,END)
            return False
        
        messagebox.showinfo("Login sucesso","Bem vindo")
        self.close()
        self.status = 1
        return True

    def close(self):
        self.destroy()
        
