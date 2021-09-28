import random


def eject_program():
    eject = True
    while eject:
        chars = int(input("\nIndique la cantidad de caracteres para su contraseña: "))
        pass_generator(chars)
        eject = input("Desea continuar el programa?: ")
        if eject == "si" or eject== "SI":
            eject = True
        else: 
            eject = False
            print("\n!!Recuerda siempre mantener una complejidad alta para tu contraseña!!\n\n\t\t ¡Hasta Pronto!")

def pass_generator(chars):
    masyusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g"]
    simbolos = ["!", "#", "$", "&", "/", "(", ")"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = masyusculas + minusculas + simbolos + numeros
    contrasena = []

    for i in range(chars):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena = "".join(contrasena)
    print("\nTu nueva contraseña es: " + contrasena)
    archive = open("contraseñas_almacenadas.txt", "a")
    archive.write(f"Contraseña almacenada = {contrasena}\n")
    archive.write("\n")
    archive.close()
