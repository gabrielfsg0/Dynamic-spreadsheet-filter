import pandas as pd
import os

def escolher_arquivo():
    while True:
        try:
            pastas = [
                pasta for pasta in os.listdir('.') # lista de caminhos 
                if os.path.isdir(os.path.join('.', pasta)) # avalia se o caminho corresponde a um diretório
                            ]

            for i, pasta in enumerate(pastas, start=1):
                print(f'{i} - {pasta}')

            opcao = int(input('Selecione a pasta desejada: '))

            selecionado = pastas[opcao - 1]

            caminho = os.path.join('.', selecionado) #cria um caminho para a pasta selecionada

            #Seleção de arquivos existentes em uma pasta no meu diretorio
            arquivos_csv = [
                arquivos for arquivos in os.listdir(caminho) # lista de caminhos 
                if arquivos.lower().endswith('.csv') # pegamos apenas caminhos que terminam com '.csv'
                ]

            for i, arquivo in enumerate(arquivos_csv, start=1):
                print(f'{i} - {arquivo}')

            opcao = int(input('Selecione o arquivo desejado: '))

            selecionado = arquivos_csv[opcao - 1]

            caminho = os.path.join(caminho, selecionado) #cria um caminho para o arquivo selecionada

            ler = pd.read_csv(caminho) #le o arquivo
        
            break
        
        except:
            print('Caminho não encontrado!')

    return ler

