import pandas as pd
import os
from caminhos import escolher_arquivo
from opcaoColunas import opcao_coluna
from opcaoItens import opcao_itens

# Escolhendo arquivo
df = escolher_arquivo() 

# Definindo colunas do arquivo
df.columns = df.columns.str.strip()

# Escolhendo coluna que sera usada de filtro
filtro = opcao_coluna(df.columns)

# De acordo com o filtro pegamos valores unicos e não nulos
valores = df[filtro].dropna().unique()

# Escolha dos itens na coluna que serao utilizados para gerar arquivos
itens = opcao_itens(valores)

# criando um repositorio
repositorio = input('Em qual pasta deseja salvar? ').strip()
os.makedirs(repositorio, exist_ok=True)

# Definindo os filtros
for valor in itens:

    df_filtro = df[df[filtro] == valor]

    #cria nome do arquivo no diretorio de acordo com o nome da variavel iterada
    nome_arquivo = os.path.join(repositorio, f'{valor}.csv')

    df_filtro.to_csv(nome_arquivo, index = False)

    print(f'Arquivo criado: {nome_arquivo}')