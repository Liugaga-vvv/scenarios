# Create a Docker Image

In this step, we will create a simple Docker image that contains a web server.

1. Create a new directory called `/home/labex/docker-lab` and navigate into it.

```bash
mkdir /home/labex/docker-lab
cd /home/labex/docker-lab
```

2. Create a file named `Dockerfile` with the following content:

```Dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/
```

This Dockerfile uses the latest version of the nginx image as the base image and copies an `index.html` file into the `/usr/share/nginx/html/` directory inside the container.

3. Create an `index.html` file with the following content:

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

4. Build the Docker image by running the following command:

```bash
docker build -t my-web-server .
```

This command builds a new Docker image with the tag `my-web-server` using the Dockerfile in the current directory. The `.` at the end of the command indicates that the build context is the current directory.
