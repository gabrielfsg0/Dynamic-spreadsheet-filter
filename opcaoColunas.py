
def opcao_coluna(colunas):
    #mostra pro usuário opções de filtro
    print('Colunas disponíveis:\n')

    for i, itens in enumerate(colunas, start = 1):
        print(f'{i} - {itens}')

    while True:
        try:
            #usuario escolhe opcao do filtro desejado
            opcao = int(input('\nEscolha a opção de filtro: '))
            #opcao atribuida
            filtro = colunas[opcao - 1]
            break

        except:
            print('Opção não disponível!')

    return filtro