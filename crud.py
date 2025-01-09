import json

inventario = {}
proximo_id = 1  

def salvar_dados():
    with open("inventario.json", "w") as arquivo:
        json.dump(inventario, arquivo, indent=4)

def carregar_dados():
    global proximo_id
    try:
        with open("inventario.json", "r") as arquivo:
            dados = json.load(arquivo)
            if dados:
                global inventario
                inventario = dados
                proximo_id = max(map(int, inventario.keys())) + 1
    except FileNotFoundError:
        pass

def adicionar_produto():
    global proximo_id
    print("\n--- Adicionar Produto ---")
    nome = input("Nome do Produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade em Estoque: "))
    preco = float(input("Preço: "))

    produto = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco
    }
    inventario[proximo_id] = produto
    print(f"\nProduto adicionado com sucesso! ID atribuído: {proximo_id}")
    proximo_id += 1
    salvar_dados()

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if not inventario:
        print("Inventário vazio.")
        return

    print("{:<5} {:<20} {:<15} {:<10} {:<10}".format("ID", "Nome", "Categoria", "Quantidade", "Preço (R$)"))
    print("-" * 60)
    for id, produto in inventario.items():
        print("{:<5} {:<20} {:<15} {:<10} {:<10.2f}".format(id, produto["nome"], produto["categoria"], produto["quantidade"], produto["preco"]))

def buscar_produto():
    print("\n--- Buscar Produto ---")
    criterio = input("Buscar por (id/nome): ").strip().lower()
    if criterio == "id":
        id = int(input("ID do Produto: "))
        produto = inventario.get(id)
        if produto:
            print(f"\nProduto encontrado: {produto}")
        else:
            print("\nProduto não encontrado.")
    elif criterio == "nome":
        nome = input("Parte do Nome: ").strip().lower()
        encontrados = [p for p in inventario.values() if nome in p["nome"].lower()]
        if encontrados:
            print("\nProdutos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("\nNenhum produto encontrado.")
    else:
        print("\nCritério inválido.")

def atualizar_produto():
    print("\n--- Atualizar Produto ---")
    id = int(input("ID do Produto a atualizar: "))
    produto = inventario.get(id)
    if not produto:
        print("\nProduto não encontrado.")
        return

    print("\nDeixe o campo vazio para não alterar o valor atual.")
    nome = input(f"Novo Nome ({produto['nome']}): ").strip() or produto["nome"]
    categoria = input(f"Nova Categoria ({produto['categoria']}): ").strip() or produto["categoria"]
    quantidade = input(f"Nova Quantidade ({produto['quantidade']}): ").strip()
    preco = input(f"Novo Preço ({produto['preco']}): ").strip()

    produto["nome"] = nome
    produto["categoria"] = categoria
    produto["quantidade"] = int(quantidade) if quantidade else produto["quantidade"]
    produto["preco"] = float(preco) if preco else produto["preco"]
    print("\nProduto atualizado com sucesso!")
    salvar_dados()

def excluir_produto():
    print("\n--- Excluir Produto ---")
    id = int(input("ID do Produto a excluir: "))
    if id in inventario:
        confirmacao = input("Tem certeza que deseja excluir este produto? (s/n): ").strip().lower()
        if confirmacao == "s":
            del inventario[id]
            print("\nProduto excluído com sucesso!")
            salvar_dados()
        else:
            print("\nOperação cancelada.")
    else:
        print("\nProduto não encontrado.")

def menu():
    carregar_dados()
    while True:
        print("\n========================================")
        print("  Gerenciamento de Produtos - AgilStore  ")
        print("========================================")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Buscar Produto")
        print("4. Atualizar Produto")
        print("5. Excluir Produto")
        print("6. Sair")
        print("========================================")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            atualizar_produto()
        elif opcao == "5":
            excluir_produto()
        elif opcao == "6":
            print("\nSaindo... Obrigado por usar a AgilStore!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
