# Create A Simple Docker Image

The first step is to create a simple Docker image that runs a simple web server. We will use the `nginx` web server as an example.

1. Create a new directory called `docker` for this lab at this path `/home/labex`, and navigate to it.

```
mkdir docker
cd docker
```

2. Create a new file called `Dockerfile` in this directory, and add the following lines:

```Dockerfile
FROM nginx
COPY index.html /usr/share/nginx/html/
```

This Dockerfile defines a new image based on the official `nginx` image, and copies a file called `index.html` to the default document root directory of `nginx`.

3. Create a new file called `index.html`, and add some simple HTML content, such as:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Hello Docker!</title>
  </head>
  <body>
    <h1>Hello Docker!</h1>
  </body>
</html>
```

4. Build the Docker image using the following command:

```bash
docker build -t my-nginx .
```

This command builds a new Docker image with the tag `my-nginx`.

5. Verify that the image was created successfully by running the following command:

```bash
docker images
```

You should see the `my-nginx` image listed in the output.

6. Run a container based on the new image using the following command:

```bash
docker run -p 8080:80 my-nginx
```

This command starts a new container based on the `my-nginx` image, and maps port 8080 on the host to port 80 in the container. You should be able to access the web server by navigating to `http://localhost:8080` in your web browser.
