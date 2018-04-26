
import json

with open('estoque.json','r') as arquivo:
    e = json.loads(arquivo.read())
    
escolha = -1
estoque = e


s = False

escolha_loja = -1

while escolha_loja !=0:
    escolha_loja = -1
    print('\n')
    print('Controle de Lojas')
    print('0 - Sair')
    print('1 - Adicionar Loja')
    print('2 - Configurar estoque da Loja')
    print('3 - Deletar uma Loja')
    
    escolha_loja = int(input('Faça uma escolha: '))
    
    if escolha_loja == 0:
        print('Até mais!')
        
    if escolha_loja == 1:
        nome_loja = input('Qual o nome da loja?: ')
        if nome_loja in estoque:
            print('Loja já cadastrada')
            escolha_loja = -2
        if nome_loja not in estoque:
            s = True
            estoque[nome_loja] = {}
            
    if escolha_loja == 2:
        nome_loja = input('Qual o nome da loja?: ')
        if nome_loja not in estoque:
            print('Loja não encontrada')
        if nome_loja in estoque:
            s = True

    if s == True:
        while escolha !=0:
            print('\n')
            print('Controle de estoque')
            print('0 - Voltar')
            print('1 - Adicionar item')
            print('2 - Remover item')
            print('3 - Alterar item')
            print('4 - Imprimir estoque')   
            print('5 - Imprimir valor monetário total')
                
            escolha = int(input('Faça uma escolha: '))
            
            if estoque[nome_loja] != 0:
                a = estoque[nome_loja].keys()
                nome_produtos = []
                for r in a:
                    nome_produtos.append(r)
                
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
                    estoque[nome_loja][item] = {'quantidade': quantidade_inicial }
                    estoque[nome_loja][item]['quantidade'] = quantidade_inicial
                   
                    estoque[nome_loja][item]["preco_unitario"] = preco_unitario
        
                else:
                    print('Produto já cadastrado')
             
            if escolha == 2:
                item_remove = input('Nome do produto: ')
                if item_remove not in estoque[nome_loja]:
                    print('Elemento não encontrado')
                else:
                    del(estoque[nome_loja][item_remove])
                    
            if escolha == 3:
                item_altera = input('Nome do produto: ')
                if item_altera not in estoque[nome_loja]:
                    print('Elemento não encontrado')
                else:
                    print("Digite A para alterar quantidade:")
                    print("Digite B para alterar valor")
                    mudanca = input("Qual a alteração?:")
                    if mudanca == "A" or mudanca == "a":
                        quantidade = int(input('Quantidade: '))
                        estoque[nome_loja][item_altera]['quantidade'] += quantidade
                        print ('Novo estoque de {0}: {1}'.format(item_altera, estoque[nome_loja][item_altera]['quantidade']))
                    elif mudanca == "B" or mudanca == "b":
                        novo_preco = float(input("novo preco:"))
                        estoque[nome_loja][item_altera]["preco_unitario"] = novo_preco
                        print ("Preço atualizado de {0}: {1}".format(item_altera,estoque[nome_loja][item_altera]["preco_unitario"]))
                 
            if escolha == 4:
                if estoque[nome_loja] == 0:
                    print('Estoque vazio')
                elif estoque[nome_loja] != 0:
                    estoques_negativos   = []
                    estoques_positivos   = []
                    x = 0
                    for b in estoque[nome_loja]:
                        if estoque[nome_loja][b]['quantidade'] < 0:
                            estoques_negativos.append(nome_produtos[x])
                        elif estoque[nome_loja][b]['quantidade'] >= 0:
                            estoques_positivos.append(nome_produtos[x])
                        x+=1
                    z = 0
                    print('Produtos com quantidades positivas:')
                    if len(estoques_positivos) !=0: 
                        for k in estoque[nome_loja]:
                            if k in estoques_positivos:
                                print('\n {0}:\n    Preço unitário: {1}\n    Quantidade: {2}\n'.format(estoques_positivos[z],estoque[nome_loja][k]['preco_unitario'],estoque[nome_loja][k]['quantidade']))
                            z+=1
                    t=0
                    print('Produtos com quantidades negativas:')
                    if len(estoques_negativos) != 0:
                        for l in estoque[nome_loja]:
                            if l in estoques_negativos:
                                print('\n{0}:\n     Preço unitário: {1}\n    Quantidade: {2}\n'.format(estoques_negativos[t],estoque[nome_loja][l]['preco_unitario'],estoque[nome_loja][l]['quantidade']))
                                t+=1
                
            if escolha == 5:
                elementos = []
                for i in estoque[nome_loja]:
                    valor_tot = estoque[nome_loja][i]['quantidade']*estoque[nome_loja][i]['preco_unitario']
                    if valor_tot > 0:
                        elementos.append(valor_tot)
                resultado = sum(elementos)
                print('\n O valor monetário total é: {}'.format(resultado))
                        
                    
                    
        estoque_json = json.dumps(estoque, sort_keys = True, indent = 4)           
                
        with open('estoque.json','w') as saida:
            saida.write(estoque_json)
