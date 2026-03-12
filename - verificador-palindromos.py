def sin_espacios(texto):
    return texto.replace(" ", "")

def reverse_text(texto):
    return texto[::-1]

def es_palindromo(frase):
    frase_sin_espacios = sin_espacios(frase.lower())
    return frase_sin_espacios == reverse_text(frase_sin_espacios)

# Programa principal
frase = input("Ingrese una palabra o frase: ")
if es_palindromo(frase):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")