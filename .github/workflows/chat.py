import tkinter
from tkinter import ttk
import time
import funcoes_pyhton


#adicionei aqui

#make de root widget
root = tkinter.Tk()
root.geometry("350x630")
root.title("Chat")

#Make the notebook
nb = ttk.Notebook(root, height = 630, width = 350)
nb.grid(column = 0, row = 0)
    
arquivo1 = open('destinatario.txt', 'r')
cpf_d = arquivo1.readline()
arquivo1.close()
    
arquivo2 = open('usuario.txt', 'r')
cpf_r = arquivo2.readline()
arquivo2.close()
    
nome1,email1,cpf1 = funcoes_pyhton.armazenar_client(cpf_d)
nome2,email2,cpf2 = funcoes_pyhton.armazenar_client(cpf_r)
    
valor, intq, ordem = funcoes_pyhton.todas_mensagens(cpf_d,cpf_r)

def PrimeiraTab():   
    f1 = tkinter.Frame(nb)
    nb.add(f1,text=nome1)
    tkinter.LabelFrame(f1)
     
    u = 0
    for n in range(intq):
        a = n-1
        if a in ordem:
            usuario = "Eu"
        else:
            usuario = nome1      
        txt_usuario = tkinter.Label(f1,text = usuario+":")
        txt_usuario.place(x = 10, y = n*30)
        txt_descricao = tkinter.Label(f1,text = valor[n])
        txt_descricao.place(x = 60, y = n*30)
        u = u+30

    y2 = 40+u
    texto = tkinter.Entry(f1,width = 30)
    texto.place(x = 50, y = y2)
    btn1 = tkinter.Button(f1,text = "Conversar",height = 1, width = 8,command = lambda: enviar_e_atualizar(str(texto.get())))
    btn1.place(x = 50,y = y2+ 30)
    
def enviar_e_atualizar(mensagem):
    funcoes_pyhton.enviar_mensagem(cpf_r, cpf_d, mensagem)



PrimeiraTab()
nb.enable_traversal()
root.mainloop()