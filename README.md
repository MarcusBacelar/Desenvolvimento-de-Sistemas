# 📦 CRUD com SQLite – Sistema de Gerenciamento de Estoque  

## 🎯 Objetivo  
Este projeto tem como finalidade aplicar os conceitos de **SQLite** e operações **CRUD (Create, Read, Update, Delete)** para construir um sistema simples de gerenciamento de estoque utilizando **Python**.  

---

## 📝 Descrição da Atividade  
O sistema foi desenvolvido para gerenciar um estoque de produtos, permitindo:  
- Criar e gerenciar o banco de dados em SQLite;  
- Adicionar novos produtos ao estoque;  
- Listar os produtos cadastrados;  
- Atualizar informações como quantidade e preço;  
- Excluir produtos pelo ID.  

---

## 🗄️ Estrutura do Banco de Dados  
**Tabela: Produtos**  

| Campo       | Tipo      | Descrição                              |  
|-------------|-----------|----------------------------------------|  
| `id`        | INTEGER   | Chave primária, auto incremento        |  
| `nome`      | TEXT      | Nome do produto (único e obrigatório) |  
| `quantidade`| INTEGER   | Quantidade em estoque (obrigatório)    |  
| `preco`     | REAL      | Preço do produto (obrigatório)         |  

---

## ⚙️ Funcionalidades CRUD  
- **C (Create):** Adicionar novo produto.  
- **R (Read):** Listar todos os produtos.  
- **U (Update):** Alterar quantidade e preço de um produto existente.  
- **D (Delete):** Remover produto pelo ID.  

---

## 🔄 Fluxo do Sistema  
1. O banco de dados é criado automaticamente ao iniciar o programa.  
2. O usuário acessa o **menu interativo** no terminal.  
3. Escolhe a operação desejada (Adicionar, Listar, Atualizar, Deletar).  
4. O sistema executa a operação e retorna o resultado.  
5. O menu permanece em loop até a escolha da opção "Sair".  

---

## 🛠️ Tratamento de Erros  
- Impede cadastro de nomes duplicados.  
- Verifica se o **ID** existe antes de atualizar ou deletar.  
- Valida entradas de dados (quantidade como inteiro, preço como real).  
- Uso de **try/except** para evitar falhas durante a execução.  

---

## 📌 Exemplos de Uso  
- **Adicionar:**  
  ```text
  Produto: Arroz | Quantidade: 10 | Preço: 5.50
