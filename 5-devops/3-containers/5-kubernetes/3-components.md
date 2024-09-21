# Kubernetes Components

Kubernetes is composed of various components that work together to manage containerized applications. These components can be categorized into control plane components and node components.

## Control Plane Components

### 1. API Server
- **Function**: Serves as the front-end of the Kubernetes control plane, handling API requests and updates to the cluster state.
- **Role**: Central point for communication; validates and processes RESTful API calls.

### 2. Controller Manager
- **Function**: Manages controllers that regulate the state of the cluster.
- **Role**: Ensures desired states are maintained by managing workloads and performing routine tasks, such as replicating pods.

### 3. Scheduler
- **Function**: Assigns pods to available worker nodes based on resource requirements.
- **Role**: Balances loads and ensures efficient resource utilization by considering node conditions.

### 4. etcd
- **Function**: A distributed key-value store that holds the cluster's configuration data and state.
- **Role**: Provides a reliable source of truth for the cluster’s data, enabling high availability.

## Node Components

### 1. Kubelet
- **Function**: An agent that runs on each worker node, managing the lifecycle of containers in pods.
- **Role**: Ensures that containers are running as expected and reports the status back to the API server.

### 2. Kube-Proxy
- **Function**: Manages network communication and load balancing for services.
- **Role**: Maintains network rules, allowing communication between pods and services, enabling service discovery.

### 3. Container Runtime
- **Function**: Software that runs containers (e.g., Docker, containerd).
- **Role**: Responsible for pulling images, starting, stopping, and managing containerized applications.

## Additional Components

### 1. Scheduler
- **Function**: Assigns newly created pods to worker nodes based on resource availability.
- **Role**: Optimizes resource distribution and workload balancing.

### 2. Dashboard
- **Function**: A web-based UI for managing Kubernetes clusters.
- **Role**: Provides visual insights into cluster status, resource utilization, and application health.

---

- [Previous](./2-architecture.md)
- [Next](./4-setup.md)
