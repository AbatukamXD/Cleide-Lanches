import time
import random
import webbrowser

print(f"\n Pedido Realizado com sucesso, o numero do seu pedido é: {random.randint(0,999)} \n O Tempo de espera é de: ")
segundos = 59 
minutos = random.randint(5, 10)

print(minutos,":", segundos )

while minutos >= 0:
   
    if segundos > -1:
        print(minutos,":", segundos )
        segundos -= 1
        time.sleep (0.1)
        if segundos == -1:
            segundos = 59
            minutos += -1

print("\nA comida está pronta!")

webbrowser.open("https://www.youtube.com/shorts/ZjEJaWByFlY")
