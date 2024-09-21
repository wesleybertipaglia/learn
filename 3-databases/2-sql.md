# SQL (Structured Query Language)

## 1. O que é SQL?
O **SQL** (Structured Query Language) é uma linguagem padrão usada para gerenciar e manipular bancos de dados relacionais. Ela permite executar comandos para criar, modificar, consultar e controlar o acesso a dados em um banco de dados.

## 2. Categorias de Comandos SQL
Os comandos SQL podem ser classificados em várias categorias, dependendo da finalidade:

### 2.1. DML (Data Manipulation Language)
Comandos usados para manipulação de dados, ou seja, inserir, atualizar, excluir e consultar dados em tabelas.

- **`SELECT`**: Recupera dados de uma tabela.
  - Exemplo: `SELECT * FROM Clientes;`
- **`INSERT`**: Insere novos dados em uma tabela.
  - Exemplo: `INSERT INTO Clientes (Nome, Email) VALUES ('João', 'joao@email.com');`
- **`UPDATE`**: Atualiza dados existentes em uma tabela.
  - Exemplo: `UPDATE Clientes SET Email = 'joao@novoemail.com' WHERE ID_Cliente = 1;`
- **`DELETE`**: Exclui dados de uma tabela.
  - Exemplo: `DELETE FROM Clientes WHERE ID_Cliente = 1;`

### 2.2. DDL (Data Definition Language)
Comandos usados para definir ou modificar a estrutura de bancos de dados e tabelas.

- **`CREATE`**: Cria novas tabelas, bancos de dados, índices ou outros objetos.
  - Exemplo: `CREATE TABLE Clientes (ID_Cliente INT PRIMARY KEY, Nome VARCHAR(100), Email VARCHAR(100));`
- **`ALTER`**: Modifica a estrutura de uma tabela existente (ex: adicionar ou remover colunas).
  - Exemplo: `ALTER TABLE Clientes ADD Telefone VARCHAR(15);`
- **`DROP`**: Remove uma tabela, banco de dados ou outro objeto.
  - Exemplo: `DROP TABLE Clientes;`

### 2.3. DCL (Data Control Language)
Comandos usados para controlar o acesso e as permissões de usuários no banco de dados.

- **`GRANT`**: Concede permissões a usuários.
  - Exemplo: `GRANT SELECT, INSERT ON Clientes TO Usuario;`
- **`REVOKE`**: Revoga permissões de usuários.
  - Exemplo: `REVOKE INSERT ON Clientes FROM Usuario;`

### 2.4. TCL (Transaction Control Language)
Comandos usados para gerenciar transações no banco de dados, garantindo a consistência dos dados.

- **`COMMIT`**: Confirma as alterações feitas na transação.
  - Exemplo: `COMMIT;`
- **`ROLLBACK`**: Desfaz as alterações feitas durante a transação.
  - Exemplo: `ROLLBACK;`
- **`SAVEPOINT`**: Define um ponto na transação para que você possa fazer um rollback parcial.
  - Exemplo: `SAVEPOINT ponto1;`

## 3. Claúsulas SQL Comuns
SQL oferece várias cláusulas que podem ser usadas para modificar consultas `SELECT` e outras operações. Algumas das mais importantes são:

### 3.1. `WHERE`
Filtra registros com base em uma condição específica.
- Exemplo: `SELECT * FROM Clientes WHERE Cidade = 'São Paulo';`

### 3.2. `ORDER BY`
Ordena os resultados com base em uma ou mais colunas.
- Exemplo: `SELECT * FROM Clientes ORDER BY Nome ASC;`

### 3.3. `GROUP BY`
Agrupa os registros com base em uma ou mais colunas e geralmente é usado com funções de agregação (como `COUNT`, `SUM`, `AVG`).
- Exemplo: `SELECT Cidade, COUNT(*) FROM Clientes GROUP BY Cidade;`

### 3.4. `HAVING`
Filtra os grupos criados pela cláusula `GROUP BY` com base em uma condição.
- Exemplo: `SELECT Cidade, COUNT(*) FROM Clientes GROUP BY Cidade HAVING COUNT(*) > 5;`

### 3.5. `JOIN`
Combina dados de duas ou mais tabelas com base em uma condição. Existem vários tipos de joins:
- **`INNER JOIN`**: Retorna registros que têm correspondências nas duas tabelas.
  - Exemplo: `SELECT Clientes.Nome, Pedidos.ID_Pedido FROM Clientes INNER JOIN Pedidos ON Clientes.ID_Cliente = Pedidos.ID_Cliente;`
