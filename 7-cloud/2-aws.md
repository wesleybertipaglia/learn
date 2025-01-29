# Amazon Web Services (AWS)

## 1. What is AWS?
**Amazon Web Services (AWS)** is a cloud computing platform provided by Amazon, which offers a wide range of infrastructure services and tools for businesses and developers. These services are delivered over the Internet in a **pay-as-you-go** model, which means that users pay only for what they use.

### 1.1. Main Features
- **Automatic Scalability**: Allows you to automatically adjust resources according to demand.
- **Pay-On-Demand Model**: No long-term contracts or large upfront expenses.
- **Security and Reliability**: AWS offers a high level of security with compliance with several standards, such as ISO, PCI, DSS and SOC.
- **Global Presence**: Data centers located in several regions of the world, allowing fast delivery of services.

## 2. Main AWS Services

### 2.1. Computing
- **EC2 (Elastic Compute Cloud)**: Scalable virtual machine service, allowing users to provision and manage instances with different operating systems and hardware configurations.
- **Lambda**: **Serverless** computing service that executes code in response to events without having to manage servers.
- **Elastic Beanstalk**: PaaS service that facilitates application management and automatically adjusts infrastructure capacity.
- **Lightsail**: Simplified alternative to EC2, ideal for small applications and development environments.

### 2.2. Storage
- **S3 (Simple Storage Service)**: Highly scalable object storage service, used to store and retrieve large volumes of data.
- **EBS (Elastic Block Store)**: Provides block storage for EC2 instances, with high durability and performance.
- **Glacier**: Low-cost storage service for files that do not need to be accessed frequently, ideal for long-term archiving.
- **EFS (Elastic File System)**: Scalable and elastic file system to be mounted on EC2 instances.

### 2.3. Databases
- **RDS (Relational Database Service)**: Managed service for relational databases such as MySQL, PostgreSQL, SQL Server and Aurora (AWS's optimized database).
- **DynamoDB**: Managed and high-performance NoSQL database, ideal for applications that require low latency and high scalability.
- **Redshift**: Data warehouse service for analyzing large volumes of data.
- **ElastiCache**: Managed service for in-memory caches (Memcached and Redis), improving application performance by reducing the load on databases.

### 2.4. Networks and Content Distribution
- **VPC (Virtual Private Cloud)**: Creation of isolated virtual private networks in the cloud to host and manage resources securely. - **CloudFront**: CDN (Content Delivery Network) service that accelerates the delivery of content, such as websites, videos, and APIs, on a global scale.
- **Route 53**: Scalable and highly available DNS service for routing internet traffic.
- **Elastic Load Balancing (ELB)**: Automatically distributes incoming traffic across multiple EC2 instances to ensure high availability and load balancing.

### 2.5. Security and Identity
- **IAM (Identity and Access Management)**: Service that allows you to manage access to AWS resources with detailed control over permissions for users, groups, and roles.
- **KMS (Key Management Service)**: Management of encryption keys to protect sensitive data.
- **AWS Shield**: DDoS attack protection service, with standard or advanced protection options.
- **Cognito**: User identity management, offering authentication, authorization, and profile synchronization for web and mobile applications.

### 2.6. Development and Integration Tools
- **CloudFormation**: Allows you to model and provision your entire AWS infrastructure using YAML or JSON templates.
- **CodeDeploy**: Automates code deployment on EC2 instances, lambdas, or on-premises servers.
- **CodePipeline**: Continuous integration and delivery (CI/CD) service that allows you to automate software release pipelines.
- **CloudWatch**: Real-time monitoring and observation service for logs, metrics, and events.

### 2.7. Artificial Intelligence and Machine Learning
- **SageMaker**: Complete platform for building, training, and deploying machine learning models.
- **Rekognition**: Image and video recognition service used to identify objects, people, texts, and activities.
- **Polly**: Text-to-speech conversion with multiple voices and languages.
- **Lex**: Service for creating chatbots with advanced natural language processing capabilities.

### 2.8. Data Analysis
- **EMR (Elastic MapReduce)**: Managed platform that facilitates the processing of large volumes of data using frameworks such as Hadoop, Spark and Presto.
- **Athena**: Interactive query service that allows you to analyze data directly in S3 using standard SQL.
- **Kinesis**: Real-time processing of large volumes of streaming data.
- **Data Pipeline**: Service that allows you to automate the movement and transformation of data between different AWS services.

## 3. AWS Pricing
### 3.1. Pricing Model
AWS uses a **pay-as-you-go** model, which means you pay only for the resources you use, with no large upfront costs or long-term contracts.

### 3.2. Pricing Options
- **On-Demand Instances**: You pay only for the time the instances are active.
- **Reserved Instances**: Offer a lower price in exchange for a usage commitment for a specific period (1 or 3 years).
- **Spot Instances**: Offer deep discounts in exchange for availability based on market demand and supply of idle instances.

### 3.3. AWS Free Tier
AWS offers a limited free tier for new users, which includes services such as EC2, S3, RDS, and Lambda with usage limits, valid for 12 months.

## 4. Advantages of AWS
- **Wide Range of Services**: AWS offers hundreds of services, allowing you to build complete solutions for different use cases.
- **Reliability and Scalability**: The global distributed infrastructure ensures high availability and automatic scalability.
- **Security**: AWS invests heavily in security, with rigorous certifications and compliances.
- **Community and Support**: A large customer base and a vast community of developers and partners who provide support, documentation, and resources.

## 5. Challenges and Considerations
- **Complexity**: The wide range of services and flexibility of AWS can be overwhelming for beginners.
- **Cost**: While AWS can be cost-effective for small projects, costs can quickly add up for large volumes of data and traffic. - **Internet Dependency**: Since AWS operates in the cloud, performance is dependent on internet connectivity.

## 6. Common Use Cases
- **Web Application Hosting**: EC2 and RDS are often used to host scalable web applications.
- **Storage and Backup**: S3 is a popular solution for storing files, backups, and static content.
- **Big Data Processing**: Tools like EMR, Athena, and Redshift are used to analyze large volumes of data.
- **Serverless Applications**: Lambda and API Gateway allow you to build serverless applications, where you only pay for the time they run.

## 7. AWS Certifications
AWS offers a variety of certifications that help validate the skills of professionals on the platform:
- **AWS Certified Solutions Architect – Associate**
- **AWS Certified Developer – Associate**
- **AWS Certified SysOps Administrator – Associate**
- **AWS Certified DevOps Engineer – Professional**
- **AWS Certified Machine Learning – Specialty**

---

- [<< Previous](./1-foundations.md)
- [Next >>](./3-azure.md)