# Passo a Passo: Sistema de Encomendas
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
precos= [149.99, 89.00, 99.90, 2.89, 2.78, 3.05, 3.05, 39.99, 59.99, 24.99, 
         39.99, 34.99,  27.99, 48.99, 78.80]
estoque = [15, 20, 15, 30,35, 28, 25, 15, 17,  
           30, 10, 15, 5, 7, 5]

#    1.1. Exibir lista de produtos disponíveis 
print("LISTA DE PRODUTOS".center(100))
print()
for i in range(len(produtos)):
    print(f'\n{i+1}. {produtos[i]:.<42}  Categoria: {categorias[i]:.<12} R$ {precos[i]:.2f} ... Unidades: {estoque[i]}')
print()

#    1.3. Criar dicionário vazio para armazenar encomendas dos clientes -
encomendas = {}
while True:
    #  2.1. Input para inserir o nome do cliente
    cliente = input("Digite o nome do cliente: ").title()
    # 2.2. Verificar se o cliente ja existe e criar lista vazia
    if cliente not in encomendas:
        # 2.3. Criar lista vazia para os produtos do cliente atual
        encomendas[cliente] = []
        break
    else:
        print("Cliente ja existe, Por favor insirar outro usuário \n ")
        break
    
    # 3. Seleção de Produtos
#    3.1. Input para o cliente selecionar um produto - OK
menu_opcao = int(input('Digite o número do produto: '))
#    3.2. Input para a quantidade desejada do produto - OK
quant_produto = int(input('Quantas unidade: '))
print()

#   3.3.  Selecionar o produto
if menu_opcao <= len(produtos):
    produto_selecionado = produtos[menu_opcao - 1]
    categoria_selecionada = categorias[menu_opcao - 1]
    preco_unitario = precos[menu_opcao - 1]
    total_produto = quant_produto * preco_unitario
    quant_estoque = estoque[menu_opcao - 1]

    #    3.3. Verificar se há estoque suficiente
    while True:
        if quant_estoque > 0 and quant_estoque >= quant_produto:
            print("Você adicionou:")
            # Mostar a compra e adicionar na variável encomendas
            print(f'\t Produto: {produto_selecionado}') # Mostrar o produto selecionado
            encomendas[cliente].append(produto_selecionado) # Adicionar o produto na lista de encomendas
        
            print(f'\t Categoria: {categoria_selecionada}') # Mostrar a categoria
            encomendas[cliente].append(categoria_selecionada) # Adicionar a categoria na lista de compras
        
            print(f'\t Preço unitário: {preco_unitario}') # Mostrar o preoço unitário

            print(f'\t Quantidade: {quant_produto}') # Mostrar a quantidade de produtos comprado
            encomendas[cliente].append(quant_produto) # Adicionar quandidade de produtos na lista de compras

            print(f'\n\t Total do produto: {total_produto:.2f}') # Mostrar o Total da compta
            encomendas[cliente].append(f'{total_produto:.2f}') # Adicionar o total da compra na lista
            break
        else:
            print(f'Quantidade insuficiente. Estoque: {quant_estoque} \n')
    
            continuar = input('Deseja comprar este produto [S/N]: ').upper()
            
            if continuar == 'S':
                quant_produto = int(input('Quantas unidade: '))

                # print(f'\n\t Total do produto: {total_produto:.2f}') # Mostrar o Total da compta
                # encomendas[cliente].append(f'{total_produto:.2f}') # Adicionar o total da compra na lista
            elif continuar == 'N':
                break     

print()
print(encomendas)
