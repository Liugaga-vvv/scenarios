# Install MySQL

Here are the specific steps to install MySQL on a Linux system:

1. Use the following command to install MySQL:

```bash
sudo apt-get install mysql-server=8.0.32-0ubuntu0.22.04.2
```

2. Check if the MySQL server is installed:

```bash
mysql --version
```

The following figure indicates that MySQL is successfully installed.

![lab-linux-deploy-lnmp-2-1](assets/lab-linux-deploy-lnmp-2-1.png)

3. Check if MySQL is started, and if not, start it with the following command.

```bash
sudo systemctl status mysql
sudo systctl start mysql
```
