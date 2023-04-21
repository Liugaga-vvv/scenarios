# Read Data From A Docker Volume

To read data from a Docker volume, you can simply read from the directory where the volume is mounted inside the container. For example, if you want to read the contents of the `hello.txt` file that you created in the previous step, you can run the following command inside the container:

```bash
docker exec container_name cat /app/data/hello.txt
```

Replace `container_name` with the name `c1` of the running container. This command reads the contents of the `/app/data/hello.txt` file inside the container and outputs it to the console.
