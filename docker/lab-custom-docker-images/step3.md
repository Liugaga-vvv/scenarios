# Use Environment Variables In The Image

The third step is to use environment variables in the Docker image to customize its behavior. We will use the `NGINX_PORT` variable as an example.

1. Modify the `Dockerfile` to include the following lines:

```Dockerfile
FROM nginx
ENV NGINX_PORT 8080
RUN sed -i "s/listen\s*80;/listen $NGINX_PORT;/g" /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/
```

This Dockerfile adds a new `ENV` instruction that sets the value of the `NGINX_PORT` variable to `8080`. It also adds a new `RUN` instruction that replaces the default `listen` directive in the `nginx` configuration file with a new directive that uses the value of the `NGINX_PORT` variable.

2. Rebuild the Docker image using the following command:

```bash
docker build -t my-nginx-env .
```

This command builds a new Docker image with the tag `my-nginx-env` that uses environment variables.

3. Verify that the image was created successfully by running the following command:

```bash
docker images
```

You should see the `my-nginx-env` image listed in the output.

4. Run a container based on the new image using the following command:

```bash
docker run -p 8080:8080 -e NGINX_PORT=8080 my-nginx-env
```

This command starts a new container based on the `my-nginx-env` image, maps port 8080 on the host to port 8080 in the container, and sets the value of the `NGINX_PORT` variable to `8080`.

5. Verify that the web server is running by navigating to `http://localhost:8080` in your web browser.
