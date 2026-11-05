def cesar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if "a" <= caracter <= "z":
            base = ord("a")
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        elif "A" <= caracter <= "Z":
            base = ord("A")
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        else:
            # Conserva espacios, números y signos de puntuación.
            resultado += caracter

    return resultado


texto = input("Introduce el texto: ")
desplazamiento = int(input("Introduce el desplazamiento: "))

opcion = input("¿Cifrar (c) o descifrar (d)? ")

if opcion == "c":
    print("Texto cifrado:", cesar(texto, desplazamiento))
else:
    print("Texto descifrado:", cesar(texto, -desplazamiento))