import json

with open('estoque.json','r') as arquivo:
    e = json.loads(arquivo.read())
    
escolha = -1
estoque = e
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
            quantidade_inicial = int(input('Quantidade inicial: '))
            preco_unitario = float(input("preço unitario do produto:"))
            estoque[item] = {'quantidade': quantidade_inicial }
            while quantidade_inicial<0:
                print('A quantidade inicial não pode ser negativa')
                quantidade_inicial = int(input('Quantidade inicial: '))
            estoque[item]['quantidade'] = quantidade_inicial
            while preco_unitario < 0 :
                print("o preço do produto não pode ser negativo")
                preco_unitario = float(input('preço unitario do produto: '))
            estoque[item]["preco_unitario"] = preco_unitario

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
        print("digite A para alterar quantidade:")
        print("digite B para alterar valor:")
        mudanca = input("qual a alteracao?:")
        if item_altera not in estoque:
            print('Elemento não encontrado')
        else:
            if mudanca == "A" or mudanca == "a":
                quantidade = int(input('Quantidade: '))
                estoque[item_altera]['quantidade'] += quantidade
                print ('Novo estoque de {0}: {1}'.format(item_altera, estoque[item_altera]['quantidade']))
            elif mudanca == "B" or mudanca == "b":
                novo_preco = float(input("novo preco:"))
                estoque[item_altera]["preco_unitario"] = novo_preco
                print ("Preço atualizado de {0}: {1}".format(item_altera,estoque[item_altera]["preco_unitario"]))


                

            
    if escolha == 4:
        print(estoque)
            
estoque_json = json.dumps(estoque, sort_keys = True, indent = 4)           
        
with open('estoque.json','w') as saida:
    saida.write(estoque_json)
    
    
