#1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def numeros_impar(lista):
    lista_impar = []
    for x in lista:
        if x % 2 == 1:
            lista_impar.append(x)
    print(lista_impar)

numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))

resultado = numeros_impar(numeros)