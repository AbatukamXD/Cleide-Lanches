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



valor_total_pedido = 0
lista_carrinho = []

def cardapio():
    while True:
        print("Este é o nosso cardápio! Aproveite! 😜")
        print ("-"*20)
        print("[1] Salgados 🥐\n[2] Hamburger 🍔\n[3] Bebidas 🥤\n[4] Fechar 👋")
        entrada = input("Selecione uma das nossas opções: ")

        match entrada:
            case "1":
                salgados()
            case "2":
                burger()
            case "3":
                bebidas()
            case "4":
                print("\nAgradecemos a sua visita! \nEsperamos por você na próxima 😁")
                return
            case _:
                print("A Cleide Lanches não entendeu. Tente novamente!")
                print ("-"*20)
''''
        if confirmar_pedido(lista_carrinho):
            total = calcular_total(lista_carrinho)
            print(f"Seu pedido foi confirmado e o valor total ficou de: R$ {total:.2f}")
            lista_carrinho.clear()
'''

def calcular_total(carrinho):
    return sum(item["valor"] for item in carrinho)

def perguntar_se_deseja_continuar():
    while True:
        opcao = input("Deseja pedir mais alguma coisa? [SIM] ou [NÃO]: ")
        match opcao:
            case "SIM":
                return cardapio()
            case "NÃO":
                print ("-"*20)
                return False
            case _:
                print("Opção inválida. Tente novamente.")

def salgados():
    print("\nÓtima escolha!")
    print("[1] Pastel\n[2] Risólis\n[3] Enroladinho")
    entrada = input("Selecione uma das nossas opções: ")

    match entrada:
        case "1":
            pastel()
        case "2":
            risolis()
        case "3":
            lista_carrinho.append({"nome": "Enroladinho", "valor": 2.00})
            print("Você escolheu Enroladinho.")
        case _:
            print("Opção inválida.")
            salgados()


def pastel():
    print("\nOpções de Pastel: ")
    entrada = input("[1] Carne 🥩\n[2] Frango 🍗\n[3] Queijo 🧀  ")

    match entrada:
        case "1":
            lista_carrinho.append({"nome": "Pastel de Carne", "valor": 5.00})
            print("Você escolheu Pastel de Carne.")
        case "2":
            lista_carrinho.append({"nome": "Pastel de Frango", "valor": 5.00})
            print("Você escolheu Pastel de Frango.")
        case "3":
            lista_carrinho.append({"nome": "Pastel de Queijo", "valor": 5.00})
            print("Você escolheu Pastel de Queijo.")
        case _:
            print("Opção inválida.")

    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def risolis():
    print("\nOpções de Risólis: ") 
    entrada = input("[1] Carne 🥩\n[2] Frango 🍗  ")

    match entrada:
        case "1":
            lista_carrinho.append({"nome": "Risólis de Carne", "valor": 4.00})
            print("Você escolheu Risólis de Carne.")
        case "2":
            lista_carrinho.append({"nome": "Risólis de Frango", "valor": 4.00})
            print("Você escolheu Risólis de Frango.")
        case _:
            print("Opção inválida.")

    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def burger():
    print("\nOpções de Hamburger: ")
    entrada = input("[1] Super Cleide 😱\n[2] Big Cleide 😎\n[3] Veg Cleide 🥗 ")

    match entrada:
        case "1":
            lista_carrinho.append({"nome": "Super Cleide", "valor": 23.00})
            print("Você escolheu Super Cleide.")
        case "2":
            lista_carrinho.append({"nome": "Big Cleide", "valor": 18.00})
            print("Você escolheu Big Cleide.")
        case "3":
            lista_carrinho.append({"nome": "Veg Cleide", "valor": 20.00})
            print("Você escolheu Veg Cleide.")
        case _:
            print("Opção inválida.")

    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def bebidas():
    print("\nOpções de Bebidas: ")
    print("[1] Pepsi\n[2] Fanta\n[3] Guaraná\n[4] Sprite\n[5] Tap Water")
    entrada = input("Escolha uma bebida: ")

    match entrada:
        case "1" | "2" | "3" | "4":
            lista_carrinho.append({"nome": "Refrigerante", "valor": 5.00})
            print("Você escolheu Refrigerante Lata. 🥃")
        case "5":
            lista_carrinho.append({"nome": "Água", "valor": 3.00})
            print("Você escolheu Tap Water. 🧊")
        case _:
            print("Opção inválida.")

    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def confirmar_pedido(lista_carrinho):
    if lista_carrinho:
        print("Você escolheu:")
        for item in lista_carrinho:
            print(f"- {item['nome']} (R$ {item['valor']:.2f})")
        total = calcular_total(lista_carrinho)
        print(f"Total do pedido: R$ {total:.2f}")
    else:
        print("Você não fez nenhum pedido.")
        return False

    confirmar = input("Deseja confirmar o pedido? [SIM] ou [NÃO]: ")
    return confirmar == "SIM"

cardapio()
verifica_primeira_vez()