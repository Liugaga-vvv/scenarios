# Note

- Input `mkdir /tmp/nginx` command to create a directory.
- Input `docker run -d --name nginx-host -v /tmp/nginx:/usr/share/nginx/html nginx` command to create an `nginx` container with a host directory.
- Input `docker cp nginx.txt nginx-host:/usr/share/nginx/html/` command to copy the local file to the `nginx-host` container.
