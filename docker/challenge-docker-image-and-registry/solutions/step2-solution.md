# Note

1. Use `echo "hello labex" > /home/labex/Code/index.html` command to create a file named `index.html` in the home directory.
2. Use `docker build -t your_dockerhub_id/web:1.1.0 .` command to build a docker image named `your_dockerhub_id/web:1.1.0`.
3. Use `docker push your_dockerhub_id/web:1.1.0` command to push the image to your `dockerhub`.
4. Use `docker run --name web -d -p 80:80 your_dockerhub_id/web:1.1.0` command to start the container.
