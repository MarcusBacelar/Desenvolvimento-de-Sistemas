import sqlite3

# ==============================
# Função para criar o banco/tabela
# ==============================
def criar_banco():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

# ==============================
# Funções CRUD
# ==============================

def adicionar_produto(nome, quantidade, preco):
    try:
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
                       (nome, quantidade, preco))
        conexao.commit()
        print(f"Produto '{nome}' adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Já existe um produto com esse nome!")
    finally:
        conexao.close()


def listar_produtos():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    if produtos:
        print("\nEstoque Atual:")
        print("-" * 40)
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Quantidade: {p[2]} | Preço: R${p[3]:.2f}")
        print("-" * 40)
    else:
        print("\nNenhum produto cadastrado.")


def atualizar_produto(id_produto, nova_quantidade, novo_preco):
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    if cursor.fetchone():
        cursor.execute("UPDATE produtos SET quantidade = ?, preco = ? WHERE id = ?",
                       (nova_quantidade, novo_preco, id_produto))
        conexao.commit()
        print("Produto atualizado com sucesso!")
    else:
        print("Erro: Produto não encontrado!")
    conexao.close()


def deletar_produto(id_produto):
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conexao.commit()
        print("Produto deletado com sucesso!")
    else:
        print("Erro: Produto não encontrado!")
    conexao.close()

# ==============================
# Menu interativo
# ==============================

def menu():
    criar_banco()
    while True:
        print("\n===== MENU ESTOQUE =====")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            try:
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço: "))
                adicionar_produto(nome, quantidade, preco)
            except ValueError:
                print("⚠️ Quantidade deve ser número inteiro e preço deve ser número real.")

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            try:
                id_produto = int(input("ID do produto a atualizar: "))
                nova_quantidade = int(input("Nova quantidade: "))
                novo_preco = float(input("Novo preço: "))
                atualizar_produto(id_produto, nova_quantidade, novo_preco)
            except ValueError:
                print("Valores inválidos! Digite números corretamente.")

        elif opcao == "4":
            try:
                id_produto = int(input("ID do produto a deletar: "))
                deletar_produto(id_produto)
            except ValueError:
                print("ID inválido!")

        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# ==============================
# Executar programa
# ==============================
if __name__ == "__main__":
    menu()
