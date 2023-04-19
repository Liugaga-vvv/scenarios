# Backup And Restore A Docker Volume

To backup a Docker volume, you can create a tarball of the volume data using the `docker run` command with the `--rm` and `--volumes-from` options:

```bash
docker run --rm -itd --volumes-from c1 -v $(pwd):/backup centos tar cvf /backup/myvolume.tar.gz /app/data
```

This command creates a tarball of the `myvolume` volume data and saves it to the current directory on your host machine.

To restore a Docker volume from a backup, you can create a new volume and extract the tarball to the volume directory:

```bash
docker volume create mynewvolume
docker run -itd --name=back -v mynewvolume:/app/data centos
docker run -itd --volumes-from back -v $(pwd):/backup centos tar xvf /backup/myvolume.tar.gz
```

This command creates a new `mynewvolume` volume and extracts the tarball to the `/app/data` directory inside the container.