- **`LEFT JOIN`**: Retorna todos os registros da tabela à esquerda e os correspondentes da tabela à direita. Se não houver correspondência, retorna `NULL`.
  - Exemplo: `SELECT Clientes.Nome, Pedidos.ID_Pedido FROM Clientes LEFT JOIN Pedidos ON Clientes.ID_Cliente = Pedidos.ID_Cliente;`
- **`RIGHT JOIN`**: Retorna todos os registros da tabela à direita e os correspondentes da tabela à esquerda.
  - Exemplo: `SELECT Clientes.Nome, Pedidos.ID_Pedido FROM Clientes RIGHT JOIN Pedidos ON Clientes.ID_Cliente = Pedidos.ID_Cliente;`

## 4. Funções de Agregação
As funções de agregação realizam cálculos em um conjunto de valores e retornam um único valor.

- **`COUNT()`**: Conta o número de linhas.
  - Exemplo: `SELECT COUNT(*) FROM Clientes;`
- **`SUM()`**: Soma os valores de uma coluna numérica.
  - Exemplo: `SELECT SUM(Preco) FROM Produtos;`
- **`AVG()`**: Calcula a média dos valores de uma coluna numérica.
  - Exemplo: `SELECT AVG(Preco) FROM Produtos;`
- **`MAX()`**: Retorna o valor máximo de uma coluna.
  - Exemplo: `SELECT MAX(Preco) FROM Produtos;`
- **`MIN()`**: Retorna o valor mínimo de uma coluna.
  - Exemplo: `SELECT MIN(Preco) FROM Produtos;`

## 5. Subconsultas
As **subconsultas** são consultas aninhadas dentro de outra consulta SQL. Elas podem ser usadas em várias cláusulas, como `WHERE`, `FROM`, ou `SELECT`.

- **Exemplo**: `SELECT Nome FROM Clientes WHERE ID_Cliente IN (SELECT ID_Cliente FROM Pedidos WHERE Valor > 1000);`

## 6. Índices
**Índices** são usados para acelerar a recuperação de dados em uma tabela, permitindo que o banco de dados localize dados mais rapidamente.

- **Criando um Índice**: `CREATE INDEX idx_nome ON Clientes(Nome);`
- **Removendo um Índice**: `DROP INDEX idx_nome;`

## 7. Vistas (Views)
Uma **vista** é uma tabela virtual baseada no resultado de uma consulta SQL. Vistas são usadas para simplificar consultas complexas, melhorar a segurança e reduzir a complexidade de manutenção.

- **Criando uma Vista**: `CREATE VIEW vista_clientes_pedidos AS SELECT Clientes.Nome, Pedidos.Data FROM Clientes INNER JOIN Pedidos ON Clientes.ID_Cliente = Pedidos.ID_Cliente;`
- **Consultando uma Vista**: `SELECT * FROM vista_clientes_pedidos;`
- **Removendo uma Vista**: `DROP VIEW vista_clientes_pedidos;`

## 8. Procedimentos Armazenados e Funções
**Procedimentos Armazenados** são blocos de código SQL que podem ser armazenados e executados no servidor do banco de dados.

- **Procedimento**: 
```sql
-- criando um procedimento
CREATE PROCEDURE AtualizaEstoque(IN produto_id INT, IN quantidade INT)
BEGIN
    UPDATE Produtos SET Estoque = Estoque + quantidade WHERE ID_Produto = produto_id;
END;

-- chamando um procedimento
CALL AtualizaEstoque(1, 10);
```

- **Funções** são blocos de código SQL que retornam um valor.

```sql
-- criando uma função
CREATE FUNCTION CalculaDesconto(preco DECIMAL(10,2), desconto DECIMAL(4,2))
RETURNS DECIMAL(10,2)

BEGIN
    DECLARE valor_desconto DECIMAL(10,2);
    SET valor_desconto = preco * (desconto / 100);
    RETURN preco - valor_desconto;
END;

-- chamando uma função
SELECT CalculaDesconto(100, 10);
```

## 9. Transações

Uma transação é um conjunto de operações SQL que deve ser executado como uma única unidade lógica. As propriedades ACID (Atomicidade, Consistência, Isolamento, Durabilidade) garantem a confiabilidade das transações.

- Iniciando uma Transação: `START TRANSACTION;`
- Confirmando uma Transação: `COMMIT;`
- Desfazendo uma Transação: `ROLLBACK;`

---

Esse resumo cobre os principais conceitos e comandos SQL, fornecendo uma base sólida para a manipulação de bancos de dados relacionais.