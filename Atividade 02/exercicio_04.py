#4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista

def segundo_maior(lista):
    if len(lista) < 2:
        return print("A lista deve conter pelo menos dois elementos.")
    if len(lista) == 2:
        return min(lista)
    lista_ordenada = sorted(lista, reverse=True)
    segundo_maior = lista_ordenada[1]
    print(f"O segundo maior valor é: {segundo_maior}")

numeros = list(map(int, input("Digite a lista de números separados por espaço: ").split()))

resultado = segundo_maior(numeros)