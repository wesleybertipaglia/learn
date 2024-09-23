# Docker Compose Commands

Docker Compose is a powerful tool for defining and running multi-container Docker applications. Below is a summary of the most commonly used Docker Compose commands.

## docker-compose up
The `up` command is used to create and start the containers defined in the `docker-compose.yml` file. If the containers do not exist, they will be created. If they already exist, they will be started.

```bash
docker-compose up
```

**Options**
- `-d` or `--detach`: Run the containers in the background (detached mode).
- `--build`: Build the images before starting the containers.
- `--force-recreate`: Recreate the containers even if they are already running.
- `--no-deps`: Do not start linked services.
- `--remove-orphans`: Remove containers for services not defined in the Compose file.

## docker-compose down
The `down` command is used to stop and remove the containers defined in the `docker-compose.yml` file. This command also removes any networks created by `docker-compose up`.

```bash
docker-compose down
```

**Options**
- `-v` or `--volumes`: Remove named volumes declared in the `volumes` section of the Compose file.
- `--rmi all`: Remove all images used by any service.

## docker-compose start
The `start` command is used to start the containers defined in the `docker-compose.yml` file.

```bash
docker-compose start
```

## docker-compose stop
The `stop` command is used to stop the containers defined in the `docker-compose.yml` file.

```bash
docker-compose stop
```

## docker-compose restart
The `restart` command is used to restart the containers defined in the `docker-compose.yml` file.

```bash
docker-compose restart
```

**Options**
- `-v` or `--volumes`: Remove named volumes declared in the `volumes` section of the Compose file.
- `--rmi all`: Remove all images used by any service.

## docker-compose ps
The `ps` command is used to list the containers managed by Docker Compose.

```bash
docker-compose ps
```

**Options**
- `-q` or `--quiet`: Only display container IDs.
- `--services`: Display services.

## docker-compose exec
The `exec` command is used to run a command in a running container.

```bash
docker-compose exec <service-name> <command>
```

**Options**
- `-d` or `--detach`: Run the command in detached mode.
- `--user <username>`: Specify the username or UID to use when running the command.


## docker-compose logs
The `logs` command is used to view the logs of the containers managed by Docker Compose.

```bash
docker-compose logs
```

**Options**
- `-f` or `--follow`: Follow log output.
- `--tail <number>`: Number of lines to show from the end of the logs.

## docker-compose build
The `build` command is used to build or rebuild the images defined in the `docker-compose.yml` file.

```bash
docker-compose build
```

**Options**
- `--no-cache`: Do not use cache when building the image.
- `--pull`: Always attempt to pull a newer version of the image.

## docker-compose pull
The `pull` command is used to pull the latest images for the services defined in the `docker-compose.yml` file.

```bash
docker-compose pull
```

## docker-compose config
The `config` command is used to validate and view the configuration of the `docker-compose.yml` file.

```bash
docker-compose config
```

**Options**
- `--services`: Display the services.
- `--volumes`: Display the volumes.
- `--networks`: Display the networks.

These are some of the most commonly used Docker Compose commands. By mastering these commands, you can efficiently manage multi-container applications using Docker Compose. For a complete list of commands and options, refer to the [official Docker Compose documentation](https://docs.docker.com/compose/reference/overview/).
