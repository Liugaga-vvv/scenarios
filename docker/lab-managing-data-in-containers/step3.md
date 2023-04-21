# Write Data To A Docker Volume

To write data to a Docker volume, you can simply write to the directory where the volume is mounted inside the container. For example, if you want to create a new file in the `myvolume` volume, you can run the following command inside the container:

```bash
docker exec container_name sh -c "echo 'Hello, World!' > /app/data/hello.txt"
```

Replace `container_name` with the name `c1` of the running container. This command writes the `Hello, World!` string to the `/app/data/hello.txt` file inside the container.

You can verify that the file is created by running the following command on your host machine:

```bash
docker volume inspect myvolume
```

This command inspects the `myvolume` volume and outputs information about it, including the path where the volume data is stored on your host machine.

Navigate to the path indicated in the output and you should see a `hello.txt` file with the `Hello, World!` string in it.
