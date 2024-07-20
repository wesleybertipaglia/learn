# Docker Commands

Docker commands are used to interact with the Docker daemon and manage containers, images, networks, and volumes. In this section, we will cover some of the most commonly used Docker commands.

## Basic Commands

1. **`docker version`**: Displays the Docker version information.

2. **`docker info`**: Displays system-wide information about Docker.

3. **`docker help`**: Displays help information for Docker commands.

4. **`docker run {image}`**: Runs a container based on the specified image.

## Image Commands

1. **`docker images`**: Lists all images on the system.

2. **`docker pull {image}`**: Pulls an image from a registry.

3. **`docker rmi {image}`**: Removes an image from the system.

4. **`docker build -t {tag} {path}`**: Builds an image from a Dockerfile.

## Container Commands

1. **`docker ps`**: Lists all running containers.

2. **`docker ps -a`**: Lists all containers, including stopped ones.

3. **`docker start {container}`**: Starts a stopped container.

4. **`docker stop {container}`**: Stops a running container.

5. **`docker rm {container}`**: Removes a container.

6. **`docker exec -it {container} {command}`**: Executes a command in a running container.

## Network Commands

1. **`docker network ls`**: Lists all networks on the system.

2. **`docker network create {name}`**: Creates a new network.

3. **`docker network connect {network} {container}`**: Connects a container to a network.

4. **`docker network disconnect {network} {container}`**: Disconnects a container from a network.

## Volume Commands

1. **`docker volume ls`**: Lists all volumes on the system.

2. **`docker volume create {name}`**: Creates a new volume.

3. **`docker volume inspect {volume}`**: Displays detailed information about a volume.

4. **`docker volume rm {volume}`**: Removes a volume.

These are just a few of the many Docker commands available. For a complete list of commands and options, refer to the [official Docker documentation](https://docs.docker.com/engine/reference/commandline/docker/).
