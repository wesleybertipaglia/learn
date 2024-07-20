# Dockerfile Commands

## Basic Commands

- `FROM` - Sets the base image for subsequent instructions

```dockerfile
FROM ubuntu:18.04
```

- `RUN` - Executes a command in a new layer on top of the current image and commits the results

```dockerfile
RUN apt-get update
RUN apt-get install -y python3
```

- `LABEL` - Adds metadata to an image

```dockerfile
LABEL version="1.0"
LABEL description="This is a simple web server"
```

- `COPY` - Copies files or directories from a source to a destination

```dockerfile
COPY . /app
```

- `ADD` - Copies files, directories, or remote file URLs from a source to a destination

```dockerfile
ADD http://example.com/big.tar.xz /usr/src/things/
```

## Configuration Commands

- `EXPOSE` - Informs Docker that the container listens on the specified network ports at runtime

```dockerfile
EXPOSE 80
```

- `ENV` - Sets the environment variable

```dockerfile
ENV PATH="/usr/src/app/bin:${PATH}"
```

- `WORKDIR` - Sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` instructions that follow it in the Dockerfile

```dockerfile
WORKDIR /app
```

- `VOLUME` - Creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers

```dockerfile
VOLUME /var/log
```

## Execution Commands

- `CMD` - Provides defaults for an executing container

```dockerfile
CMD ["python3", "-m", "http.server"]
```


- `ENTRYPOINT` - Allows you to configure a container that will run as an executable

```dockerfile
ENTRYPOINT ["docker-entrypoint.sh"]
```

- `HEALTHCHECK` - Tells Docker how to test a container to check that it is still working

```dockerfile
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost/ || exit 1
```

- `SHELL` - Allows the default shell used for the shell form of commands to be overridden

```dockerfile
SHELL ["/bin/bash", "-c"]
```
