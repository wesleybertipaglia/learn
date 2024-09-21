# Docker Swarm Commands

Docker Swarm provides a variety of commands to manage and orchestrate your Swarm cluster. Below is a summary of the most commonly used Docker Swarm commands.

## docker swarm init
The `docker swarm init` command initializes a new Docker Swarm. This command is used to create a new Swarm cluster and designate the current node as the Swarm manager.

```bash
docker swarm init
```

## docker swarm join
The `docker swarm join` command is used to join a node to an existing Docker Swarm. This command is used to add additional nodes to the Swarm cluster.

```bash
docker swarm join --token <token> <manager-ip>:<manager-port>
```

## docker swarm leave
The `docker swarm leave` command is used to remove a node from the Swarm cluster. This command is used to gracefully leave the Swarm cluster.

```bash
docker swarm leave
```

## docker swarm update
The `docker swarm update` command is used to update the configuration of the Swarm cluster. This command is used to update the configuration of the Swarm manager or worker nodes.

```bash
docker swarm update --autolock=true
```

## docker swarm unlock
The `docker swarm unlock` command is used to unlock a locked Swarm cluster. This command is used to unlock a Swarm cluster that has been locked due to too many failed attempts to unlock it.

```bash
docker swarm unlock
```

## docker swarm unlock-key
The `docker swarm unlock-key` command is used to retrieve the unlock key for a locked Swarm cluster. This command is used to retrieve the unlock key that is required to unlock a locked Swarm cluster.

```bash
docker swarm unlock-key
```
