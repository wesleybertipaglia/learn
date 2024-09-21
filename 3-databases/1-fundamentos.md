# Fundamentos de Bancos de Dados

## 1. O que é um Banco de Dados?
Um banco de dados é uma coleção organizada de dados que pode ser acessada, gerenciada e atualizada. Ele permite o armazenamento estruturado de informações para que possam ser recuperadas e manipuladas facilmente.

## 2. Tipos de Bancos de Dados
- **Bancos de Dados Relacionais (SQL):** Estruturados em tabelas com linhas e colunas. Ex: MySQL, PostgreSQL.
- **Bancos de Dados Não Relacionais (NoSQL):** Projetados para lidar com grandes volumes de dados não estruturados. Ex: MongoDB, Cassandra.

## 3. Conceitos Básicos
- **Tabelas:** estruturas principais em bancos de dados relacionais, compostas por linhas (registros) e colunas (atributos).

- **Chave Primária (Primary Key):** um ou mais campos que identificam unicamente um registro em uma tabela.

- **Chave Estrangeira (Foreign Key):** um campo que cria um relacionamento entre duas tabelas, referenciando a chave primária de outra tabela.

- **Índices:** estruturas que aceleram a recuperação de dados, permitindo buscas mais rápidas.

- **Consultas (Queries):** solicitações feitas a um banco de dados para buscar ou manipular dados. Em bancos relacionais, a linguagem SQL (Structured Query Language) é usada.

## 4. Modelagem de Dados
A modelagem de dados envolve a criação de um **modelo de dados** que representa a estrutura lógica dos dados. Isso inclui:
- **Diagrama Entidade-Relacionamento (ERD)**: Um modelo visual que descreve como os dados estão relacionados.
- **Normalização**: Processo de organizar os dados para reduzir a redundância e melhorar a integridade dos dados.

## 5. Normalização
- **1ª Forma Normal (1NF)**: Elimina duplicação de colunas e cria tabelas separadas para grupos de dados relacionados.
- **2ª Forma Normal (2NF)**: Garante que todos os atributos dependem totalmente da chave primária.
- **3ª Forma Normal (3NF)**: Remove dependências transitivas (quando um campo depende de outro campo que não é chave primária).

## 6. ACID (Propriedades das Transações)
1. **Atomicidade**: As transações são "tudo ou nada" (completam-se completamente ou falham completamente).
2. **Consistência**: Assegura que a transação leva o banco de dados de um estado válido para outro estado válido.
3. **Isolamento**: Transações simultâneas não interferem umas nas outras.
4. **Durabilidade**: Após a confirmação, os dados persistem no banco de dados, mesmo em caso de falha.

## 7. SQL Básico
### 7.1. Comandos de Manipulação de Dados (DML)
- `SELECT`: Consulta dados.
- `INSERT`: Insere dados em uma tabela.
- `UPDATE`: Atualiza dados existentes.
- `DELETE`: Remove dados de uma tabela.

### 7.2. Comandos de Definição de Dados (DDL)
- `CREATE`: Cria novas tabelas ou objetos.
- `ALTER`: Modifica a estrutura de tabelas.
- `DROP`: Remove tabelas ou objetos do banco de dados.

### 7.3. Comandos de Controle de Transação (TCL)
- `COMMIT`: Confirma uma transação.
- `ROLLBACK`: Reverte uma transação.

### 7.4. Comandos de Controle de Acesso (DCL)
- `GRANT`: Concede privilégios a usuários.
- `REVOKE`: Revoga privilégios de usuários.

### 7.5. Funções Agregadas
- `COUNT()`: Conta o número de linhas.
- `SUM()`: Soma os valores de uma coluna.
- `AVG()`: Calcula a média dos valores de uma coluna.
- `MAX()`: Retorna o maior valor de uma coluna.
- `MIN()`: Retorna o menor valor de uma coluna.

### 7.6. Cláusulas SQL
- `WHERE`: Filtra os resultados.
- `ORDER BY`: Ordena os resultados.
- `GROUP BY`: Agrupa os resultados.
- `HAVING`: Filtra os resultados de grupos.
- `JOIN`: Combina dados de duas ou mais tabelas.

## 8. NoSQL
Os bancos de dados NoSQL são projetados para trabalhar com grandes volumes de dados não estruturados ou semi-estruturados. Existem quatro categorias principais:
- **Documentos**: Armazenam dados no formato de documentos (JSON, BSON). Ex: MongoDB.
- **Chave-Valor**: Dados armazenados como pares de chave-valor. Ex: Redis.
- **Colunar**: Armazena dados em colunas, otimizando grandes volumes de dados. Ex: Cassandra.
- **Grafos**: Otimiza a representação de redes e relacionamentos. Ex: Neo4j.

## 9. Ferramentas de Gerenciamento de Bancos de Dados (SGBD)
Um Sistema de Gerenciamento de Banco de Dados (SGBD) é um software que permite criar, gerenciar e manipular bancos de dados.
- **Exemplos de SGBDs Relacionais**: MySQL, PostgreSQL, Oracle, SQL Server.
- **Exemplos de SGBDs NoSQL**: MongoDB, CouchDB, Cassandra.

## 10. Segurança de Bancos de Dados
Inclui técnicas para garantir que os dados sejam protegidos contra acessos não autorizados. Algumas práticas incluem:
- **Autenticação**: Verificar a identidade de usuários.
- **Autorização**: Controlar o nível de acesso dos usuários.
- **Criptografia**: Proteger os dados em repouso e em trânsito.

## 11. Backup e Recuperação
Estratégias de **backup** e **recuperação** são essenciais para garantir que os dados possam ser restaurados em caso de perda ou falha.
- **Backup Completo**: Cópia de todo o banco de dados.
- **Backup Incremental**: Cópia das alterações feitas desde o último backup.

## 12. Replicação
A replicação é o processo de copiar e manter sincronizados múltiplos bancos de dados em diferentes servidores. Pode ser usada para melhorar a disponibilidade e a escalabilidade.

---

Este é um resumo dos conceitos fundamentais de bancos de dados. Cada tópico pode ser aprofundado para entender melhor o funcionamento de um sistema de banco de dados.
