import os


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
    match os.path.exists("variaveis.txt"):

        case True:
            variaveis_carregadas = carregar_variaveis('variaveis.txt')
            if variaveis_carregadas != None:
                if len(variaveis_carregadas) > 0:
                    print(f"seja bem vindo novamente, seus dados são:\n Nome: {variaveis_carregadas['nome']} \n Numero de Telefone:{variaveis_carregadas['telefone']}\n Email: {variaveis_carregadas['email']}")
                else:
                    nome_v = input("por favor digite seu nome")
                    telefone_v = input("por favor digite seu numero de telefone")
                    email_v = input("por favor digite seu Email")

                    salvar_variaveis('variaveis.txt',nome = nome_v, telefone = telefone_v, email = email_v )
            else:
                nome_v = input("por favor digite seu nome")
                telefone_v = input("por favor digite seu numero de telefone")
                email_v = input("por favor digite seu Email")

                salvar_variaveis('variaveis.txt',nome = nome_v, telefone = telefone_v, email = email_v )
        case False:
                nome_v = input("por favor digite seu nome")
                telefone_v = input("por favor digite seu numero de telefone")
                email_v = input("por favor digite seu Email")

                salvar_variaveis('variaveis.txt',nome = nome_v, telefone = telefone_v, email = email_v )

verifica_primeira_vez()