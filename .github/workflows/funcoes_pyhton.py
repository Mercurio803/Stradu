#basicao
import pyrebase

config = {
    "apiKey": "AIzaSyAmFzJSSNnvJ00W8u8Xm_zBrabYuqkpkr8",
    "authDomain": "straduo-bf4c4.firebaseapp.com",
    "databaseURL": "https://straduo-bf4c4.firebaseio.com",
    "projectId": "straduo-bf4c4",
    "storageBucket": "straduo-bf4c4.appspot.com",
    "messagingSenderId": "959052971762",
    "appId": "1:959052971762:web:bf4e037f58a9cc933c1a6b"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

user = auth.sign_in_with_email_and_password("cachorro@gmail.com","jacare")

db = firebase.database()


#Funcoes que recebe valores de nome, email, cpf,senha e cadastra no firebase
#coloquei 3 linha de criacao de arquivo 3X
def cadastrar_caminhoneiro_dono(nome, email, cpf, senha):
    caminhoneiro = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "cpf": cpf
    }
    arquivo = open('usuario.txt', 'w')
    arquivo.write(cpf)
    arquivo.close()
    results = db.child("caminhoneiros_dono").child(caminhoneiro['cpf']).set(caminhoneiro, user['idToken'])
    
def cadastrar_caminhoneiro_amigo(nome, email, cpf, senha):
    caminhoneiro = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "cpf": cpf
    }
    arquivo = open('usuario.txt', 'w')
    arquivo.write(cpf)
    arquivo.close()
    results = db.child("caminhoneiros_amigo").child(caminhoneiro['cpf']).set(caminhoneiro, user['idToken'])

#funcao de login
def login(cpf, senha):
    data1 = db.child("caminhoneiros_amigo/"+cpf+"/senha").get(user['idToken'])
    data2 = db.child("caminhoneiros_dono/"+cpf+"/senha").get(user['idToken'])
        
    if(str(data1.val()) == senha):
        data = db.child("caminhoneiros_amigo/"+cpf+"/nome").get(user['idToken'])
        arquivo = open('usuario.txt', 'w')
        arquivo.write(cpf)
        arquivo.close()
        import amigo       

    elif(str(data2.val()) == senha):
        data = db.child("caminhoneiros_dono/"+cpf+"/nome").get(user['idToken'])
        arquivo = open('usuario.txt', 'w')
        arquivo.write(cpf)
        arquivo.close()
        import autonomo      
    else:
        pass
    
def armazenar_client(cpf):
    if (str(db.child("caminhoneiros_amigo/"+cpf+"/cpf").get(user['idToken']).val()) == cpf):
        email = str(db.child("caminhoneiros_amigo/"+cpf+"/email").get(user['idToken']).val())
        nome = str(db.child("caminhoneiros_amigo/"+cpf+"/nome").get(user['idToken']).val())
    
    else:
        email = str(db.child("caminhoneiros_dono/"+cpf+"/email").get(user['idToken']).val())
        nome = str(db.child("caminhoneiros_dono/"+cpf+"/nome").get(user['idToken']).val())

    return (nome,email,cpf)    
          
#funcao publicar proposta
def publicar_proposta(descricao, valor_total, valor_proposto, cidade_partida, cidade_destino):
    #pegando o cpf do arquivo
    arquivo = open('usuario.txt', 'r')
    cpf = arquivo.readline()
    arquivo.close()
    #------
    qtd = int(str(db.child("qtd_propostas").get(user['idToken']).val()))
    qtd = qtd + 1;
    db.child("qtd_propostas").set(qtd, user['idToken'])
    proposta = {
        "descricao":descricao,
        "valor_total": valor_total,
        "valor_proposto": valor_proposto,
        "cidade_partida": cidade_partida,
        "cidade_destino": cidade_destino,
        "cpf_autor": cpf,
        "qtd_propostas": qtd
    }


    results = db.child("propostas/"+str(qtd)).set(proposta, user['idToken'])

