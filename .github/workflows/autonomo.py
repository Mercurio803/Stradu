import tkinter
from tkinter import ttk
import pandas as pd
import numpy as np
import funcoes_pyhton


'''df = pd.read_json("estados-cidades.json")
df.to_excel("teste.xlsx")'''

#make de root widget
root = tkinter.Tk()
root.geometry("350x630")
root.title("Caminhoneiro Autonomo")

#Make the notebook
nb = ttk.Notebook(root, height = 630, width = 350)
nb.grid(column = 0, row = 0)


def PrimeiraTab():
    f1 = tkinter.Frame(nb)
    nb.add(f1,text="Criar proposta")
    tkinter.LabelFrame(f1)

    valor_total_txt = tkinter.Label(f1,text = "Valor total")
    valor_total_txt.place(x = 13 , y = 35)
    valor_total = tkinter.Entry(f1,width = 30)
    valor_total.place(x = 13 , y = 60)

    descricao_txt = tkinter.Label(f1,text = "Descrição")
    descricao_txt.place(x = 13, y = 100)
    descricao = tkinter.Entry(f1,width = 30)
    descricao.place(x = 13 , y = 125)

    valor_ofertado_txt = tkinter.Label(f1,text = "Valor ofertado")
    valor_ofertado_txt.place(x = 13 , y = 165)
    valor_ofertado = tkinter.Entry(f1,width = 30)
    valor_ofertado.place(x = 13 , y = 190)

    cidade_saida_txt = tkinter.Label(f1,text = "Cidade de partida:")
    cidade_saida_txt.place(x = 10, y = 250)
    cidade_saida = tkinter.Entry(f1,width = 20)
    cidade_saida.place(x = 10 , y = 280)


    cidade_chegada = tkinter.Label(f1,text = "Cidade de chegada:")
    cidade_chegada.place(x = 190, y = 250)
    cidade_chegada = tkinter.Entry(f1,width = 20)
    cidade_chegada.place(x = 190, y = 280)

    btn1 = tkinter.Button(f1, text = "Criar Proposta", height = 1, width = 13, command =  lambda: MoveTo(str(descricao.get()),str(valor_total.get()),str(valor_ofertado.get()),str(cidade_saida.get()),str(cidade_chegada.get()),cpf = "123123123"))
    btn1.place(x = 110 , y = 320)

    nb.select(f1)


    def MoveTo(descricao, valor_total, valor_proposto, cidade_partida, cidade_destino, cpf):
        funcoes_pyhton.publicar_proposta(descricao, valor_total, valor_proposto, cidade_partida, cidade_destino)
        


def SegundaTab():
    f2 = tkinter.Frame(nb)
    nb.add(f2,text="Propostas Criadas")
    return


def TerceiraTab():
    f3 = tkinter.Frame(nb)
    nb.add(f3,text="Usuarios")
    arquivo = open('usuario.txt', 'r')
    cpf2 = arquivo.readline()
    arquivo.close()
    result = funcoes_pyhton.monstrar_contatos_em_conversa(cpf2)
    i = 1
    for n in result:
        nome,email,cpf = funcoes_pyhton.armazenar_client(n)
        y1 = 40+i*70
        i = i+1
        txt_usuario = tkinter.Label(f3,text = "Usuario:" +nome)
        txt_usuario.place(x = 50, y = y1)
        btn1 = tkinter.Button(f3,text = "Conversar",height = 1, width = 8,command = lambda: conversar(cpf))
        btn1.place(x = 200,y = y1)
    return
def conversar(cpf_remetente):
   arquivo = open('destinatario.txt', 'w')
   arquivo.write(cpf_remetente)
   arquivo.close()
   import chat


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