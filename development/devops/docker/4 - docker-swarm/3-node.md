# Node Commands

## docker node ls
The `docker node ls` command lists the nodes in the Swarm cluster. This command is used to list the nodes in the Swarm cluster along with their status and availability.

```bash
docker node ls
```

## docker node inspect
The `docker node inspect` command inspects a node in the Swarm cluster. This command is used to inspect the details of a specific node in the Swarm cluster.

```bash
docker node inspect <node-id>
```

## docker node update
The `docker node update` command updates the configuration of a node in the Swarm cluster. This command is used to update the configuration of a specific node in the Swarm cluster.

```bash
docker node update --availability drain <node-id>
```

## docker node promote
The `docker node promote` command promotes a node to a manager in the Swarm cluster. This command is used to promote a worker node to a manager node in the Swarm cluster.

```bash
docker node promote <node-id>
```

## docker node demote
The `docker node demote` command demotes a manager to a worker in the Swarm cluster. This command is used to demote a manager node to a worker node in the Swarm cluster.

```bash
docker node demote <node-id>
```

## docker node rm
The `docker node rm` command removes a node from the Swarm cluster. This command is used to remove a specific node from the Swarm cluster.

```bash
docker node rm <node-id>
```
