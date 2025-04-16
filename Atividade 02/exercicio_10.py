#10.Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

#Resp: Temos duas opções, podemos remover os valores ausentes ou preencher com a média ou mediana dos dados que estão presentes.
#Exemplo:

import pandas as pd

# Exemplo de DataFrame com valores ausentes
dados = {
    'nome': ['Ana', 'Bruno', 'Carla', 'Diego'],
    'idade': [25, None, 30, 28],
    'salario': [3000, 3500, None, 4000]
}

df = pd.DataFrame(dados)

print("DataFrame original:")
print(df)

print("\nEscolha uma opção para lidar com os valores ausentes:")
print("1 - Remover linhas com valores ausentes")
print("2 - Preencher com média")
print("3 - Preencher com mediana")

opcao = input("Digite a opção (1, 2 ou 3): ")

if opcao == '1':
    df_tratado = df.dropna()
elif opcao == '2':
    df_tratado = df.copy()
    for coluna in df_tratado.select_dtypes(include='number'):
        media = df_tratado[coluna].mean()
        df_tratado[coluna].fillna(media, inplace=True)
elif opcao == '3':
    df_tratado = df.copy()
    for coluna in df_tratado.select_dtypes(include='number'):
        mediana = df_tratado[coluna].median()
        df_tratado[coluna].fillna(mediana, inplace=True)
else:
    print("Opção inválida.")
    df_tratado = df 

print("\nDataFrame após o tratamento:")
print(df_tratado)