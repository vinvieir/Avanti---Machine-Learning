#2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def numeros_primos(lista):
    lista_primos = []
    for x in lista:
        if x > 1:
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    break
            else:
                lista_primos.append(x)
    print(lista_primos)

numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))

resultado = numeros_primos(numeros)