#3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

def listas_unicas(lista1, lista2):
    lista_unica = []
    for x in lista1:
        if x not in lista2:
            lista_unica.append(x)
    for y in lista2:
        if y not in lista1:
            lista_unica.append(y)
    print(lista_unica)

numeros1 = list(map(int, input("Digite a primeira lista de números separados por espaço: ").split()))
numeros2 = list(map(int, input("Digite a segunda lista de números separados por espaço: ").split()))

resultado = listas_unicas(numeros1, numeros2)