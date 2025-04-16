#5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def ordenar_por_nome(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key=lambda x: x[0])
    print(lista_ordenada)

pessoas = [tuple(pessoa.split(',')) for pessoa in input("Digite o nome e a idade de cada pessoa (separados por vírgula) e separados por espaço: ").split()]

ordenar_por_nome(pessoas)