📦 CRUD com SQLite – Sistema de Gerenciamento de Estoque
🎯 Objetivo

Este projeto tem como finalidade aplicar os conceitos de SQLite e operações CRUD (Create, Read, Update, Delete) para construir um sistema simples de gerenciamento de estoque utilizando Python.

📝 Descrição da Atividade

O sistema foi desenvolvido para gerenciar um estoque de produtos, permitindo:

Criar e gerenciar o banco de dados em SQLite;

Adicionar novos produtos ao estoque;

Listar os produtos cadastrados;

Atualizar informações como quantidade e preço;

Excluir produtos pelo ID.

🗄️ Estrutura do Banco de Dados

Tabela: Produtos

Campo	Tipo	Descrição
id	INTEGER	Chave primária, auto incremento
nome	TEXT	Nome do produto (único e obrigatório)
quantidade	INTEGER	Quantidade em estoque (obrigatório)
preco	REAL	Preço do produto (obrigatório)
⚙️ Funcionalidades CRUD

C (Create): Adicionar novo produto.

R (Read): Listar todos os produtos.

U (Update): Alterar quantidade e preço de um produto existente.

D (Delete): Remover produto pelo ID.

🔄 Fluxo do Sistema

O banco de dados é criado automaticamente ao iniciar o programa.

O usuário acessa o menu interativo no terminal.

Escolhe a operação desejada (Adicionar, Listar, Atualizar, Deletar).

O sistema executa a operação e retorna o resultado.

O menu permanece em loop até a escolha da opção "Sair".

🛠️ Tratamento de Erros

Impede cadastro de nomes duplicados.

Verifica se o ID existe antes de atualizar ou deletar.

Valida entradas de dados (quantidade como inteiro, preço como real).

Uso de try/except para evitar falhas durante a execução.

📌 Exemplos de Uso

Adicionar:

Produto: Arroz | Quantidade: 10 | Preço: 5.50


Listar:

ID: 1 | Nome: Arroz | Quantidade: 10 | Preço: R$5.50


Atualizar:

Quantidade: 15 | Preço: 6.00


Deletar:

Produto ID 1 removido com sucesso

🚧 Desafios Encontrados

Modelagem do Banco: Definição correta dos tipos e unicidade do campo nome.

Integração Python + SQLite: Uso do módulo sqlite3 e boas práticas de conexão.

Tratamento de Erros: Evitar falhas em inserções duplicadas ou IDs inexistentes.

Menu Interativo: Construção de um loop amigável e intuitivo.

Organização do Código: Modularização das funções para manter legibilidade.

✅ Como os Desafios Foram Superados

Uso de try/except para capturar exceções.

Testes individuais de cada função antes da integração.

Consulta à documentação oficial e exemplos práticos em Python.

Divisão do código em módulos menores e reutilizáveis.

🏁 Conclusão

O projeto demonstrou, de forma prática, o funcionamento de operações CRUD com Python e SQLite.
Foi possível desenvolver um sistema funcional, modular e reutilizável, com criação automática do banco e aplicação de boas práticas de programação.

👨‍💻 Autores

João Francisco Torres

Kayky Ferreira

Marcus Vinícius R. Bacelar
