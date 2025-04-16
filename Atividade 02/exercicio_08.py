#8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

#Resp: Importamos o pandas, colocamos o arquivo em um dataframe e depois damos um print com .head pra exibir as primeiras linhas.
#Exemplo:

import pandas as pd

df = pd.read_csv('caminho')
print(df.head())