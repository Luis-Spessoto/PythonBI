#Projeto Agenda - SQL + Python

import sqlite3 as sq
import time 

conectar = sq.connect('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/BancoDados/agenda.db') #.db = database
c = conectar.cursor()

def criarDB():
    c.execute("CREATE TABLE IF NOT EXISTS cadastro (Nome TEXT, Telefone VARCHAR, Email TEXT, Data TEXT)") #varchar = str grande que pode contar letras, numeros e ou simbolos

try: #serve para testar o codigo quando se pensa que esse pode ser suscetivel a erros
    criarDB()
except:
    print("Erro ao criar DataBase")
else:
    print("DataBase atualizada com sucesso")

def inserirDados(n, t, e): #nome telefone email
    d = time.strftime('%d/%m/%y') #para importar data do pc d = day, m = month, y = year
    c.execute("INSERT INTO cadastro VALUES(?, ?, ?, ?)", (n, t, e, d))
    conectar.commit()

def pesquisaDados(p):
    sql = 'SELECT * FROM cadastro WHERE Nome = ? or Telefone = ? or Email = ?'
    resultadoPESQUISA = c.execute(sql, (p, p, p )).fetchall() #isso aqui recupera todas as informacoes da database para poder fazer a verificacao (thx to CHATGPT)
    if resultadoPESQUISA: #se o resultadoPesquisa trouxer alguma informacao
        for row in resultadoPESQUISA: #p, indica um tupla quando se tem , apos (nesse caso sao 3 p, pois se refere a nome, telefone e email)
            print(row) #row seria a linha da tabela
    else:
        print("\nInformações não constam em nossa DataBase\n")
    conectar.commit()


op = int(input('1 - Cadastrar \n2 - Pesquisar \n3 - Atualizar informações \n4 - Sair \nSelecione uma opção: '))

#cadastro
while op != 4:
    if op == 1:
        try:
            print('Cadastro de Agenda')
            time.sleep(2)
            n = str(input('Informe seu nome: '))
            t = str(input('Informe seu telefone: '))
            e = str(input('Informe seu email: '))
            inserirDados(n, t, e)
        except: 
            print("Erro ao efetuar cadastro!")
        else:
            print("Cadastro realizado com sucesso!") 

    #pesquisa = verificacao do banco de dados 
    elif op == 2:
        op2 = str(input('Você quer pesquisar pelo [NOME ou TELEFONE ou EMAIL]: ')).upper()
        if op2 == 'NOME':
            p = str(input('Informe o nome para consulta: '))
            time.sleep(1)
            print("Aguarde um momento...")
            time.sleep(2)
            print("Resultado da pesquisa: ")
            pesquisaDados(p)
        elif op2 == 'TELEFONE':
            p = str(input('Informe o telefone para consulta: '))
            time.sleep(1)
            print("Aguarde um momento...")
            time.sleep(2)
            print("Resultado da pesquisa: ")
            pesquisaDados(p)
        elif op2 == 'EMAIL':
            p = str(input('Informe o email para consulta: '))
            time.sleep(1)
            print("Aguarde um momento...")
            time.sleep(2)
            print("Resultado da pesquisa: ")
            pesquisaDados(p)

    #atualizar cadastro     
    elif op == 3:
        oldPERSON = str(input("Digite o nome da pessoa que você gostaria de fazer algum tipo de atualização: "))
        op3 = str(input('Qual informação você gostaria de atualizar? [NOME ou TELEFONE ou EMAIL]: ')).upper()
        if op3 == 'NOME':
            nomeNEW = str(input('Informe o novo nome: '))
            c.execute("UPDATE cadastro SET Nome = '{}' WHERE Nome = '{}'".format(nomeNEW, oldPERSON)) #ou c.execute("UPDATE cadastro SET Nome = ? WHERE Nome = ?", (nomeNEW, oldPERSON)) 
            conectar.commit()
        elif op3 == 'TELEFONE':
            telNEW = str(input('Informe o novo telefone: '))
            c.execute("UPDATE cadastro SET Telefone = '{}' WHERE Nome = '{}'".format(telNEW, oldPERSON))
            conectar.commit()
        elif op3 == 'EMAIL':
            emailNEW = str(input('Informe o novo email: ')) 
            c.execute("UPDATE cadastro SET Email = '{}' WHERE Nome = '{}'".format(emailNEW, oldPERSON))
            conectar.commit()           

    #encerrar aplicacao
    elif op == 4:
        break

    #verificacao se opcao for invalida para informar novamente
    else:
        while op != 1 and op != 2 and op != 3 and op != 4:
            op = int(input('Opção Inválida! Tente novamente: '))
    op = int(input('1 - Cadastrar \n2 - Pesquisar \n3 - Atualizar informações \n4 - Sair \nSelecione uma opção: '))

conectar.close() #fecha o banco de dados 