# Add Custom Software To The Image

The second step is to add custom software to the Docker image. We will use the `curl` utility as an example.

1. Modify the `Dockerfile` to include the following lines:

```Dockerfile
FROM nginx
RUN apt-get update && apt-get install -y curl
COPY index.html /usr/share/nginx/html/
```

This Dockerfile adds a new `RUN` instruction that updates the package index and installs the `curl` utility using the `apt-get` package manager.

2. Rebuild the Docker image using the following command:

```bash
docker build -t my-nginx-curl .
```

This command builds a new Docker image with the tag `my-nginx-curl` that includes the `curl` utility.

3. Verify that the image was created successfully by running the following command:

```bash
docker images
```

You should see the `my-nginx-curl` image listed in the output.

4. Run a container based on the new image using the following command:

```bash
docker run -d --name curl -it my-nginx-curl
```

This command starts a new container based on the `my-nginx-curl` image, and opens a Bash shell inside the container.

5. Test the `curl` utility by running the following command inside the container:

```bash
docker exec -it curl bash
curl http://localhost:80
```

You should see the HTML content of the `index.html` file displayed in the console.
