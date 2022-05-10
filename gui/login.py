from ..set.util import cor,cor3,cor5,cor6,cor7
from tkinter import*
 


tela_login = Tk()
tela_login.title("Login")
tela_login.geometry('500x300')
tela_login.resizable(height='FALSE',width='FALSE')
tela_login.iconphoto(False,PhotoImage(file='../imgs/icons8-locked-with-key-96.png'))

# Parte de cima..............................................................
f_cima = Frame(tela_login, height=100,width=500, background=cor)
f_cima.grid(row=0,column=0)

# Parte de  baixo............................................................
f_baixo = Frame(tela_login, height=200, width=500,background=cor6)
f_baixo.grid(row=1,column=0)

# Adicionando imagem.........................................................
img = PhotoImage(file='../imgs/icons8-login-67.png')
l_logo = Label(f_cima, image=img, width=100, height=90,background=cor)
l_logo.place(x=200,y=15)

# Credenciais................................................................
l_usuario = Label(f_baixo, text='Usuário', background=cor6)
l_usuario.place(x=15, y=30)

e_usuario = Entry(f_baixo,width=40,justify='left',bg=cor7)
e_usuario.place(x=80, y=30)

l_pass = Label(f_baixo, text='Senha', background=cor6)
l_pass.place(x=15, y=80)

e_pass = Entry(f_baixo,width=20,justify='left',show='*',bg=cor7)
e_pass.place(x=80, y=80)

# Botões......................................................................
b_ent = Button(f_baixo,text='Confirmar',bg=cor5)
b_ent.place(x=110,y=150)

b_exit = Button(f_baixo,text='Cancelar',bg=cor3)
b_exit.place(x=250,y=150)

tela_login.mainloop()