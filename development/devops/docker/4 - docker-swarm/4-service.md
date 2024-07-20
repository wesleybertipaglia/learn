# Service Commands

## docker service ls
The `docker service ls` command lists the services in the Swarm cluster. This command is used to list the services in the Swarm cluster along with their status and availability.

```bash
docker service ls
```

## docker service inspect
The `docker service inspect` command inspects a service in the Swarm cluster. This command is used to inspect the details of a specific service in the Swarm cluster.

```bash
docker service inspect <service-id>
```

## docker service create
The `docker service create` command creates a new service in the Swarm cluster. This command is used to create a new service in the Swarm cluster with the specified configuration.

```bash
docker service create --name <service-name> --replicas <replicas> <image>
```

## docker service update
The `docker service update` command updates the configuration of a service in the Swarm cluster. This command is used to update the configuration of a specific service in the Swarm cluster.

```bash
docker service update --replicas <replicas> <service-id>
```

## docker service scale
The `docker service scale` command scales a service in the Swarm cluster. This command is used to scale the number of replicas of a specific service in the Swarm cluster.

```bash
docker service scale <service-id>=<replicas>
```

## docker service rm
The `docker service rm` command removes a service from the Swarm cluster. This command is used to remove a specific service from the Swarm cluster.

```bash
docker service rm <service-id>
```

## docker service logs
The `docker service logs` command displays the logs of a service in the Swarm cluster. This command is used to display the logs of a specific service in the Swarm cluster.

```bash
docker service logs <service-id>
```

## docker service ps
The `docker service ps` command lists the tasks of a service in the Swarm cluster. This command is used to list the tasks of a specific service in the Swarm cluster along with their status and availability.

```bash
docker service ps <service-id>
```

## docker service update --force
The `docker service update --force` command forces an update of a service in the Swarm cluster. This command is used to force an update of a specific service in the Swarm cluster.

```bash
docker service update --force <service-id>
```

## docker service update --rollback
The `docker service update --rollback` command rolls back an update of a service in the Swarm cluster. This command is used to roll back an update of a specific service in the Swarm cluster.

```bash
docker service update --rollback <service-id>
```

## docker service update --image
The `docker service update --image` command updates the image of a service in the Swarm cluster. This command is used to update the image of a specific service in the Swarm cluster.

```bash
docker service update --image <service-id>=<new-image>
```
