# Kubernetes Architecture

Kubernetes architecture consists of several components that work together to manage containerized applications across a cluster of machines.

## Key Components

### 1. Master Node
The master node is the control plane that manages the Kubernetes cluster. It handles API requests, scheduling, and overall cluster management.

- **API Server**: The front-end for the Kubernetes control plane, exposing the Kubernetes API.
- **Controller Manager**: Manages controllers that regulate the state of the cluster, ensuring the desired state matches the actual state.
- **Scheduler**: Assigns work to worker nodes by scheduling pods based on resource availability.

### 2. Worker Nodes
Worker nodes are responsible for running the applications. Each node contains the necessary components to manage pods.

- **Kubelet**: An agent that runs on each worker node, ensuring that containers are running in pods.
- **Kube-Proxy**: Maintains network rules and enables communication between pods.
- **Container Runtime**: The software responsible for running containers (e.g., Docker, containerd).

## Pods
The smallest deployable units in Kubernetes, pods can contain one or more containers that share the same network namespace.

## Services
A way to expose a set of pods as a network service, providing stable IP addresses and DNS names.

## Configurations
Kubernetes uses YAML files for configuration, defining desired states for deployments, services, and other resources.

## Why This Architecture?

- **Decoupled Components**: Each component can be managed independently, improving flexibility and scalability.
- **High Availability**: The architecture allows for redundancy and failover mechanisms, ensuring consistent application availability.
- **Resource Efficiency**: Kubernetes optimally schedules pods based on resource requirements, maximizing utilization of hardware.

---

- [Previous](./1-introduction.md)
- [Next](./3-components.md)
