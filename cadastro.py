valor_total_pedido = 0
lista_carrinho = []

def cardapio():
    while True:
        print("Este é o nosso cardápio! Aproveite!")
        print("1. Salgados\n2. Hamburger\n3. Bebidas\n4. Fechar")
        entrada = input("Selecione uma das nossas opções: ")

        if entrada == "1":
            salgados()
        elif entrada == "2":
            burger()
        elif entrada == "3":
            bebidas() 
        elif entrada == "4":
            print("Agradecemos a sua visita! Esperamos por você na próxima :)")
            break  
        else:
            print("A Cleide Lanches não entendeu. Tente novamente.")

        if confirmar_pedido(lista_carrinho):
            total = calcular_total(lista_carrinho)
            print(f"Seu pedido foi confirmado e o valor total ficou de: R$ {total:.2f}")
            lista_carrinho.clear()  
        else:
            print("Voltando ao menu principal")

def calcular_total(carrinho):
    return sum(item["valor"] for item in carrinho)

def perguntar_se_deseja_continuar():
    while True:
        opcao = input("Deseja pedir mais alguma coisa? [s] ou [n]: ")
        if opcao == "s":
            return cardapio()
        elif opcao == "n":
            return False
        else:
            print("Opção inválida. Tente novamente.")

def salgados():
    print("Ótima escolha!")
    print("1. Pastel\n2. Risólis\n3. Enroladinho")
    entrada = input("Selecione uma das nossas opções: ")

    if entrada == "1":
        pastel()
    elif entrada == "2":
        risolis()
    elif entrada == "3":
        enroladinho = {"nome": "Enroladinho", "valor": 2.00}
        lista_carrinho.append(enroladinho)
        print("Você escolheu Enroladinho.")
    else:
        print("Opção inválida.")
    
    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def pastel():
    print("Opções de Pastel: ")
    entrada = input("1. Carne\n")
    if entrada == "1":
        pastel = {"nome": "Pastel de Carne", "valor": 5.00}
        lista_carrinho.append(pastel)
        print("Você escolheu Pastel de Carne.")
    else:
        print("Opção inválida.")
    
    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def risolis():
    print("Opções de Risólis: ") 
    entrada = input("1. Carne\n")
    if entrada == "1":
        risolis = {"nome": "Risólis de Carne", "valor": 4.00}
        lista_carrinho.append(risolis)
        print("Você escolheu Risólis de Carne.")
    else:
        print("Opção inválida.")
    
    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def burger():
    print("Opções de Hamburger: ")
    entrada = input("1. Cleide 1\n")
    if entrada == "1":
        burger = {"nome": "Cleide 1", "valor": 5.00}
        lista_carrinho.append(burger)
        print("Você escolheu Cleide 1.")
    else:
        print("Opção inválida.")
    
    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def bebidas():
    print("Opções de Bebidas: ")
    print("1. Pepsi\n2. Fanta\n3. Guaraná\n4. Sprite\n5. Tap Water")
    entrada = input("Escolha uma bebida: ")

    if entrada in ['1', '2', '3', '4']:
        refri = {"nome": "Refrigerante", "valor": 5.00}
        lista_carrinho.append(refri)
        print("Você escolheu Refrigerante Lata.")
    elif entrada == "5":
        agua = {"nome": "Água", "valor": 3.00}
        lista_carrinho.append(agua)
        print("Você escolheu Tap Water.")
    else:
        print("Opção inválida.")

    if not perguntar_se_deseja_continuar():
        confirmar_pedido(lista_carrinho)

def confirmar_pedido(lista_carrinho):
    if lista_carrinho:
        print("Você escolheu:")
        for item in lista_carrinho:
            print(f"- {item['nome']} (R$ {item['valor']:.2f})")
    else:
        print("Você não fez nenhum pedido.")
        return False

    confirmar = input("Deseja confirmar o pedido? [s] ou [n]: ")
    if confirmar == "n":
        print ("Retornando ao menu principal.")
        cardapio()
    return confirmar.lower() == "s"

cardapio()
