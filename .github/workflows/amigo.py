import tkinter
from tkinter import ttk
import time
import funcoes_pyhton
#adicionei aqui

#make de root widget
root = tkinter.Tk()
root.geometry("350x630")
root.title("Caminhoneiro Amigo")

#Make the notebook
nb = ttk.Notebook(root, height = 630, width = 350)
nb.grid(column = 0, row = 0)


def PrimeiraTab():
    f1 = tkinter.Frame(nb)
    nb.add(f1,text="Viagens Realizadas")
    tkinter.LabelFrame(f1)
    return


def SegundaTab():
    f2 = tkinter.Frame(nb)
    nb.add(f2,text="Ver propostas")
    
    qtd,results_cpf,results_descricao = funcoes_pyhton.ver_propostas_disponiveis()
    for n in range(qtd):
        nome,email,cpf = funcoes_pyhton.armazenar_client(results_cpf[n])
        y1 = 40+70*n
        txt_usuario = tkinter.Label(f2,text = "Usuario:" + nome)
        txt_usuario.place(x = 50, y = y1)
        txt_descricao = tkinter.Label(f2,text = "DESCRICAO:" + results_descricao[n])
        txt_descricao.place(x = 50, y = y1+20)
        btn1 = tkinter.Button(f2,text = "Conversar",height = 1, width = 8,command = lambda: conversar(cpf))
        btn1.place(x = 50,y = y1+ 40)
    return
def conversar(cpf_remetente):
   arquivo = open('destinatario.txt', 'w')
   arquivo.write(cpf_remetente)
   arquivo.close()
   import chat


def TerceiraTab():
    f3 = tkinter.Frame(nb)
    nb.add(f3,text="Home Page")
    return


def QuartaTab():
    f4 = tkinter.Frame(nb)
    nb.add(f4,text="Home Page")
    return

PrimeiraTab()
SegundaTab()
TerceiraTab()
QuartaTab()
nb.enable_traversal()
root.mainloop()