# Cloud Computing Fundamentals

## 1. What is Cloud Computing?
**Cloud Computing** refers to the delivery of computing services — such as servers, storage, databases, networks, software, and intelligence — over the Internet (“cloud”). These services are provided by cloud providers such as **Amazon Web Services (AWS)**, **Microsoft Azure**, **Google Cloud Platform (GCP)**, among others.

### 1.1. Key Features of the Cloud
- **On-Demand Self-Service**: The user can provision and manage resources as needed, without the need for human interaction with the provider.
- **Broad Network Access**: Services can be accessed through any Internet-connected device.
- **Rapid Elasticity**: Resources can be quickly adjusted to scale according to demand. - **Pooled Resources**: Multiple customers share a pool of computing resources that are dynamically allocated.
- **Pay-as-you-go model**: Customers pay only for the resources they actually use.

## 2. Cloud Computing Service Models
There are three main service models in cloud computing, each with different levels of control and responsibility for the user.

### 2.1. IaaS (Infrastructure as a Service)
- Provides infrastructure resources such as virtual machines, networks, and storage on demand.
- The user manages the operating system, middleware, and applications, while the provider takes care of the physical infrastructure.
- **Examples**: AWS EC2, Google Compute Engine, Microsoft Azure Virtual Machines.

### 2.2. PaaS (Platform as a Service)
- Provides a complete platform for developing, running, and managing applications without having to deal with the underlying infrastructure.
- The user manages the applications, while the provider takes care of the operating system, infrastructure, and runtime. - **Examples**: Google App Engine, Heroku, AWS Elastic Beanstalk.

### 2.3. SaaS (Software as a Service)
- Provides ready-to-use applications, accessible over the Internet, without the need for local installation.
- The provider takes care of all the infrastructure, maintenance and updates.
- **Examples**: Google Workspace, Salesforce, Microsoft 365.

## 3. Deployment Models
Cloud services can be deployed in different ways, depending on the needs of the organization.

### 3.1. Public Cloud
- Offered by third-party providers and available to any person or company that wants to use it.
- Resources are shared among multiple customers, but are isolated to ensure privacy.
- **Examples**: AWS, Azure, Google Cloud.

### 3.2. Private Cloud
- The cloud infrastructure is dedicated to a single organization, being managed by the company itself or by a third-party provider. - Provides greater control and security, but at higher costs.
- **Examples**: Private clouds built with OpenStack or VMware.

### 3.3. Hybrid Cloud
- Combines public and private clouds, allowing data and applications to be shared between them.
- Offers flexibility, allowing companies to keep critical data in the private cloud while using the public cloud for other operations.
- **Examples**: Microsoft Azure with Azure Stack, AWS with VPC (Virtual Private Cloud).

### 3.4. Community Cloud
- Shared by several organizations with similar needs (e.g., government agencies).
- The infrastructure is managed and used collectively by the participating organizations.

## 4. Advantages of Cloud Computing
- **Cost Reduction**: Eliminates the need for investments in hardware and data center maintenance.
- **Scalability**: Automatically increases or reduces capacity according to demand. - **Global Access**: Allows access to resources and data from anywhere with an Internet connection.
- **Business Continuity**: Cloud providers typically offer high availability and backup, ensuring resilience.
- **Security**: Many providers offer infrastructure with high levels of security and compliance with data regulations.

## 5. Disadvantages and Challenges of Cloud Computing
- **Connectivity Dependence**: Accessing cloud services depends on a reliable Internet connection.
- **Security Concerns**: Although cloud providers implement rigorous security, sensitive data may still be at risk.
- **Limited Control**: Users have less control over the underlying infrastructure compared to on-premises solutions.
- **Long-Term Cost**: For large companies, the cost of ongoing use of cloud services can accumulate over time.

## 6. Important Cloud Computing Concepts

### 6.1. Virtualization
- Virtualization is the technology that allows the creation of multiple virtual machines on a single physical server. It is essential for the cloud, as it allows resources to be used efficiently and flexibly.
- **Hypervisors**: These are the software that manages virtualization. There are two types:
- **Type 1 (bare metal)**: Runs directly on the hardware (e.g.: VMware ESXi, Microsoft Hyper-V).
- **Type 2 (hosted)**: Runs on an operating system (e.g.: VirtualBox, VMware Workstation).

### 6.2. Containers and Kubernetes
- **Containers**: Technology that allows you to package and run applications in isolation. It is lighter than a virtual machine, as it shares the operating system kernel.
- **Kubernetes**: Container orchestration platform that automates the management, scalability, and operation of containerized applications.

### 6.3. Multi-Cloud
- The use of more than one cloud service provider. Allows organizations to choose different services and offerings from each provider to meet their specific needs.
- **Example**: A company can use AWS for IaaS and Google Cloud for Machine Learning.

## 7. Cloud Computing Use Case Examples
- **Data Storage and Backup**: Using the cloud to store large volumes of data and backups.
- **Software Development and Testing**: Test environments can be quickly set up and torn down in the cloud.
- **Streaming Services**: Video and music streaming platforms use the cloud to deliver content globally.
- **Machine Learning and AI**: Cloud providers offer ML and AI services that can be used without the need for your own infrastructure.
- **Serverless Computing**: Executing functions without the need to provision or manage servers (e.g., AWS Lambda, Google Cloud Functions).

## 8. Cloud Computing Providers
- **Amazon Web Services (AWS)**: Offers a wide range of services, including computing, storage, databases, and artificial intelligence. - **Microsoft Azure**: Microsoft's cloud platform that supports integration with Microsoft services, as well as IaaS, PaaS, and SaaS.
- **Google Cloud Platform (GCP)**: Excels in data analytics and machine learning, in addition to offering traditional IaaS and PaaS services.
- **IBM Cloud**: Focused on enterprise solutions and hybrid computing.
- **Oracle Cloud**: Specialized in databases and enterprise solutions.

---

- [>> Next](./2-aws.md)