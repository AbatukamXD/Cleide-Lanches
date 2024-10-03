import os
import time
import random
import webbrowser

print(" -----------------------------------\n Seja Bem vindo ao cardapio da Cleide Lanches! Aqui oferecemos as melhores soluções para a sua fome! 😋🍔\n--------------------------------\n Tudo feito de forma caseira pelo nosso chefe Carlinhos! 🐴👨‍🍳\n------------------------------------")



    # Salvar variáveis em um arquivo separado por nomes
def salvar_variaveis(path_file, **kwargs):
    with open(path_file, 'w') as f:
     for nome, valor in kwargs.items():
        f.write(f"{nome}: {valor}\n")

# Carregar variáveis de um arquivo
def carregar_variaveis(path_file):
    variaveis = {}
    with open(path_file, 'r') as f:
        for line in f:
            try:
                chave, valor = line.strip().split(': ')
                variaveis[chave] = valor
            except ValueError:
                return None 
    return variaveis

def verifica_primeira_vez():
    match os.path.exists("dados_pessoais.txt"):

        case True:
            
            variaveis_carregadas = carregar_variaveis('dados_pessoais.txt')
            if variaveis_carregadas != None:
                
                if len(variaveis_carregadas) > 0:
                    
                    print(f" Vejo que você ja tem registro, por acaso você é: {variaveis_carregadas['nome']}? ")
                    variaveis_carregadas = input("Digite: \n-------\n 1-Sim \n-------\n 2-Não\n-------> ")
                    
                    if variaveis_carregadas == "1":
                        
                        variaveis_carregadas = carregar_variaveis('dados_pessoais.txt')
                        
                    elif variaveis_carregadas == "2":
                        
                         print("\n Digite as informações a seguir para se cadastrar!🥳\n-----------------------") 
                         nome_v = input(" Digite seu Nome: ")
                         email_v = input("\n--------------------- Digite seu Email: ")
                         senha_v = input("\n------------------- Digite seu Senha: ")
                         
                         print("\nCadastro Concluido.")
                         

                         salvar_variaveis('dados_pessoais.txt',nome = nome_v)
                        
                else:
                    nao_cadastro = input("\n\n---------------------------\n Você não tem um cadastro 😱, deseja se cadastrar?🥺 \n---------------------\n 1-Sim!😊 \n--------\n 2-Não!🤬 \n--------> ")
                    if nao_cadastro == "1":
                        
                        print("\n Digite as informações a seguir para se cadastrar!🥳\n-----------------------") 
                        nome_v = input(" Digite seu Nome: ")
                        email_v = input("\n--------------------- Digite seu Email: ")
                        senha_v = input("\n------------------- Digite seu Senha: ")
                        
                        print("\nCadastro Concluido.")
                        
                        salvar_variaveis('dados_pessoais.txt',nome = nome_v, senha = senha_v, email = email_v )
                        
                    elif nao_cadastro == "2":
                        print("Entendido, programa finalizado!")
                        
                    else:
                        print("Digito Invalido, Programa finalizado.")
                        

            else:
                nao_cadastro = input("\n\n---------------------------\n Você não tem um cadastro 😱, deseja se cadastrar?🥺 \n---------------------\n 1-Sim!😊 \n--------\n 2-Não!🤬 \n--------> ")
                if nao_cadastro == "1":
                    
                    print("\n Digite as informações a seguir para se cadastrar!🥳\n-----------------------")    
                    nome_v = input(" Digite seu Nome: ")
                    email_v = input("\n--------------------- Digite seu Email: ")
                    senha_v = input("\n------------------- Digite seu Senha: ")
                    
                    print("\nCadastro Concluido.")
                    
                    salvar_variaveis('dados_pessoais.txt',nome = nome_v, senha = senha_v, email = email_v )
                    
                elif nao_cadastro == "2":
                    print("Entendido, programa finalizado!")
                else:
                    print("Digito Invalido, Programa finalizado.")
                    
        case False:
                nao_cadastro = input("\n\n---------------------------\n Você não tem um cadastro 😱, deseja se cadastrar?🥺 \n---------------------\n 1-Sim!😊 \n--------\n 2-Não!🤬 \n--------> ")
                if nao_cadastro == "1":
                    print("\n Digite as informações a seguir para se cadastrar!🥳\n-----------------------") 
                    nome_v = input(" Digite seu Nome: ")
                    email_v = input("\n--------------------- Digite seu Email: ")
                    senha_v = input("\n------------------- Digite seu Senha: ")
                    
                    print("\nCadastro Concluido.")

                    salvar_variaveis('dados_pessoais.txt',nome = nome_v, senha = senha_v, email = email_v )   
                     
                elif nao_cadastro == "2":
                    print("Entendido, programa finalizado!")
                    
                else:
                    print("Digito Invalido, Programa finalizado.")

verifica_primeira_vez()

