print("Ingresa el mensaje cifrado")
mensaje = input()
print("¿Cuántas veces quieres se movió la letra en el mensaje original?")
veces = int(input())

mensajeDescifrado = ""

for i in range(0, len(mensaje), 1):
    letra = mensaje[i]
    minuscula = (letra >= 'a' and letra <= 'z')
    mayuscula = (letra >= 'A' and letra <= 'Z')
    if not(minuscula or mayuscula):
        mensajeDescifrado += letra
    else:
        ascii = ord(letra)
        baseAscii = ord('a')
        if mayuscula:
            baseAscii = ord('A')
        nuevoAscii = (ascii - baseAscii - veces) % 26 + baseAscii
        nuevaLetra = chr(nuevoAscii)
        mensajeDescifrado += nuevaLetra

print(mensajeDescifrado)
