def contar_vogais():
    palavra = input("Digite uma palavra: ")
    palavra = palavra.lower()
    vogais = "aeiou"
    resultado = 0

    for letra in palavra:
        if letra in vogais:
            resultado += letra.count(letra)

    print(f"Na palavra {palavra}, existem", resultado, "vogais")


contar_vogais()
