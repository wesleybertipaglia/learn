# Kubernetes Setup Tutorial

This guide outlines the steps to set up a Kubernetes cluster using Minikube, a tool for running Kubernetes locally.

## Prerequisites

- **System Requirements**: At least 2 GB of RAM and 2 CPUs.
- **Install Dependencies**:
  - [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
  - [Minikube](https://minikube.sigs.k8s.io/docs/start/)
  - A virtualization software (e.g., VirtualBox, Docker).

## Step 1: Install kubectl

Follow the installation instructions for your OS:

```bash
# For macOS
brew install kubectl

# For Windows (using Chocolatey)
choco install kubernetes-cli

# For Linux
sudo apt-get install -y kubectl
```

## Step 2: Install Minikube

Download and install Minikube using the package manager for your OS:

```bash
# For macOS
brew install minikube

# For Windows (using Chocolatey)
choco install minikube

# For Linux
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube \
  && sudo mv minikube /usr/local/bin/
```

## Step 3: Start Minikube

Start Minikube using the following command:

```bash
minikube start
```

## Step 4: Verify Installation

Check the status of the cluster using the following command:

```bash
kubectl cluster-info
```

## Step 5: Deploy your first application

Create a simple deployment using the following command:

```bash
kubectl create deployment hello-world --image=nginx
```

Expose the deployment as a service:

```bash
kubectl expose deployment hello-world --type=NodePort --port=80
```

Access the service:

```bash
minikube service hello-world
```

Success! You have set up a Kubernetes cluster using Minikube.

> To stop Minikube, run `minikube stop`.

## Additional Resources

- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [Minikube GitHub Repository](https://github.com/kubernetes/minikube)

---

- [Previous](./3-components.md)