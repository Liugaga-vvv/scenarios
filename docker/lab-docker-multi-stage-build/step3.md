# Run A Docker Container

The final step is to use the Docker image to run a Docker container. To do this, follow these steps:

1. Run the following command to start a new Docker container:

```bash
docker run -p 3030:3000 myapp
```

This command starts a new Docker container using the `myapp` image you just built, and maps port 3000 on the container to port 3030 on the host.

2. Open a web browser and navigate to `http://localhost:3030` to access the running application.
