import json

with open('estoque.json','r') as arquivo:
    e = json.loads(arquivo.read())
    
escolha = -1
estoque = e
a = estoque.keys()

if len(estoque)!=0:
    nome_produtos = []
    for r in a:
        nome_produtos.append(r)


while escolha !=0:
    print('\n')
    print('Controle de estoque')
    print('0 - Sair')
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Alterar item')
    print('4 - Imprimir estoque')   
    print('5 - Imprimir valor monetário total')
        
    escolha = int(input('Faça uma escolha: '))
        
    if escolha == 0:
        print('Até mais!')
        
    if escolha == 1:
        item = input('Nome do produto: ')
        if item not in estoque:
            quantidade_inicial = int(input('Quantidade inicial: '))
            while quantidade_inicial<0:
                print('A quantidade inicial não pode ser negativa')
                quantidade_inicial = int(input('Quantidade inicial: '))
            preco_unitario = float(input("preço unitario do produto:"))
            while preco_unitario < 0 :
                print("O preço do produto não pode ser negativo")
                preco_unitario = float(input('preço unitario do produto: '))
            estoque[item] = {'quantidade': quantidade_inicial }
            estoque[item]['quantidade'] = quantidade_inicial
           
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
        if item_altera not in estoque:
            print('Elemento não encontrado')
        else:
            print("Digite A para alterar quantidade:")
            print("Digite B para alterar valor")
            mudanca = input("Qual a alteração?:")
            if mudanca == "A" or mudanca == "a":
                quantidade = int(input('Quantidade: '))
                estoque[item_altera]['quantidade'] += quantidade
                print ('Novo estoque de {0}: {1}'.format(item_altera, estoque[item_altera]['quantidade']))
            elif mudanca == "B" or mudanca == "b":
                novo_preco = float(input("novo preco:"))
                estoque[item_altera]["preco_unitario"] = novo_preco
                print ("Preço atualizado de {0}: {1}".format(item_altera,estoque[item_altera]["preco_unitario"]))
         
    if escolha == 4:
        estoques_negativos   = []
        estoques_positivos   = []
        x = 0
        for b in estoque:
            if estoque[b]['quantidade'] < 0:
                estoques_negativos.append(nome_produtos[x])
            elif estoque[b]['quantidade'] >= 0:
                estoques_positivos.append(nome_produtos[x])
            x+=1
        z = 0
        print('Produtos com quantidades positivas:')
        if len(estoques_positivos) !=0: 
            for k in estoque:
                if k in estoques_positivos:
                    print('\n {0}:\n    Preço unitário: {1}\n    Quantidade: {2}\n'.format(estoques_positivos[z],estoque[k]['preco_unitario'],estoque[k]['quantidade']))
                z+=1
        t=0
        print('Produtos com quantidades negativas:')
        if len(estoques_negativos) != 0:
            for l in estoque:
                if l in estoques_negativos:
                    print('\n{0}:\n     Preço unitário: {1}\n    Quantidade: {2}\n'.format(estoques_negativos[t],estoque[l]['preco_unitario'],estoque[l]['quantidade']))
                    t+=1
        
    if escolha == 5:
        elementos = []
        for i in estoque:
            valor_tot = estoque[i]['quantidade']*estoque[i]['preco_unitario']
            if valor_tot > 0:
                elementos.append(valor_tot)
        resultado = sum(elementos)
        print('\n O valor monetário total é: {}'.format(resultado))
                
            
            
estoque_json = json.dumps(estoque, sort_keys = True, indent = 4)           
        
with open('estoque.json','w') as saida:
    saida.write(estoque_json)
