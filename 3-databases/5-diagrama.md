# Diagramas de Entidade-Relacionamento (ERD)

## 1. O que é um Diagrama de Entidade-Relacionamento (ERD)?
Um **Diagrama de Entidade-Relacionamento (ERD)** é uma representação visual que modela a estrutura lógica de um banco de dados. Ele descreve as entidades do sistema, seus atributos, e os relacionamentos entre elas, ajudando a projetar ou entender a organização dos dados.

## 2. Elementos de um Diagrama ER
Os principais componentes de um diagrama ER são:

### 2.1. Entidades
As **entidades** representam objetos ou conceitos sobre os quais informações são armazenadas no banco de dados. Cada entidade se torna uma tabela no banco de dados relacional.
- **Exemplo**: Cliente, Pedido, Produto.

#### 2.1.1. Tipos de Entidades
- **Entidades Fortes**: Existem de forma independente e possuem chave primária própria.
  - Exemplo: Cliente.
- **Entidades Fracas**: Dependem de outra entidade para existir e não possuem chave primária própria.
  - Exemplo: Detalhes do Pedido (depende do Pedido).

### 2.2. Atributos
Os **atributos** são as propriedades ou características das entidades. Cada atributo se torna uma coluna na tabela correspondente à entidade.
- **Exemplo**: Nome (para Cliente), Preço (para Produto).

#### 2.2.1. Tipos de Atributos
- **Atributo Simples**: Contém um único valor atômico.
  - Exemplo: `Nome`.
- **Atributo Composto**: Pode ser subdividido em vários atributos menores.
  - Exemplo: `Endereço` (que pode ser dividido em Rua, Cidade, CEP).
- **Atributo Multivalorado**: Pode conter mais de um valor.
  - Exemplo: `Telefones` (um cliente pode ter mais de um número de telefone).
- **Atributo Derivado**: Um atributo que pode ser calculado a partir de outros atributos.
  - Exemplo: `Idade`, derivado da data de nascimento.

### 2.3. Relacionamentos
Os **relacionamentos** descrevem como as entidades estão associadas entre si. Eles indicam as conexões entre duas ou mais entidades.
- **Exemplo**: Um Cliente faz um Pedido.

#### 2.3.1. Tipos de Relacionamentos
- **1:1 (Um para Um)**: Uma entidade A está associada a, no máximo, uma entidade B, e vice-versa.
  - Exemplo: Cada pessoa tem um número de identidade único.
- **1:N (Um para Muitos)**: Uma entidade A pode estar associada a várias entidades B, mas uma entidade B só pode estar associada a uma entidade A.
  - Exemplo: Um Cliente pode fazer vários Pedidos, mas cada Pedido pertence a apenas um Cliente.
- **N:M (Muitos para Muitos)**: Uma entidade A pode estar associada a várias entidades B, e vice-versa.
  - Exemplo: Um Aluno pode estar inscrito em vários Cursos, e um Curso pode ter vários Alunos.

### 2.4. Cardinalidade
A **cardinalidade** de um relacionamento indica o número de instâncias de uma entidade que podem estar relacionadas a instâncias de outra entidade. Os três principais tipos de cardinalidade são:
- **1:1** (um para um).
- **1:N** (um para muitos).
- **N:M** (muitos para muitos).

### 2.5. Chaves
As **chaves** são atributos que identificam de forma única uma entidade ou relacionam uma entidade com outra.

#### 2.5.1. Chave Primária (PK)
Um atributo (ou conjunto de atributos) que identifica de forma única cada instância de uma entidade.
- **Exemplo**: `ID_Cliente` como chave primária para a entidade Cliente.

#### 2.5.2. Chave Estrangeira (FK)
Um atributo em uma entidade que referencia a chave primária de outra entidade, estabelecendo um relacionamento entre as duas.
- **Exemplo**: `ID_Cliente` como chave estrangeira na tabela de Pedido, referenciando a tabela de Cliente.

## 3. Notações em Diagramas ER
Existem várias notações usadas em diagramas ER para representar entidades, atributos e relacionamentos. As mais comuns incluem:

- **Retângulos**: Representam entidades.
- **Elipses**: Representam atributos.
- **Diamantes**: Representam relacionamentos entre entidades.
- **Linhas**: Conectam entidades e relacionamentos, geralmente marcadas com a cardinalidade.

### Notações Populares
- **Notação de Chen**: Uma das mais tradicionais, com elipses para atributos e diamantes para relacionamentos.
- **Notação de Crow’s Foot**: Usa “pés de corvo” para representar a cardinalidade (ex: uma linha com três traços para muitos, um traço para um).

## 4. Exemplo de Diagrama ER
Vamos modelar um exemplo simples de um sistema de pedidos, com as entidades **Cliente**, **Pedido**, e **Produto**.

1. **Cliente**: Tem atributos como `ID_Cliente` (PK), `Nome`, e `Endereço`.
2. **Pedido**: Tem atributos como `ID_Pedido` (PK), `Data` e `ID_Cliente` (FK).
3. **Produto**: Tem atributos como `ID_Produto` (PK), `Nome_Produto`, e `Preço`.

Relacionamentos:
- **Cliente faz Pedido** (1:N).
- **Pedido inclui Produto** (N:M) — precisaria de uma tabela associativa, como `Itens_Pedido`, para representar esse relacionamento.

## 5. Benefícios de um Diagrama ER
- **Clareza no Design**: Ajuda a visualizar o modelo de dados e entender como os dados se relacionam.
- **Melhoria na Comunicação**: Serve como um documento de referência claro entre equipes de desenvolvimento e stakeholders.
- **Base para a Criação do Banco de Dados**: Um ERD bem estruturado facilita a implementação de um banco de dados relacional.

## 6. Limitações dos Diagramas ER
- **Complexidade**: Para sistemas muito grandes, o diagrama pode se tornar complexo e difícil de entender.
- **Foco em Estrutura, não em Processos**: Os ERDs mostram a estrutura de dados, mas não como eles serão usados ou como o sistema funcionará.

---

Este resumo fornece uma visão geral dos conceitos básicos de diagramas de entidade-relacionamento (ERD), suas notações, componentes e como eles ajudam na modelagem de dados.
