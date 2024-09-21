# NoSQL (Not Only SQL)

## 1. O que é NoSQL?
**NoSQL** refere-se a um conjunto de sistemas de gerenciamento de banco de dados que não seguem o modelo tradicional de bancos de dados relacionais baseados em tabelas. NoSQL é projetado para lidar com grandes volumes de dados distribuídos, fornecer alta escalabilidade, flexibilidade de dados e suportar tipos de dados não estruturados.

## 2. Características dos Bancos de Dados NoSQL
- **Escalabilidade Horizontal**: Suporta expansão ao distribuir dados entre vários servidores.
- **Flexibilidade de Esquema**: Ao contrário dos bancos de dados relacionais, NoSQL permite armazenar dados sem um esquema fixo, facilitando a mudança do formato dos dados ao longo do tempo.
- **Desempenho em Grande Escala**: Otimizado para grandes volumes de dados e alta taxa de leitura/gravação.
- **Alta Disponibilidade e Particionamento de Dados**: Suporta sistemas distribuídos e tolerância a falhas.
- **Armazenamento de Dados Não Estruturados**: Permite armazenar dados no formato JSON, XML, entre outros, sem seguir uma estrutura de colunas e tabelas.

## 3. Tipos de Bancos de Dados NoSQL
Existem diferentes categorias de bancos de dados NoSQL, cada uma adequada a um tipo específico de necessidade:

### 3.1. Bancos de Dados de Chave-Valor
Esse modelo armazena dados como pares de chave-valor, onde a chave é única e é usada para recuperar o valor associado. É simples, rápido e eficiente para dados não estruturados.

- **Exemplos**: Redis, DynamoDB, Riak.
- **Quando Usar**: Ideal para armazenar cache, sessões de usuário e perfis de usuário.

#### Exemplo de estrutura:
```json
{
  "user123": {
    "nome": "Maria",
    "idade": 29,
    "cidade": "São Paulo"
  }
}
```

### 3.2. Bancos de Dados Orientados a Documentos
Armazenam dados no formato de documentos (geralmente JSON ou BSON). Cada documento pode ter um esquema diferente, proporcionando flexibilidade.

- **Exemplos**: MongoDB, CouchDB, Amazon DocumentDB.
- **Quando Usar**: Aplicações que lidam com dados semiestruturados ou que requerem flexibilidade no esquema (ex: catálogos de produtos, perfis de usuário).

Exemplo de documento JSON:
```json
{
  "_id": "12345",
  "nome": "João",
  "endereço": {
    "cidade": "Rio de Janeiro",
    "estado": "RJ"
  },
  "pedidos": [
    {"id_pedido": 1, "valor": 150},
    {"id_pedido": 2, "valor": 200}
  ]
}
```

### 3.3. Bancos de Dados Orientados a Colunas
Armazenam dados em colunas em vez de linhas. Cada coluna pode ser armazenada e lida de forma independente, o que otimiza consultas de leitura intensiva.

- **Exemplos**: Cassandra, HBase.
- **Quando Usar**: Para grandes volumes de dados com alta taxa de leitura, como logs de eventos e data warehouses.

Exemplo de estrutura de colunas:
```
| ID_Cliente | Nome   | Email            |
|------------|--------|------------------|
| 1          | João   | joao@email.com   |
```

### 3.4. Bancos de Dados Orientados a Grafos
São projetados para armazenar e navegar em relacionamentos complexos entre dados. As entidades são representadas como nós, e os relacionamentos entre elas são armazenados como arestas.

- **Exemplos**: Neo4j, ArangoDB, Amazon Neptune.
- **Quando Usar**: Para modelagem de redes sociais, sistemas de recomendação, detecção de fraudes e análise de redes.

Exemplo de Grafo:
- **Nós**: Pessoa (João), Pessoa (Maria)
- **Arestas**: João é amigo de Maria

## 4. Vantagens do NoSQL
- **Escalabilidade Horizontal**: Capacidade de adicionar mais servidores (escalar "horizontalmente") para lidar com o aumento de dados.
- **Alto Desempenho**: Projetado para lidar com grandes volumes de leitura e gravação, especialmente em sistemas distribuídos.
- **Flexibilidade**: Não requer um esquema fixo, permitindo o armazenamento de dados de diferentes tipos sem alterações estruturais.
- **Tolerância a Falhas**: Sistemas NoSQL são projetados para operar de forma eficaz em ambientes distribuídos e de alta disponibilidade.

## 5. Desvantagens do NoSQL
- **Consistência**: Muitos sistemas NoSQL seguem o modelo CAP (Consistência, Disponibilidade e Tolerância à Partição), sacrificando a consistência em favor da disponibilidade e partição.
- **Suporte a Transações**: Bancos de dados NoSQL geralmente têm suporte limitado para transações ACID, embora alguns tenham começado a oferecer mais recursos transacionais.
- **Falta de Padronização**: Diferentes sistemas NoSQL podem ter APIs e funcionalidades muito distintas, dificultando a portabilidade entre eles.
- **Complexidade de Consultas**: Consultas complexas como JOINs e GROUP BY podem não ser tão eficientes ou suportadas como em bancos de dados relacionais.

## 6. Quando Usar NoSQL?
- **Grandes volumes de dados**: NoSQL é ideal para aplicações que gerenciam grandes volumes de dados distribuídos.
- **Dados semiestruturados ou não estruturados**: Se você precisa armazenar dados que mudam frequentemente de formato, ou que não se encaixam bem em um esquema de tabela rígido.
- **Alta taxa de leitura/escrita**: Aplicações com muitos usuários simultâneos que exigem alta taxa de leitura e escrita.
- **Escalabilidade**: Quando é necessário escalar horizontalmente e distribuir dados em vários servidores.

## 7. Exemplos de Casos de Uso de NoSQL
- **Redes sociais**: Para modelagem de relacionamentos complexos e recomendações personalizadas.
- **E-commerce**: Armazenamento de catálogos de produtos que variam em atributos.
- **Aplicações em tempo real**: Sistemas de recomendação, chats, sistemas de monitoramento e análise de eventos.
- **Data Lakes**: Armazenamento de grandes volumes de dados sem estrutura definida para análise posterior.

---

Esse resumo cobre os principais conceitos de bancos de dados NoSQL, os tipos mais comuns e suas vantagens e desvantagens.