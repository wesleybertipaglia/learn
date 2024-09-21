# Administração de Redes

## 1. Monitoramento de Rede
O **monitoramento de rede** é o processo de observar e analisar a atividade e o desempenho de uma rede para garantir que ela esteja operando de forma eficiente e segura. Ele ajuda a identificar problemas de desempenho, falhas, gargalos e ameaças de segurança.

### 1.1. Ferramentas de Monitoramento
Ferramentas de monitoramento são usadas para coletar e analisar dados de desempenho de rede.
- **Nagios**: Monitora servidores, switches, e roteadores, alertando sobre falhas e gargalos.
- **Zabbix**: Fornece monitoramento em tempo real de desempenho de redes, servidores e aplicações.
- **Wireshark**: Uma ferramenta de análise de pacotes que captura e inspeciona o tráfego de rede.
- **Prometheus + Grafana**: Monitoramento de métricas de rede com visualização de dados em dashboards.

### 1.2. Métricas Comuns de Monitoramento
- **Largura de Banda (Bandwidth)**: Volume de dados transmitidos por unidade de tempo.
- **Latência**: Tempo que um pacote leva para ir de um ponto a outro na rede.
- **Perda de Pacotes**: Percentual de pacotes de dados que são descartados durante a transmissão.
- **Taxa de Erro**: Percentagem de pacotes que são corrompidos ou perdidos durante a transmissão.

## 2. IPsec (Internet Protocol Security)
**IPsec** é um conjunto de protocolos que fornecem autenticação, integridade e criptografia de dados em comunicação ponto a ponto na camada de rede (camada 3 - IP). É usado principalmente em **VPNs** e para proteger comunicações na Internet.

### 2.1. Componentes do IPsec
- **AH (Authentication Header)**: Fornece autenticação de integridade dos pacotes.
- **ESP (Encapsulating Security Payload)**: Fornece confidencialidade (criptografia), integridade e autenticação de pacotes.
- **SA (Security Association)**: Define os parâmetros de segurança (algoritmos, chaves) usados para proteger a comunicação.
- **IKE (Internet Key Exchange)**: Protocolo usado para negociar chaves de segurança e estabelecer SAs.

### 2.2. Modos de Operação
- **Modo Transporte**: Apenas o payload (dados) do pacote IP é criptografado, mantendo o cabeçalho IP original.
- **Modo Túnel**: O pacote inteiro (cabeçalho e payload) é criptografado e encapsulado em um novo pacote IP.

### 2.3. Aplicações do IPsec
- **VPNs corporativas**: Proteger a comunicação entre redes remotas.
- **Proteção de dados na Internet**: Fornece segurança em comunicações sobre redes inseguras.

## 3. BGP (Border Gateway Protocol)
O **BGP** é o protocolo de roteamento utilizado para trocar informações de roteamento entre redes autônomas na Internet (AS - Autonomous Systems). Ele é crucial para garantir a conectividade global entre diferentes provedores de serviço.

### 3.1. Como o BGP Funciona
O BGP decide qual caminho os dados devem seguir para chegar a um destino, com base em regras e políticas definidas pelos administradores. Ele usa **sistemas autônomos** para rotear o tráfego entre diferentes redes.

### 3.2. Tipos de BGP
- **IBGP (Internal BGP)**: Utilizado dentro de um mesmo sistema autônomo.
- **EBGP (External BGP)**: Utilizado para a comunicação entre diferentes sistemas autônomos.

### 3.3. Riscos e Considerações
- **Segurança**: Ataques como a "sequestro de prefixos" (prefix hijacking) podem redirecionar tráfego para redes maliciosas.
- **Convergência lenta**: O BGP pode demorar a se ajustar a alterações na rede, especialmente em grande escala.
- **Políticas de Roteamento**: O BGP permite configurar políticas de roteamento complexas, mas isso requer planejamento cuidadoso.

### 3.4. Uso do BGP
- **Provedores de Internet**: Gerenciar roteamento entre ISPs e garantir que o tráfego siga caminhos otimizados.
- **Grandes empresas**: Conectar diferentes escritórios ou data centers via múltiplas rotas.

## 4. VPN (Virtual Private Network)
A **VPN** cria uma conexão segura e criptografada entre dois ou mais dispositivos sobre uma rede pública ou privada, como a Internet. É amplamente utilizada para acesso remoto seguro e para conectar redes diferentes.

### 4.1. Tipos de VPN
- **VPN Site-to-Site**: Conecta redes locais (LANs) em locais diferentes via a Internet. Usado por empresas para conectar filiais.
- **VPN de Acesso Remoto (Client-to-Site)**: Permite que usuários remotos se conectem com segurança à rede corporativa.
- **VPNs SSL**: Usa o protocolo SSL/TLS para criar um túnel seguro através de navegadores web.

### 4.2. Protocolos Comuns de VPN
- **OpenVPN**: Um dos mais usados, oferece alta segurança e flexibilidade.
- **L2TP/IPsec**: Combina o protocolo L2TP para tunelamento com o IPsec para segurança.
- **PPTP (Point-to-Point Tunneling Protocol)**: Simples, mas menos seguro em comparação a outros protocolos.

### 4.3. Aplicações de VPN
- **Acesso remoto seguro**: Usuários podem acessar recursos corporativos de qualquer lugar.
- **Privacidade na Internet**: VPNs são usadas para ocultar o IP e criptografar o tráfego de Internet.
- **Conexão de filiais**: Empresas podem interligar escritórios remotos de forma segura.

## 5. Load Balancing
O **Load Balancing** distribui o tráfego de rede entre vários servidores ou recursos para garantir disponibilidade, desempenho e redundância. Ele ajuda a evitar sobrecarga de servidores individuais e melhora o tempo de resposta do sistema.

### 5.1. Tipos de Load Balancing
- **Balanceamento de Carga de Rede (L3/L4)**: Funciona na camada de rede ou de transporte, redirecionando o tráfego baseado no endereço IP e na porta.
- **Balanceamento de Carga de Aplicação (L7)**: Funciona na camada de aplicação, redirecionando o tráfego com base no conteúdo do pacote (ex: cabeçalhos HTTP).

### 5.2. Algoritmos Comuns de Distribuição
- **Round Robin**: O tráfego é distribuído igualmente entre os servidores de forma cíclica.
- **Least Connections**: O tráfego é enviado para o servidor com o menor número de conexões ativas.
- **Hashing**: Usa o valor de um hash (como o IP do cliente) para decidir qual servidor receberá a conexão.

### 5.3. Ferramentas de Load Balancing
- **Nginx**: Um servidor web popular que também oferece recursos de balanceamento de carga.
- **HAProxy**: Um software amplamente usado para balanceamento de carga de alta performance.
- **AWS Elastic Load Balancer (ELB)**: Serviço gerenciado de balanceamento de carga em ambientes na nuvem da Amazon Web Services.

### 5.4. Vantagens do Load Balancing
- **Alta disponibilidade**: Garante que o serviço continue funcionando, mesmo se um servidor falhar.
- **Escalabilidade**: Facilita a adição de mais servidores conforme a demanda aumenta.
- **Desempenho melhorado**: Reduz o tempo de resposta distribuindo a carga de forma eficiente.

---

Esse resumo cobre os principais conceitos de administração de rede, como monitoramento, IPsec, BGP, VPN e Load Balancing, com suas funcionalidades, vantagens e exemplos de aplicação.
