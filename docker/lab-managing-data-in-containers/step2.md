# Mount A Docker Volume In A Container

To use a Docker volume in a container, you need to mount it as a directory inside the container. You can do this by using the `-v` option when running a container:

```bash
docker run -td --name=c1 -v myvolume:/app/data centos
```

This command runs a new Docker container, it is name `c1` based on the `centos` image and mounts the `myvolume` volume as a directory inside the container at the `/app/data` path.

You can verify that the volume is mounted correctly by running the `docker inspect` command:

```bash
docker inspect <container_name>
```

Replace `<container_name>` with the name `c1` of the running container. In the output, you should see a section like this:

```json
"Mounts": [
    {
        "Type": "volume",
        "Name": "myvolume",
        "Source": "/var/lib/docker/volumes/myvolume/_data",
        "Destination": "/app/data",
        "Driver": "local",
        "Mode": "",
        "RW": true,
        "Propagation": ""
    }
]
```

This section indicates that the `myvolume` volume is mounted as a directory inside the container at the `/app/data` path.
