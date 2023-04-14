# Note

- Input `docker volume create my-vol` command to create a data volume
- Input `docker volume ls` command to list data volumes
- Input `docker volume inspect my-vol` command to inspect the data volume
- Input `docker run -d --name nginx --mount source=nginx-vol,target=/usr/share/nginx/html nginx` command to create an nginx container with a data volume.
- Input `docker cp index.html nginx:/usr/share/nginx/html/` command to copy the local file to the nginx container.
- Input `docker run -d --name nginx-host -v /tmp/nginx:/usr/share/nginx/html nginx` command to create an nginx container with a host directory.
- Input `docker run -d --name busybox-share --volumes-from nginx-share busybox sleep 3000` command to Create a busybox container with shared nginx container data volume.