#ver_propostas
def ver_propostas_disponiveis():
    qtd = int(str(db.child("qtd_propostas").get(user['idToken']).val()))
    results_cpf = {}
    results_descricao = {}
    for i in range(qtd):
        results_cpf[i] = str(db.child("propostas/"+str(i+1)+"/cpf_autor").get(user['idToken']).val())
        
    for j in range(qtd):
        results_descricao[j] = str(db.child("propostas/"+str(j+1)+"/descricao").get(user['idToken']).val())
        
    return qtd,results_cpf,results_descricao
    
#funcao_enviar_mensagem
def enviar_mensagem(cpf_remetente, cpf_destinatario, mensagem):
    qtd1 = str(db.child("mensagens/"+cpf_remetente+"/"+cpf_destinatario+"/qtd_mensagens").get(user['idToken']).val())
    qtd2 = str(db.child("mensagens/"+cpf_destinatario+"/"+cpf_remetente+"/qtd_mensagens").get(user['idToken']).val())

    if(qtd1.isdigit() == False):
        qtd1 = "0"

    if(qtd2.isdigit() == False):
        qtd2 = "0"

    if(qtd1.isdigit() or qtd2.isdigit()):
        int_qtd = int(qtd1) + int(qtd2)
        int_qtd = int_qtd+1
        db.child("mensagens/"+cpf_remetente+"/"+cpf_destinatario+"/qtd_mensagens").set(int(qtd1)+1, user['idToken'])
        db.child("mensagens/"+cpf_remetente+"/"+cpf_destinatario+"/"+str(int_qtd)).set(mensagem, user['idToken'])
        
    else:
        int_qtd = 1
        db.child("mensagens/"+cpf_remetente+"/"+cpf_destinatario+"/qtd_mensagens").set(int_qtd, user['idToken'])
        db.child("mensagens/"+cpf_remetente+"/"+cpf_destinatario+"/"+str(int_qtd)).set(mensagem, user['idToken'])

def todas_mensagens(cpf1,cpf2):
    qtd1 = str(db.child("mensagens/"+cpf1+"/"+cpf2+"/qtd_mensagens").get(user['idToken']).val())
    qtd2 = str(db.child("mensagens/"+cpf2+"/"+cpf1+"/qtd_mensagens").get(user['idToken']).val())
    result = {}
    ordem = []
    if(qtd1.isdigit() == False):
        qtd1 = "0"

    if(qtd2.isdigit() == False):
        qtd2 = "0"
        
    int_qtd = int(qtd1) + int(qtd2)
        
    for i in range(int_qtd):
        a = i+1
        m = str(db.child("mensagens/"+cpf1+"/"+cpf2+"/"+str(a)).get(user['idToken']).val())
        n = str(db.child("mensagens/"+cpf2+"/"+cpf1+"/"+str(a)).get(user['idToken']).val())
        if(m != "None"):
            ordem.append(i);
            result[i] = m
        if(n != "None"):
            result[i] = n
            print(ordem)
    return result,int_qtd,ordem

def retornar_todos_cpf_cadastrados():
    all_cpfs_amigo = db.child("caminhoneiros_amigo").get(user['idToken'])
    all_cpfs_autonomo = db.child("caminhoneiros_dono").get(user['idToken'])
    result =[]
    for cpfam in all_cpfs_amigo.each():
        lista1 = cpfam.val()
        result.append(lista1['cpf'])
    for cpfau in all_cpfs_autonomo.each():
        lista2 = cpfau.val()
        result.append(lista2['cpf'])
    return result

def monstrar_contatos_em_conversa(cpf):
    testar = retornar_todos_cpf_cadastrados()
    result = []
    for icpf in testar:
        cmd = str(db.child("mensagens/"+icpf+"/"+str(cpf)+"/qtd_mensagens").get(user['idToken']).val())
        if(cmd != "None"):
            result.append(icpf)
    return result
    

    

