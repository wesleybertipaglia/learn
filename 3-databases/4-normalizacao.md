# Normalização e Denormalização

## 1. O que é Normalização?
A **normalização** é o processo de organizar os dados em um banco de dados para minimizar a redundância e evitar anomalias de inserção, atualização e exclusão. O objetivo é garantir a integridade dos dados, eliminando a duplicação de informações e estruturando os dados em tabelas menores, com relacionamentos bem definidos.

### 1.1. Formas Normais
As formas normais são níveis de normalização que seguem regras progressivamente mais rígidas. Cada nível corrige diferentes tipos de problemas de organização de dados.

#### 1.1.1. Primeira Forma Normal (1NF)
- **Regra**: Elimina grupos repetidos de dados e garante que cada célula contém um valor único (dados atômicos).
- **Exemplo**: Separar dados combinados, como múltiplos números de telefone em uma única célula, em várias linhas ou colunas distintas.

#### 1.1.2. Segunda Forma Normal (2NF)
- **Regra**: Satisfaz a 1NF e garante que todos os atributos dependem totalmente da chave primária (não pode haver dependência parcial).
- **Exemplo**: Mover atributos que não dependem exclusivamente da chave primária para uma tabela separada.

#### 1.1.3. Terceira Forma Normal (3NF)
- **Regra**: Satisfaz a 2NF e remove dependências transitivas, ou seja, quando um atributo não chave depende de outro atributo que não é chave primária.
- **Exemplo**: Se em uma tabela de pedidos, o endereço do cliente depende da identificação do cliente (e não do pedido), deve-se criar uma tabela separada para os clientes.

### 1.2. Benefícios da Normalização
- **Redução de Redundância**: Evita a duplicação desnecessária de dados.
- **Melhoria da Integridade dos Dados**: Assegura que as alterações em dados relacionados são consistentes.
- **Facilidade de Manutenção**: Atualizações e exclusões tornam-se mais fáceis, minimizando anomalias.

## 2. O que é Denormalização?
A **denormalização** é o processo oposto à normalização, em que dados são deliberadamente duplicados e combinados para melhorar o desempenho de consultas. Enquanto a normalização visa à eficiência de armazenamento e integridade dos dados, a denormalização busca otimizar a leitura dos dados, reduzindo o número de junções (joins) em consultas complexas.

### 2.1. Quando Usar Denormalização?
A denormalização é útil em sistemas onde a leitura de dados é mais frequente e o desempenho de consultas precisa ser otimizado. Exemplos incluem sistemas de análise, data warehouses e aplicações com grandes volumes de leitura.

### 2.2. Técnicas de Denormalização
- **Adicionar colunas calculadas**: Colunas que armazenam resultados de cálculos frequentemente usados, evitando que sejam recalculados em tempo de execução.
- **Duplicação de dados**: Armazenar informações que normalmente estariam em tabelas separadas em uma única tabela para evitar o uso de `JOIN`.
- **Tabelas agregadas**: Criar tabelas contendo dados agregados (ex: totais, médias) para otimizar relatórios e consultas analíticas.

### 2.3. Benefícios da Denormalização
- **Melhoria no Desempenho**: Reduz o número de junções (joins) necessários em consultas complexas, tornando-as mais rápidas.
- **Facilidade de Consulta**: Consultas se tornam mais simples, já que os dados necessários estão em uma única tabela.

### 2.4. Desvantagens da Denormalização
- **Aumento da Redundância**: Duplicação de dados pode levar a inconsistência se os dados não forem atualizados corretamente.
- **Dificuldade de Manutenção**: Mudanças nos dados podem exigir atualizações em várias tabelas.

## 3. Comparação entre Normalização e Denormalização

| **Critério**          | **Normalização**                            | **Denormalização**                        |
|-----------------------|---------------------------------------------|-------------------------------------------|
| **Objetivo**          | Minimizar redundância, melhorar integridade | Melhorar o desempenho de leitura          |
| **Estrutura**         | Dados divididos em várias tabelas           | Dados combinados em tabelas maiores       |
| **Vantagem Principal**| Reduzir inconsistências e anomalias         | Reduzir o tempo de consulta               |
| **Desvantagem Principal** | Dificulta consultas complexas            | Aumenta a redundância e pode gerar inconsistências |
| **Aplicação**         | Sistemas transacionais (OLTP)               | Sistemas analíticos (OLAP) ou com leitura intensiva |

---

Esse resumo cobre os principais pontos de normalização e denormalização, além de suas vantagens e desvantagens.
