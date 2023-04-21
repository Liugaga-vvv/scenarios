# Create A Docker Volume

A volume is a Docker object that allows you to store data separately from the container. You can use a volume to store configuration files, databases, logs, or any other data that needs to persist across container restarts.

To create a Docker volume, use the `docker volume create` command:

```bash
docker volume create myvolume
```

This command creates a new Docker volume named `myvolume`. You can list all the Docker volumes on your machine using the `docker volume ls` command:

```bash
docker volume ls
```

You should see the `myvolume` volume in the output.
