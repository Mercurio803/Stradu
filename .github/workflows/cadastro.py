import tkinter
from tkinter import ttk
import funcoes_pyhton
import time

root = tkinter.Tk()
root.geometry("350x630")
root.title("Amigo Caminhoneiro")


nb = ttk.Notebook(root, height = 630, width = 350)
nb.grid(column = 0, row = 0)



def PrimeiraTab_cadastro():
    f1 = tkinter.Frame(nb)
    nb.add(f1,text="Login")

    txt_cpf = tkinter.Label(f1,text = "CPF:")
    txt_cpf.place(x = 50, y = 40)
    cpf = tkinter.Entry(f1,width = 30)
    cpf.place(x = 50, y = 60)

    txt_senha = tkinter.Label(f1,text = "Senha:")
    txt_senha.place(x = 50, y = 100)
    senha = tkinter.Entry(f1,width = 30, show="*")
    senha.place(x = 50, y = 120)

    btn1 = tkinter.Button(f1,text = "Entrar",height = 1, width = 8,command = lambda: MoveTo(str(cpf.get()),str(senha.get())))
    btn1.place(x = 120,y = 160)

    def MoveTo(cpf,senha):
        funcoes_pyhton.login(cpf,senha)



def SegundaTab_cadastro():

    f2 = tkinter.Frame(nb)
    nb.add(f2,text="Cadastro")

    txt_nome = tkinter.Label(f2,text = "Nome:")
    txt_nome.place(x = 13, y = 15)
    nome = tkinter.Entry(f2,width = 30)
    nome.place(x = 13, y = 40)


    txt_email = tkinter.Label(f2,text = "Email:")
    txt_email.place(x = 13, y = 70)
    email = tkinter.Entry(f2,width = 30)
    email.place(x = 13, y = 95)

    txt_telefone = tkinter.Label(f2,text = "Telefone Celular:")
    txt_telefone.place(x = 13, y = 125)
    telefone = tkinter.Entry(f2,width = 30)
    telefone.place(x = 13, y = 155)

    txt_cpf = tkinter.Label(f2,text = "CPF:")
    txt_cpf.place(x = 13, y = 180)
    cpf = tkinter.Entry(f2,width = 30)
    cpf.place(x = 13, y = 205)

    txt_senha = tkinter.Label(f2,text = "Senha:")
    txt_senha.place(x = 13, y =235)
    senha = tkinter.Entry(f2,width = 30, show="*")
    senha.place(x = 13, y = 260)


    btn1 = tkinter.Button(f2,text = "Autônomo",height = 2, width = 10,command = lambda: MoveToAutonomo(str(nome.get()),str(email.get()),str(cpf.get()),str(senha.get())))
    btn1.place(x = 13,y = 300)

    btn2 = tkinter.Button(f2,text = "Amigo", height = 2 , width = 10, command = lambda: MoveToAmigo(str(nome.get()),str(email.get()),str(cpf.get()),str(senha.get())))
    btn2.place(x = 100 , y = 300)

    def MoveToAutonomo(nome,email,cpf,senha):
        funcoes_pyhton.cadastrar_caminhoneiro_dono(nome,email,cpf,senha)
        time.sleep(3)
        import autonomo    


    
    def MoveToAmigo(nome,email,cpf,senha):
        funcoes_pyhton.cadastrar_caminhoneiro_amigo(nome,email,cpf,senha)
        time.sleep(3)
        import amigo

    return cpf.get()


PrimeiraTab_cadastro()
SegundaTab_cadastro()
root.mainloop()