import os

# 1. Criar lista de produtos 
produtos = ['Ração Golden Adulto (15kg) Cães', 'Ração GranPlus (15kg) Cães',
        'Ração Magnus para Cães (15kg)', 'GranPlus Sachê Cães Carne 100g',
        'GranPlus Sachê Gatos Carne 100g', 'Whiskas Sachê Carne ao Molho Gatos 85g',
        'Pedigree Sachê Cães Carne ao Molho 100g', 'Shampoo Hipoalergênico (500ml)',
        'Shampoo Antisséptico (500ml)', 'Lenços Umedecidos',
        'Areia Higiênica Petz Grãos Finos (12Kg)', 'Coleira Peitoral Ajustável', 
        'Guia Retrátil Chalesco', 'Cama Pet Cachorro/Gato tamanho Médio',
        'Colchão Cachorro Grande 90x60cm']

categorias = ['Alimento', 'Alimento', 'Alimento', 'Alimento', 'Alimento', 'Alimento', 'Alimento', 
              'Higiêne', 'Higiêne', 'Higiêne', 'Higiêne', 'Acessório', 'Acessório', 
              'Acessório', 'Acessório']

precos= [149.99, 89.00, 99.90, 2.89, 2.78, 3.05, 3.05, 39.99, 29.99, 24.99, 
         39.99, 34.99,  27.99, 48.99, 78.80]
estoque = [15, 20, 15, 30,35, 28, 25, 15, 17, 30, 10, 15, 5, 7, 5]

# Criar dicionário vazio 
encomendas = {}
indice = 0
total = 0

while True:
    print('Bem-Vindo ao CLUBE PET 🐶🐾🐾'.center(20))
        
    print('-' * 30)
    print(f'<<< Menu >>>'.center(30))
    print('-' * 30)
    print('|    [1] Lista de produtos   |'.center(20))
    print('|    [2] Sair                |'.center(20))
    print('-' * 30)

    # Input  usuário
    cliente = input('Como podemos te chamar? ').lower()
    
    # Verificar se o cliente ja existe e criar lista vazia
    if cliente not in encomendas:
        # Criar lista vazia para os produtos do cliente atual
        encomendas[cliente] = []
    else:
        print("Cliente ja existe, Por favor insirar outro usuário \n ")
        pass   
    
    menu = int(input(f'Olá {cliente}, escolha uma das opções acima: '))
    if menu == 1:
        #  Exibir lista de produtos disponíveis 
        print("LISTA DE PRODUTOS".center(100))
        print()
        
        for i in range(len(produtos)):
            print(f'{i+1}. {produtos[i]:.<42}, Categoria: {categorias[i]:.<12}', 
                  f'Preço: R$ {precos[i]:.2f} ... Unidades: {estoque[i]} \n')
    elif menu == 2:
        print('\n Obrigado por visitar a nossa loja')
        break
    
    continuar_compra = True   # Variável de controle
    while continuar_compra:   # Seleção de produtos
        menu_opcao = int(input('Digite o número do produto: '))
        
        # Input quantidade de produto
        quant_produto = int(input('Quantas unidade: '))
        print()
        
        # Selecionar o produto
        if menu_opcao <= len(produtos):
            produto_selecionado = produtos[menu_opcao - 1]
            categoria_selecionada = categorias[menu_opcao - 1]
            preco_unitario = precos[menu_opcao - 1]
            quant_estoque = estoque[menu_opcao - 1]  
            total_produto = quant_produto * preco_unitario
            
            # Verificar se há estoque suficiente
            if quant_estoque > 0 and quant_estoque >= quant_produto:
                # Mostar a compra e adicionar na variável encomendas
                print("Você adicionou:")            
                print(f'\t Produto: {produto_selecionado}')        
                print(f'\t Categoria: {categoria_selecionada}')             
                print(f'\t Preço unitário: {preco_unitario}') 
                print(f'\t Quantidade: {quant_produto}') 
                print(f'\n\t Total do produto: {total_produto:.2f}')
                
                # Adicionar os dados no dicionario encomenda
                encomendas[cliente].append({
                    'produto': produto_selecionado,
                    'categoria': categoria_selecionada,
                    'quantidade': quant_produto,
                    'preco_unitario': preco_unitario,
                    'total_produto': round(total_produto, 2)
                    }) 
                # Remover a quantidade de produtos
                estoque[menu_opcao - 1] -= quant_produto
                # print()
                # print(estoque[menu_opcao - 1])
                # print()
            else:
                print(f'     \033[31m Quantidade insuficiente. Estoque contem {quant_estoque} unidade \n')        
                print()
    
            while True: #  Loop para add mais produtos
                continuar = input("Deseja adicionar mais produto [S/N]: ").upper()
                if continuar == 'S':
                    break    # Parar o loop e retornar ao primeiro loop
                elif continuar != 'S' and continuar != 'N': 
                    print("Opção invalida. Por favor, digite 'S' para continuar ou 'N' para encerrar as compras.\n")
                    continue   
                elif continuar == 'N':
                    print()
                    
                    print(f'-'*30)
                    print(f"  {'=' * 3} << Você deseja? >> {'=' * 3}")
                    print('-'*30)
                    print('|   [1] Adiconar produtos    |'.center(30))
                    print('|   [2] Remover produto(s)   |'.center(25))
                    print('|   [3] Finalizar compras    |'.center(25))

                    finalizar = int(input("Escolha uma das opçôes acima: "))
                    if finalizar == 1: # Volta para as compras
                        break
                    elif finalizar == 2:
                        print("Carrinho: ")
        
                        for item in encomendas[cliente]:
                            indice +=1
                            print(f"\t {indice}. Categoria: {item['categoria']}",
                                  f"\n\t Produto: {item['produto']}",
                                  f"\n\t Preço Unitário: {item['preco_unitario']}"
                                  f"\n\t Quantidade: {item['quantidade']}", 
                                  f"\n\t Total do Porduto: {item['total_produto']}\n")

                        # Remover itens da lista
                        remover_item = int(input('Digite o número do produto que deseja remover: '))
                        
                        if remover_item <= len(encomendas[cliente]): # Condição
                            del encomendas[cliente][remover_item - 1] # removendo o item
                            estoque[menu_opcao - 1] += quant_produto # Add item removido para o estoque
                            print()
                            # print(estoque[menu_opcao - 1]) # Validação
                            # print()
                            print('Produto removido com sucesso.')
                            continue
                        else:
                            print('Opção inválida. Tente novamente')
                    
                    elif finalizar == 3: # Encerrar as compras
                        print(f'{cliente}, seus produtos são: '.upper())
                        
                        for item in encomendas[cliente]:
                            print(f"\t Categoria: {item['categoria']}",
                                      f"\n\t Produto: {item['produto']}",
                                      f"\n\t Preço Unitário: {item['preco_unitario']}",
                                      f"\n\t Quantidade: {item['quantidade']}", 
                                      f"\n\t Total do Porduto: {item['total_produto']}\n")
                            
                            total += item['total_produto']   # Calculo total dos produtos
                        if total > 300:
                            desconto_compra = total * 0.10  # Aplicar desconto
    
                        print(f'Valor total da compra: {round(total, 2)}')  # Mostrar total da compra
                        print(f'Desconto de 10%: {round(desconto_compra, 2)}') # Mostrar calculo do desconto
                        print(f'Valor após o desconto: {round(total - desconto_compra, 2)}\n\n') # Mostrar o resultado com o desconto
    
                        continuar_compra = False # Variável de controle encerrando o Loop
                        break
                else:
                    print('Opção inválida. Tente novamente')
