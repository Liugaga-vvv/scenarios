# Note

- Input `docker volume create nginx-vol` command to create a data volume
- Input `docker volume ls` command to list data volumes
- Input `docker run -d --name nginx --mount source=nginx-vol,target=/usr/share/nginx/html nginx` command to create an `nginx` container with a data volume.
- Input `docker cp index.html nginx:/usr/share/nginx/html/` command to copy the local file to the `nginx` container.
