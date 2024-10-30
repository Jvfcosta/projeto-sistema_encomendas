import os
# 1. Criar lista de produtos 
produtos = ['Ração Golden Adulto 15kg Cães', 'Ração GranPlus 15kg Cães',
        'Ração Magnus para Cães 15kg', 'GranPlus Sachê Cães Carne 100g',
        'GranPlus Sachê Gatos Carne 100g', 'Whiskas Sachê Carne ao Molho Gatos 85g',
        'Pedigree Sachê Cães Carne ao Molho 100g', 'Shampoo Hipoalergênico 500ml',
        'Shampoo Antisséptico 500ml', 'Lenços Umedecidos',
        'Areia Higiênica Petz 12Kg', 'Coleira Peitoral Ajustável', 
        'Guia Retrátil Chalesco', 'Cama Pet Cachorro/Gato tamanho Médio',
        'Colchão Cachorro Grande 90x60cm']

categorias = ['Alimento', 'Alimento', 'Alimento', 'Alimento', 'Alimento', 'Alimento', 'Alimento', 
              'Higiêne', 'Higiêne', 'Higiêne', 'Higiêne', 'Acessório', 'Acessório', 
              'Acessório', 'Acessório']

precos= [149.99, 89.00, 99.90, 2.89, 2.78, 3.05, 3.05, 39.99, 29.99, 24.99, 
         39.99, 34.99,  27.99, 48.99, 78.80]
estoque = [15, 20, 15, 30,35, 28, 25, 15, 17, 30, 10, 15, 5, 7, 5]

def menu_inicial():
    print('Bem-Vindo ao CLUBE PET 🐶🐾🐾'.center(35))
        
    print('-' * 36)
    print(f' <<< Menu >>> '.center(35))
    print('-' * 36)
    print('| [1] Compras                      |'.center(20))
    print('| [2] Adicionar produto ao estoque |'.center(20))
    print('| [3] Sair                         |'.center(20))
    print('-' * 36)
    
# Cadastro de produto
def cadastro_produto():
    # Adicionar produtos ao estoque
    novo_produto = input(" Digite o nome do produto: ")
    try:
        qtd_produto= int(input(" Quantidade do produto: "))
    except ValueError:
        print("Quantidade deve ser um número inteiro")
        return
    
    # Verificar se o produto  já existe
    for i in range(len(produtos)):
        if produtos[i] == novo_produto:
            while  True:
                resposta = input(f"\n Produto {novo_produto} já está cadastrado.\n" 
                      f" Deseja atualizar a quantidade do produto? [S/N]: ").upper()
                if resposta == 'S':
                    estoque[i] += qtd_produto
                    print(f'\n Quantidade do produto {novo_produto} atualizado para {estoque[i]} unidades')
                    return True
                elif resposta != 'S' and resposta != 'N':
                    print('Opção inválida. Digite "S" para continuar ou "N" para encerrar')
                    continue
                else:
                    break
        if novo_produto not in produtos:
            categoria_produto =  input(" Digite a categoria do produto: ")
            preco_produto = float(input(" Digite o preço do produto: "))
            
            # Armazenando  os dados do produto
            produtos.append(novo_produto)
            categorias.append(categoria_produto)
            precos.append(preco_produto)
            estoque.append(qtd_produto)
            print(f'\n Produto {novo_produto} adicionado com sucesso')
            return True

# Acesso para cadastro dos produtos
def acesso_cadastro():
    usuario = input("Login: ")
    senha = input("Senha: ")

    try:
        if usuario == "adm" and senha == 'adm':
            os.system('cls') #  Limpar a tela

            print("CLUBE PET 🐶🐾🐾".center(45))
            return True
        else:
            print("\n Login ou senha inválida.")
            return False
    except:
        print()

# Criar dicionário vazio 
encomendas = {}

