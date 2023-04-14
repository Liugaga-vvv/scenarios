# Note

1. Use `docker build -t your_dockerhub_id/go-hello-world:1.1.0 .` command to build a docker image named `your_dockerhub_id/go-hello-world:1.1.0`.
2. Use `docker push your_dockerhub_id/go-hello-world:1.1.0` command to push the image to your `dockerhub`.
3. Use `docker run --name go-hello-world -d -p 8080:8080 your_dockerhub_id/go-hello-world:1.1.0` command to start the container.
