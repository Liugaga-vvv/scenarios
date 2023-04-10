# Note

- Input `mkdir /tmp/share` command to create a directory.
- Input `docker run -d --name nginx-share -v /tmp/share:/usr/share/nginx/html nginx` command to create an `nginx` container with a host directory.
- Input `docker run -d --name busybox-share --volumes-from nginx-share busybox sleep 3000` command to Create a `busybox` container with shared the `nginx` container data volume.
- Input `docker cp share.txt nginx-share:/usr/share/nginx/html/` command to copy the local file to the `nginx-share` container.
- Imnp `docker exec -it busybox-share cat share.txt` command to check the file exists in the `busybox-share` container.
