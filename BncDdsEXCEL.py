#Importação de bibliotecas
import sqlite3 as sq
import tkinter as tk
import pandas as pd


#Criação - Banco de Dados
dataBase = sq.connect('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/BancoDados/bancoClientes.db')
db = dataBase.cursor()
db.execute("CREATE TABLE IF NOT EXISTS clientes(Nome text, Sobrenome text, Email text, Telefone text)")
dataBase.commit()
dataBase.close()


#Criação - Cadastro clientes
def cadastro():
    dataBase = sq.connect('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/BancoDados/bancoClientes.db')
    db = dataBase.cursor()
    db.execute("INSERT INTO clientes VALUES(:Nome, :Sobrenome, :Email, :Telefone)", 
               {
                   'Nome':entry_Nome.get(),
                   'Sobrenome':entry_Sobrenome.get(),
                   'Email':entry_Email.get(),
                   'Telefone':entry_Telefone.get()
               })


#Deleção de nomes do campo após nomes inseridos
    entry_Nome.delete(0, 'end') #deletar do primeiro caractere ate o final
    entry_Sobrenome.delete(0, 'end')
    entry_Email.delete(0, 'end')
    entry_Telefone.delete(0, 'end')

    dataBase.commit()
    dataBase.close()


#Exportar clientes para o Excel
def exportar():
    dataBase = sq.connect('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/BancoDados/bancoClientes.db')
    db = dataBase.cursor()
    db.execute("SELECT *, oid FROM clientes")
    clientesCadastrados = db.fetchall()
    clientesCadastrados = pd.DataFrame(clientesCadastrados, columns = ['Nome', 'Sobrenome', 'Email', 'Telefone', 'ID'])
    clientesCadastrados.to_excel('BancoClientes.xlsx')
    
    print(clientesCadastrados)
    dataBase.commit()
    dataBase.close()


#Criar título da janela
janela = tk.Tk()
janela.title('Ferramenta de Cadastro de Clientes')


#Criar lables (etiqueta antes da entrada de dados)
lableNome = tk.Label(janela, text = 'Nome', width = 30)
lableNome.grid(row = 0, column = 0, padx = 10, pady = 10)

lableSobrenome = tk.Label(janela, text = 'Sobrenome', width = 30)
lableSobrenome.grid(row = 1, column = 0, padx = 10, pady = 10)

lableEmail = tk.Label(janela, text = 'Email', width = 30)
lableEmail.grid(row = 2, column = 0, padx = 10, pady = 10)

lableTelefone = tk.Label(janela, text = 'Telefone', width = 30)
lableTelefone.grid(row = 3, column = 0, padx = 10, pady = 10)


#Criar widgets - Entrada de Dados (textbox)
entry_Nome = tk.Entry(janela, text = 'Nome', width = 30)
entry_Nome.grid(row = 0, column = 1, padx = 10, pady = 10)

entry_Sobrenome = tk.Entry(janela, text = 'Sobrenome', width = 30)
entry_Sobrenome.grid(row = 1, column = 1, padx = 10, pady = 10)

entry_Email = tk.Entry(janela, text = 'Email', width = 30)
entry_Email.grid(row = 2, column = 1, padx = 10, pady = 10)

entry_Telefone = tk.Entry(janela, text = 'Telefone', width = 30)
entry_Telefone.grid(row = 3, column = 1, padx = 10, pady = 10)



#Criar botões - Cadastrar e Exportar
botaoCadastro = tk.Button(janela, text = 'Cadastrar Cliente', command = cadastro)
botaoCadastro.grid(row = 4, column = 0, padx = 0, pady = 0, columnspan = 2, ipadx = 80)

botaoExportar = tk.Button(janela, text = 'Exportar para Excel', command = exportar)
botaoExportar.grid(row = 5, column = 0, padx = 0, pady = 0, columnspan = 2, ipadx = 80)


janela.mainloop()