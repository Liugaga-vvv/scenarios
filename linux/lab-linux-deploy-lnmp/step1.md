# Install Nginx

Sure, here are the specific steps to install `Nginx` on a Linux system:

1. Update package lists: Run the following command to update the package lists on the server:

```bash
sudo apt-get update
```

2. Use the following command to install Nginx:

```bash
sudo apt-get install nginx=1.18.0-6ubuntu14.3
```

3. Check if `Nginx` is installed successfully

```bash
nginx -v
```

The following image indicates that `Nginx` was installed successfully, and the currently installed version is `1.18.0`.

![lab-linux-deploy-lnmp-1-1](assets/lab-linux-deploy-lnmp-1-1.png)
