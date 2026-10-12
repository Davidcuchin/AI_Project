import random

def recommendation_system():
    opciones = ["piedra", "papel", "tijera"]

    print("=== Piedra, Papel o Tijera ===")
    eleccion = input("Elige piedra, papel o tijera: ").lower().strip()

    if eleccion not in opciones:
        print("Opción no válida. Elige piedra, papel o tijera.")
        return

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if eleccion == computadora:
        print("¡Empate!")
    elif (eleccion == "piedra" and computadora == "tijera") or \
         (eleccion == "papel" and computadora == "piedra") or \
         (eleccion == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

recommendation_system()
