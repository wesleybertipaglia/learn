# Docker Architecture

Docker is a platform for developing, shipping, and running applications using containerization. In this section, we will explore how Docker works internally, including its architecture, containers, images, and networking.

![Docker Architecture](https://docs.docker.com/guides/images/docker-architecture.webp)

Docker architecture consists of several key components:

- **Client (docker):** The command-line interface (CLI) that allows users to interact with Docker Daemon.
- **Host:** The system running the Docker Daemon, images and containers.
- **Registry:** A repository for Docker images, such as Docker Hub or a private registry.

## Docker Client

The Docker client is the primary way that users interact with Docker. It accepts commands from the user and communicates with the Docker Daemon to execute them. The client can run on the same system as the Docker Daemon or on a remote system that connects to the Docker Daemon over a network.

It provides interfaces for managing containers, images, networks, and volumes, as well as other Docker resources. The client communicates with the Docker Daemon using the Docker Remote API, which allows it to send commands and receive responses from the Daemon. Here are some common Docker client commands:

- `docker run`: Runs a container based on a specified image.

- `docker build`: Builds an image from a Dockerfile.

- `docker pull`: Pulls an image from a registry.

- `docker push`: Pushes an image to a registry.

- `docker exec`: Executes a command in a running container.

- `docker ps`: Lists all running containers.

## Docker Host

The Docker host is the system that runs the Docker Daemon, images, and containers. It is responsible for managing the containers and providing the necessary resources for them to run. The host can be a physical machine, a virtual machine, or a cloud instance.

The Docker Daemon is the background service that manages the Docker objects, such as images, containers, networks, and volumes. It listens for Docker API requests and manages the Docker objects on the host system. The Daemon is responsible for creating, running, stopping, and removing containers, as well as managing the networking and storage for the containers.

## Docker Registry

The Docker Registry is a repository for Docker images. It stores images that can be shared and reused by users. The most popular Docker Registry is Docker Hub, which is a public registry that hosts thousands of images for various applications and services. Users can also create private registries to store their own images securely.

When a user runs a container based on an image, Docker pulls the image from the registry if it is not already available on the host system. Users can also push their own images to the registry to share them with others. The registry provides a centralized location for managing and distributing Docker images.

## Conclusion

In summary, Docker architecture consists of the Docker client, Docker host, and Docker registry. The client interacts with the Daemon to manage containers, images, networks, and volumes. The host runs the Daemon and manages the containers, while the registry stores and distributes Docker images. Understanding the Docker architecture is essential for working with Docker effectively and efficiently.