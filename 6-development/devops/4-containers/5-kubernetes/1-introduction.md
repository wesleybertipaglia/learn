# Introduction to Kubernetes

Kubernetes (K8s) is an open-source container orchestration platform initially developed by Google. It automates the deployment, scaling, and management of containerized applications, providing a powerful framework for managing microservices architectures.

## Syntax

Kubernetes uses a declarative syntax for managing applications through YAML configuration files. Here’s a summary of key Kubernetes commands and concepts.

```bash
# Create a new Kubernetes cluster
kubectl create cluster

# Get cluster information
kubectl cluster-info

# Deploy an application
kubectl apply -f deployment.yaml

# List all pods
kubectl get pods

# Describe a pod
kubectl describe pod <pod-name>

# Scale a deployment
kubectl scale deployment <deployment-name> --replicas=<number>

# Update a deployment
kubectl set image deployment/<deployment-name> <container-name>=<new-image>

# Delete a deployment
kubectl delete deployment <deployment-name>
```

## Why Use Kubernetes?
- High Availability Kubernetes ensures your applications are highly available by automatically rescheduling containers when a node fails, maintaining uptime.

- Scalability It allows you to easily scale applications up or down based on demand, making it ideal for fluctuating workloads.

- Load Balancing Kubernetes automatically distributes network traffic to ensure no single container is overwhelmed, improving resource utilization.

- Declarative Configuration With Kubernetes, you define the desired state of your applications in YAML files, allowing K8s to ensure the actual state matches.

- Ecosystem Integration Kubernetes integrates seamlessly with various tools and services, including monitoring and logging solutions, enhancing your cloud-native stack.

- Self-Healing K8s automatically replaces and reschedules containers that fail, ensuring your applications remain operational without manual intervention.

## What Can You Do With Kubernetes?
- Deploy and Manage Applications Kubernetes allows you to define and manage complex applications using simple configuration files, supporting both stateless and stateful workloads.

- Scale Applications Easily adjust the number of replicas for your applications to handle varying loads, ensuring efficient performance.

- Ensure High Availability By distributing replicas across multiple nodes, Kubernetes keeps your applications available even during node failures.

- Perform Rolling Updates Kubernetes supports rolling updates, allowing you to update applications without downtime. You can roll back if issues arise.

- Simplify Networking K8s provides a robust networking model, allowing containers to communicate seamlessly regardless of where they are deployed in the cluster.

- Manage Storage Kubernetes abstracts storage management, allowing you to attach persistent storage to containers, ensuring data durability.

- Monitor and Troubleshoot Use built-in tools and commands to monitor the health and performance of your applications and quickly troubleshoot issues.

## Key Concepts

- **Node** A Kubernetes node is a physical or virtual machine that runs your applications. It can be a master node or a worker node.

- **Pod** A Pod is the smallest deployable unit in Kubernetes, consisting of one or more containers that share resources, such as storage and network.

- **Cluster** A Kubernetes cluster consists of a master node and multiple worker nodes. The master node manages the cluster, while the worker nodes run your applications.

- **Container** A container is a lightweight, standalone executable package that includes everything needed to run an application, including code, runtime, libraries, and dependencies.

- **Workload** A workload is a set of containers that run together to provide a specific service. Kubernetes supports various workload types, including Deployments, StatefulSets, and DaemonSets.

- **Service** A Kubernetes Service is an abstraction that defines a logical set of Pods and a policy by which to access them. It enables network access to a set of Pods, providing load balancing and service discovery.

- **Storage** Kubernetes provides persistent storage for containers using Persistent Volumes (PVs) and Persistent Volume Claims (PVCs). PVs are storage resources in the cluster, while PVCs are requests for storage by Pods.

## Additional Resources

- [Kubernetes Website](https://kubernetes.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes GitHub Repository](https://github.com/kubernetes/kubernetes)


---

- [Next](./2-architecture.md)