# Run a Docker Container

In this step, we will run a Docker container based on the image we created in the previous step.

1. Run the following command to start a new container based on the `my-web-server` image:

```bash
docker run -d -p 8080:80 my-web-server
```

This command starts a new container in detached mode (`-d`) with port forwarding from the host port 8080 to the container port 80 (`-p 8080:80`). The container runs the `my-web-server` image we created in the previous step.

2. Open a web browser and go to `http://localhost:8080` to see the web page served by the container.
