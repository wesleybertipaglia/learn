# Modelo OSI (Open Systems Interconnection)

O Modelo OSI é um modelo de referência para redes de computadores que divide a comunicação de rede em 7 camadas distintas. Cada camada tem uma função específica e interage com as camadas acima e abaixo dela para garantir uma comunicação eficiente.

## 1. Camada Física

- **Função**: Transmissão de bits através do meio físico.
- **Protocolos e Tecnologias**: Ethernet, cabos de fibra óptica, sinais elétricos, conectores.
- **Exemplos**: Conexões de cabos, voltagens de sinal, características físicas dos meios de transmissão.

## 2. Camada de Enlace de Dados

- **Função**: Transmissão de quadros (frames) e controle de erros de camada física. Gerencia a comunicação entre dispositivos na mesma rede.
- **Protocolos e Tecnologias**: Ethernet, PPP (Point-to-Point Protocol), ARP (Address Resolution Protocol).
- **Exemplos**: Detecção e correção de erros, controle de acesso ao meio (MAC), endereçamento físico (endereços MAC).

## 3. Camada de Rede

- **Função**: Roteamento de pacotes e endereçamento lógico. Determina o caminho que os pacotes devem seguir na rede.
- **Protocolos e Tecnologias**: IP (Internet Protocol), ICMP (Internet Control Message Protocol).
- **Exemplos**: Endereçamento IP, roteadores, seleção de caminhos de roteamento.

## 4. Camada de Transporte

- **Função**: Controle de fluxo e erros, e transporte de dados de maneira confiável (ou não confiável). Garante a entrega correta e ordenada dos dados.
- **Protocolos e Tecnologias**: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).
- **Exemplos**: Controle de retransmissão de pacotes, segmentação e reassembly de dados.

## 5. Camada de Sessão

- **Função**: Estabelecimento, manutenção e encerramento de sessões de comunicação entre aplicações. Coordena o diálogo entre sistemas.
- **Protocolos e Tecnologias**: NetBIOS, RPC (Remote Procedure Call).
- **Exemplos**: Controle de sessões de comunicação, sincronização de diálogo.

## 6. Camada de Apresentação

- **Função**: Tradução, formatação e criptografia de dados. Garante que os dados sejam apresentados de forma que a camada de aplicação entenda.
- **Protocolos e Tecnologias**: SSL/TLS (para criptografia), formatos de dados como JPEG, MPEG.
- **Exemplos**: Compressão de dados, conversão de formatos, criptografia e descriptografia.

## 7. Camada de Aplicação

- **Função**: Interface entre as aplicações e a rede. Fornece serviços de rede para aplicativos de usuário.
- **Protocolos e Tecnologias**: HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), SMTP (Simple Mail Transfer Protocol).
- **Exemplos**: Navegadores web, clientes de e-mail, serviços de transferência de arquivos.

---

O Modelo OSI é uma ferramenta conceitual útil para entender e projetar redes de computadores, proporcionando uma abordagem sistemática para o processo de comunicação de rede. Cada camada do modelo é projetada para lidar com aspectos específicos da comunicação, garantindo uma troca de informações eficaz entre sistemas diferentes.
