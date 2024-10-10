import os
import time
import random
import webbrowser
import signal

def salvar_variaveis(path_file, **kwargs):
    with open(path_file, 'w') as f:
        for nome, valor in kwargs.items():
            f.write(f"{nome}: {valor}\n")

def carregar_variaveis(path_file):
    variaveis = {}
    try:
        with open(path_file, 'r') as f:
            for line in f:
                chave, valor = line.strip().split(': ')
                variaveis[chave] = valor
    except FileNotFoundError:
        return None
    return variaveis

def verifica_primeira_vez():
    if os.path.exists("dados_pessoais.txt"):
        variaveis_carregadas = carregar_variaveis('dados_pessoais.txt')
        if variaveis_carregadas:
            nome = variaveis_carregadas.get('nome', 'desconhecido')
            print(f"Vejo que você já tem registro, por acaso você é: {nome}?")
            resposta = input("Digite: \n1 - Sim\n2 - Não\n-------> ")
            if resposta == "2":
                cadastrar_usuario()
        else:
            cadastrar_usuario()
    else:
        cadastrar_usuario()

def cadastrar_usuario():
    print("\nDigite as informações a seguir para se cadastrar!🥳")
    nome_v = input("Digite seu Nome: ")
    email_v = input("Digite seu Email: ")
    senha_v = input("Digite sua Senha: ")
    print("Cadastro Concluído.")
    salvar_variaveis('dados_pessoais.txt', nome=nome_v, senha=senha_v, email=email_v)

def calcular_total(carrinho):
    return sum(item["valor"] for item in carrinho)

def perguntar_se_deseja_continuar():
    while True:
        opcao = input("Deseja pedir mais alguma coisa? [SIM] ou [NÃO]: ").strip().upper()
        match opcao:
            case "SIM":
                return True
            case "NÃO":
                return False
            case _:
                print("Opção inválida. Tente novamente.")


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

    confirmar = input("Deseja confirmar o pedido? [SIM] ou [NÃO]: ").strip().upper()
    match confirmar:
        case "SIM":
            return True
        case "NÃO":
            return False
        case _:
            print("Opção inválida.")
            return False


def cardapio():
    lista_carrinho = []
    while True:
        print("Este é o nosso cardápio! Aproveite! 😜")
        print("-" * 20)
        print("[1] Salgados 🥐\n[2] Hamburger 🍔\n[3] Bebidas 🥤\n[4] Fechar 👋")
        entrada = input("Selecione uma das nossas opções: ")

        match entrada:
            case "1":
                lista_carrinho += salgados()
            case "2":
                lista_carrinho += burger()
            case "3":
                lista_carrinho += bebidas()
            case "4":
                print("\nAgradecemos a sua visita! \nEsperamos por você na próxima 😁")
                pid = os.getpid()
                os.kill(pid, signal.SIGTERM)
            case _:
                print("A Cleide Lanches não entendeu. Tente novamente!")

        if confirmar_pedido(lista_carrinho):
            total = calcular_total(lista_carrinho)
            print(f"Seu pedido foi confirmado e o valor total ficou de: R$ {total:.2f}")
            break  # Sai do loop do cardápio


def salgados():
    lista = []
    print("\nÓtima escolha!")
    print("[1] Pastel\n[2] Risólis\n[3] Enroladinho")
    entrada = input("Selecione uma das nossas opções: ")
    if entrada == "1":
        lista.append(pastel())
    elif entrada == "2":
        lista.append(risolis())
    elif entrada == "3":
        lista.append({"nome": "Enroladinho", "valor": 2.00})
        print("Você escolheu Enroladinho.")
    else:
        print("Opção inválida.")

    if not perguntar_se_deseja_continuar():
        return lista
    return []

def pastel():
    entrada = input("Opções de Pastel: \n[1] Carne 🥩\n[2] Frango 🍗\n[3] Queijo 🧀\nEscolha: ")
    if entrada == "1":
        return {"nome": "Pastel de Carne", "valor": 5.00}
    elif entrada == "2":
        return {"nome": "Pastel de Frango", "valor": 5.00}
    elif entrada == "3":
        return {"nome": "Pastel de Queijo", "valor": 5.00}
    else:
        print("Opção inválida.")
        return {}

def risolis():
    entrada = input("Opções de Risólis: \n[1] Carne 🥩\n[2] Frango 🍗\nEscolha: ")
    if entrada == "1":
        return {"nome": "Risólis de Carne", "valor": 4.00}
    elif entrada == "2":
        return {"nome": "Risólis de Frango", "valor": 4.00}
    else:
        print("Opção inválida.")
        return {}

def burger():
    entrada = input("Opções de Hamburger: \n[1] Super Cleide 😱\n[2] Big Cleide 😎\n[3] Veg Cleide 🥗\nEscolha: ")

    match entrada:
        case "1":
            return [{"nome": "Super Cleide", "valor": 23.00}]
        case "2":
            return [{"nome": "Big Cleide", "valor": 18.00}]
        case "3":
            return [{"nome": "Veg Cleide", "valor": 20.00}]
        case _:
            print("Opção inválida.")
            return []


def bebidas():
    print("\nOpções de Bebidas: ")
    print("[1] Pepsi \n[2] Fanta\n[3] Guaraná\n[4] Sprite\n[5] Tap Water")
    entrada = input("Escolha uma bebida: ")

    if entrada in ['1', '2', '3', '4']:
        return [{"nome": "Refrigerante 🥃", "valor": 5.00}]
    elif entrada == "5":
        return [{"nome": "Tap Water 🧊", "valor": 3.00}]
    else:
        print("Opção inválida.")
        return []

def main():
    verifica_primeira_vez()
    cardapio()

    metodo_de_pagamento = int(input("\nQual método de pagamento você deseja?\n1 - Pix\n2 - Dinheiro\n3 - Cartão\n------> "))
    if metodo_de_pagamento == 1:
        print("⬛⬜⬛⬛⬜\n⬜⬜⬛⬜⬛\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬛")
    elif metodo_de_pagamento == 2:
        print("Vá ao caixa e realize o pagamento!")
    elif metodo_de_pagamento == 3:
        cartao_v = input("Digite os números do seu cartão: ")
        salvar_variaveis('dados_pessoais.txt', cartao=cartao_v)

    print(f"\nPedido Realizado com sucesso, o número do seu pedido é: {random.randint(0, 999)}")
    print("O tempo de espera é de: ")
    segundos = 59
    minutos = random.randint(2, 6)

    while minutos >= 0:
        if segundos > -1:
            print(f"{minutos}:{segundos:02d}", end="\r")
            time.sleep(0.01)
            segundos -= 1
            if segundos == -1:
                segundos = 59
                minutos -= 1

    print("\nA comida está pronta!")
    webbrowser.open("https://www.youtube.com/shorts/ZjEJaWByFlY")

if __name__ == "__main__":
    main()

