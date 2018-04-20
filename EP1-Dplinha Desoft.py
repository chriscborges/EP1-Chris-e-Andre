escolha = -1

estoque = {}

while escolha !=0:
    print('\n')
    print('Controle de estoque')
    print('0 - Sair')
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Alterar item')
    print('4 - Imprimir estoque')

    escolha = int(input('Faça uma escolha: '))

    if escolha == 0:
        print('Até mais!')
        
    if escolha == 1:
        item = input('Nome do produto: ')
        if item not in estoque:
            estoque[item] = {'quantidade': }
            quantidade_inicial = int(input('Quantidade inicial: '))
            while quantidade_inicial<0:
                print('A quantidade inicial não pode ser negativa')
                quantidade_inicial = int(input('Quantidade inicial: '))
            estoque[item]['quantidade'] = quantidade_inicial
        else:
            print('Produto já cadastrado')
      
    if escolha == 2:
        item_remove = input('Nome do produto: ')
        if item_remove not in estoque:
            print('Elemento não encontrado')
        else:
            del(estoque[item_remove])
            
    if escolha == 3:
        item_altera = input('Nome do produto: ')
        if item_altera not in estoque:
            print('Elemento não encontrado')
        else:
            quantidade = int(input('Quantidade: '))
            estoque[item_altera] += quantidade
            print ('Novo estoque de {0}: {1}'.format(item_altera, estoque[item_altera]['quantidade']))
            
    if escolha == 4:
        print(estoque)
            
