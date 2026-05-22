# ==========================================
# ESTRUTURA DE DADOS INICIAL (ETAPA 1)
# ==========================================
# Escolha técnica: Dicionário de dicionários para acesso rápido O(1) por chave.
estoque = {
    "Filtro de Óleo": {
        "quantidade": 15,
        "preco": 45.90
    },
    "Correia Dentada": {
        "quantidade": 8,
        "preco": 120.50
    },
    "Pastilha de Freio": {
        "quantidade": 20,
        "preco": 89.90
    }
}

# ==========================================
# LAÇO PRINCIPAL E MENU INTERATIVO (ETAPA 2)
# ==========================================
while True:
    # Exibição visual do menu com foco em legibilidade e experiência do usuário
    print("\n" + "=" * 30)
    print(" DATACODE SOLUTIONS - ESTOQUE ")
    print("=" * 30)
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    print("=" * 30)

    # Coleta defensiva da opção removendo espaços em branco acidentais
    opcao = input("Escolha uma opção (1-4): ").strip()

    # ==========================================
    # CONTROLE DE FLUXO E REGRAS DE NEGÓCIO
    # ==========================================

    # OPÇÃO 1: Visualização Iterativa do Estoque
    if opcao == "1":
        print("\n" + "-" * 30)
        print("         ESTOQUE ATUAL - OFICINA")
        print("-" * 30)

        for produto, dados in estoque.items():
            print(f"Produto: {produto}")
            print(f"    - Quantidade: {dados['quantidade']} unidades")
            print(f"    - Preço: R$ {dados['preco']:.2f}")
            print("-" * 30)

    # OPÇÃO 2: Registrar Entrada de Produto
    elif opcao == "2":
        print("\n" + "-" * 30)
        print("    REGISTRAR ENTRADA DE PRODUTO")
        print("-" * 30)

        nome_produto = input("Digite o nome exato do produto: ").strip()

        # Validação de segurança: verifica se o produto existe no banco
        if nome_produto in estoque:
            try:
                quantidade_entrada = int(input(f"Digite a quantidade de entrada para '{nome_produto}': "))

                if quantidade_entrada > 0:
                    estoque[nome_produto]['quantidade'] += quantidade_entrada
                    print(f"\n>>> Sucesso! {quantidade_entrada} unidade(s) adicionada(s) ao estoque de '{nome_produto}'.")
                    print(f"Nova quantidade total: {estoque[nome_produto]['quantidade']} unidades.")
                else:
                    print("\n>>> Erro: A quantidade deve ser um número maior que zero.")

            except ValueError:
                print("\n>>> Erro: Digite um número inteiro válido para a quantidade.")
        else:
            print("\n>>> Produto não encontrado.")

    # OPÇÃO 3: Processamento de Saída e Validações Aninhadas
    elif opcao == "3":
        print("\n" + "-" * 30)
        print("    REGISTRAR SAÍDA DE PRODUTO")
        print("-" * 30)

        nome_produto = input("Digite o nome exato do produto para saída: ").strip()

        # 1ª Camada de Validação: Verificação de existência
        if nome_produto in estoque:
            try:
                quantidade_saida = int(input(f"Digite a quantidade de saída para '{nome_produto}': "))

                if quantidade_saida <= 0:
                    print("\n>>> Erro: A quantidade deve ser um número maior que zero.")

                # 2ª Camada de Validação: Verificação de saldo disponível
                elif quantidade_saida <= estoque[nome_produto]['quantidade']:
                    # Dedução segura do estoque
                    estoque[nome_produto]['quantidade'] -= quantidade_saida
                    print(f"\n>>> Sucesso! Saída de {quantidade_saida} unidade(s) realizada com sucesso.")
                    print(f"Saldo atualizado de '{nome_produto}': {estoque[nome_produto]['quantidade']} unidades.")
                else:
                    print("\n>>> Estoque insuficiente.")
                    print(f"Saldo disponível: {estoque[nome_produto]['quantidade']} unidades.")

            except ValueError:
                print("\n>>> Erro: Digite um número inteiro válido para a quantidade.")
        else:
            print("\n>>> Produto não encontrado.")

    # OPÇÃO 4: Encerramento do Sistema
    elif opcao == "4":
        print("\n" + "=" * 30)
        print(" Encerramento solicitado...")
        print(" Obrigado por utilizar o sistema DataCode Solutions!")
        print(" Até a próxima!")
        print("-" * 30 + "\n")
        break

    # Fallback: Opções inválidas
    else:
        print("\n>>> Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
