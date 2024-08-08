
import random
numero_secreto = random.randint(0, 100)
adivinado = False
cant_intentos = 0
cant_max_intentos = 5

print("¡Bientevenido al juego de adivinar el numero secreto!")

while not adivinado and cant_intentos < cant_max_intentos:
    numero = input("Introduce un numero entre 1 al 99: ")
    numero = int(numero)

    if numero == numero_secreto:
        print("Felicidades, has adivinado el numero!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero secreto es mayor al ingresado")
    else:
        print("El numero secreto es menor al ingresado")

    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print("¡GAME OVER!Se han agotado los intentos. El numero secreto era:", numero_secreto)