while True:
    menu_inicial()
    try:
        menu = int(input('Olá, escolha uma das opções acima: '))
    except ValueError:
        os.system('cls')
        print('\n \033[31m Por favor, digite um número válido \033[0m \n')
        continue
    
    if menu == 1:
        cliente = input('Como podemos te chamar? ').title()  # Input  usuário 
        os.system('cls') #  Limpar tela

        print("CLUBE PET 🐶🐾🐾".center(25))
        
        # Verificar se o cliente ja existe e criar lista vazia
        if cliente not in encomendas:
            encomendas[cliente] = []
            indice = 0
            total = 0
        else:
            print("\033[31m Cliente ja existe, Por favor insirar outro nome \033[0m \n ")
            continue
        
        #  Exibir lista de produtos disponíveis
        print("LISTA DE PRODUTOS".center(100))
        print()
        for i in range(len(produtos)):
            print(f'{i+1}. {produtos[i]:.<42} Categoria: {categorias[i]:.<12}',
                  f'Preço: R$ {precos[i]:.2f} ... Unidades: {estoque[i]} \n')

        continuar_compra = True   # Variável de controle
        while continuar_compra:   # Seleção de produtos
            try:
                menu_opcao = int(input(f'\n{cliente}. Digite o número do produto: '))
                menu_opcao = int(menu_opcao)
            except ValueError:
                print('\n \033[31m Opção inválida. Por favor, digite um número válido \033[0m \n')
                continue
            
            # Input quantidade de produto
            try:
                quant_produto = int(input('Quantas unidade: '))
            except ValueError:
                print('\n \033[31m Por favor, digite um número válido \033[0m \n')
                continue
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
                    encomendas[cliente].append((produto_selecionado, categoria_selecionada, 
                                                preco_unitario, quant_produto, 
                                                total_produto))
                    
                    # Remover a quantidade de produtos
                    estoque[menu_opcao - 1] -= quant_produto

                else:
                    print(f'     \033[31m Quantidade insuficiente. Estoque contêm {quant_estoque} unidade \033[0m \n')
                encerrar = True
                while encerrar: #  Loop para add mais produtos
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
                        print('|   [4] Sair                 |'.center(25))
                        print('-'*30)
        
                        finalizar = int(input("\n Escolha uma das opçôes acima: "))
                        if finalizar == 1: # Volta para as compras
                            break
                        elif finalizar == 2:
                            print("Carrinho: ")
                            indice = 0 # Resetar a unidade

                            for produto in encomendas[cliente]:
                                indice += 1
                                print(f'\t {indice}. Produto: {produto[0]}')
                                print(f'\t    Categoria: {produto[1]}')
                                print(f'\t    Preço unitário: R$ {produto[2]:.2f}')
                                print(f'\t    Quantidade: {produto[3]}')
                                print(f'\t    Total: R$ {produto[4]:.2f}')
                                print('-' * 70)
        
                            remover_item = int(input('Digite o número do produto que deseja remover: '))
                            if remover_item <= len(encomendas[cliente]):
                                item_removido =  encomendas[cliente][remover_item - 1]
                                
                                del encomendas[cliente][remover_item - 1] # Removendo o item                                                
                                estoque[menu_opcao - 1] += produto[3] # Add item removido para o estoque 
                                
                                print(f"O item {item_removido[0]} foi removido do carrinho e devolvido ao estoque") # Mostrar  o item removido                             
                                print()
                                continue
                            else:
                                print(' \033[31m Opção inválida. Tente novamente \033[0m ')      
                        
                        elif finalizar == 3: # Encerrar as compras
                            total = 0
                            print(f'{cliente}, seus produtos são: '.upper())
                            for produto in encomendas[cliente]:
                                indice += 1
                                print(f'\t Produto: {produto[0]}')
                                print(f'\t Categoria: {produto[1]}')
                                print(f'\t Preço unitário: R$ {produto[2]:.2f}')
                                print(f'\t Quantidade: {produto[3]}')
                                print(f'\t Total: R$ {produto[4]:.2f}')
                                print()
     
                                total += produto[4]   # Calculo total dos produtos
                            if total > 300:
                                desconto_compra = total * 0.10  # Aplicar desconto
                                print(f'Valor total da compra: R$ {round(total, 2)}')  # Total da compra
                                print(f'Desconto de 10%: R$ {round(desconto_compra, 2)}') # Calculo do desconto
                                print(f'Valor após o desconto: R$ {round(total - desconto_compra, 2)}\n\n') # Resultado
                            
                            else:
                                print(f'Valor total da compra: R$ {round(total, 2)}\n\n')  # Mostrar total da compra
        
                            continuar_compra = False # Variável de controle encerrando o Loop
                            print()        
                            break

                        elif finalizar == 4:
                            estoque[menu_opcao - 1] += quant_produto
                            continuar_compra = False
                            print('Obrigado por visitar nossa loja \n')
                            break
                    else:
                        print(' \033[31m Opção inválida. Tente novamente \033[0m')
                        pass
        
    elif menu == 2:
        cadastro = True
        while cadastro:
            os.system('cls')
            print("CLUBE PET 🐶🐾🐾".center(40))
            
            if acesso_cadastro():
                while True:
                    # print("CLUBE PET 🐶🐾🐾".center(50))
                    cadastro_produto()
                    
                    cadastrar_itens = input("\n Deseja cadastrar um produtos [S/N]: ").upper()
                    print()
                    if cadastrar_itens == 'S':
                        continue                
                    elif cadastrar_itens == 'N':
                        os.system('cls')
                        break
                    else:
                        print(" Digite 'S'para continuar ou 'N' para encerrar!")
                        continue
                cadastro = False  
    elif menu == 3:
        print('\n Obrigado por visitar a nossa loja')
        break