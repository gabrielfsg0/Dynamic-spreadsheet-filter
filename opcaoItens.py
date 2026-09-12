
def opcao_itens(valores):
    #escolha dos itens que quero gerar arquivo
    print('Itens disponíveis: ')

    for i, itens in enumerate(valores, start=1):
        print(f'{i} - {itens}')
        
    print('Todas opções')

    while True:
        try:

            entrada = input('\nEscolha a opção de valor: ').lower()
            if 'todas' in entrada:
                valores_escolhidos = valores
                break

            else:
                opcoes = entrada.split(',')

                valores_escolhidos = []

                for opcao in opcoes:

                    numero = int(opcao.strip())
                    valor = valores[numero - 1]
                    valores_escolhidos.append(valor)
                    
                #Transformo minha lista em uma coleção para excluir valores duplicados
                valores_escolhidos = list(set(valores_escolhidos))
                
                break

        except:
            print('Valor indisponível!')

    return valores_escolhidos