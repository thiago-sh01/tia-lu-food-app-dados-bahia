menu = []
pedidos = []
fila_pendentes = []
fila_aceitos = []
fila_prontos = []

proximo_codigo_item = 1
proximo_codigo_pedido = 1


while True:
    print("\n===== SISTEMA DE RESTAURANTE =====")
    print("1 - Cadastrar Item no Cardápio")
    print("2 - Atualizar Item do Cardápio")
    print("3 - Consultar Itens do Cardápio")
    print("4 - Criar Novo Pedido")
    print("5 - Processar Pedidos Pendentes")
    print("6 - Atualizar Status de Pedido")
    print("7 - Cancelar Pedido")
    print("8 - Relatórios")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do item: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Quantidade em estoque: "))
        item = [proximo_codigo_item, nome, descricao, preco, estoque]
        menu.append(item)
        print("Item cadastrado com sucesso! Código:", proximo_codigo_item)
        proximo_codigo_item += 1

    elif opcao == "2":
        codigo = int(input("Código do item a atualizar: "))
        encontrado = False
        for item in menu:
            if item[0] == codigo:
                encontrado = True
                print("Item atual:", item)
                item[1] = input("Novo nome: ")
                item[2] = input("Nova descrição: ")
                item[3] = float(input("Novo preço: "))
                item[4] = int(input("Novo estoque: "))
                print("Item atualizado!")
        if not encontrado:
            print("Item não encontrado.")

    elif opcao == "3":
        if len(menu) == 0:
            print("Nenhum item cadastrado.")
        else:
            print("\n--- CARDÁPIO ---")
            for item in menu:
                print("Código:", item[0], "| Nome:", item[1], "| Preço:", item[3], "| Estoque:", item[4])

    elif opcao == "4":
        if len(menu) == 0:
            print("Nenhum item no cardápio.")
        else:
            cliente = input("Nome do cliente: ")
            itens_pedido = []
            valor_total = 0
            while True:
                codigo = int(input("Digite o código do item (0 para finalizar): "))
                if codigo == 0:
                    break
                quantidade = int(input("Quantidade: "))
                encontrado = False
                for item in menu:
                    if item[0] == codigo:
                        encontrado = True
                        if quantidade <= item[4]:
                            item[4] -= quantidade
                            subtotal = item[3] * quantidade
                            itens_pedido.append([codigo, quantidade, subtotal])
                            valor_total += subtotal
                            print("Item adicionado!")
                        else:
                            print("Estoque insuficiente.")
                if not encontrado:
                    print("Item não encontrado.")
            if len(itens_pedido) > 0:
                pedido = [proximo_codigo_pedido, cliente, itens_pedido, valor_total, "AGUARDANDO APROVACAO"]
                pedidos.append(pedido)
                fila_pendentes.append(pedido)
                print("Pedido criado com sucesso! Código:", proximo_codigo_pedido)
                proximo_codigo_pedido += 1

    elif opcao == "5":
        if len(fila_pendentes) == 0:
            print("Nenhum pedido pendente.")
        else:
            pedido = fila_pendentes.pop(0)
            print("Processando pedido:", pedido[0], "-", pedido[1])
            print("Valor total:", pedido[3])
            acao = input("Aceitar (A) ou Rejeitar (R)? ").upper()
            if acao == "A":
                pedido[4] = "ACEITO"
                fila_aceitos.append(pedido)
                print("Pedido aceito.")
            else:
                pedido[4] = "REJEITADO"
                print("Pedido rejeitado.")

    elif opcao == "6":
        codigo = int(input("Código do pedido: "))
        encontrado = False
        for pedido in pedidos:
            if pedido[0] == codigo:
                encontrado = True
                print("Status atual:", pedido[4])
                novo = input("Novo status: ")
                pedido[4] = novo
                if novo == "FAZENDO":
                    fila_prontos.append(pedido)
                print("Status atualizado!")
        if not encontrado:
            print("Pedido não encontrado.")

    elif opcao == "7":
        codigo = int(input("Código do pedido: "))
        for pedido in pedidos:
            if pedido[0] == codigo:
                if pedido[4] == "AGUARDANDO APROVACAO" or pedido[4] == "ACEITO":
                    pedido[4] = "CANCELADO"
                    print("Pedido cancelado!")
                else:
                    print("Não é possível cancelar este pedido.")
                break
        else:
            print("Pedido não encontrado.")

    elif opcao == "8":
        print("\n--- RELATÓRIOS ---")
        print("Pedidos cadastrados:", len(pedidos))
        print("Pedidos pendentes:", len(fila_pendentes))
        print("Pedidos aceitos:", len(fila_aceitos))
        print("Pedidos prontos:", len(fila_prontos))
        total_vendas = 0
        for pedido in pedidos:
            if pedido[4] == "ENTREGUE":
                total_vendas += pedido[3]
        print("Total em vendas entregues: R$", total_vendas)

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")