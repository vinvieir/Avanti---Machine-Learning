#9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

#Resp: Primeiro importamos o pandas e o dataframe e depois selecionamos a coluna e damos a condição na linha.
#Exemplo:

import pandas as pd

dados = {
    'nome': ['Ana', 'Bruno', 'Carla', 'Diego'],
    'idade': [22, 35, 17, 42]
}

df = pd.DataFrame(dados)

maior_que_30 = df[df['idade'] > 30]

print(maior_que_30)