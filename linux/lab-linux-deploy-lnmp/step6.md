# Configure PHP

1. Create and edit a new phpinfo.php file to display PHP information.

```bash
sudo vim /var/www/html/phpinfo.php
```

Write the following content.

```txt
<?php echo phpinfo(); ?>
```

> Tips: Where `/var/www/html` is the site root directory, which can be viewed by running the `cat /etc/nginx/sites-enabled/default` command.

2. Start PHP-FPM: Once the installation is complete, start the PHP-FPM service using the following command.

```bash
sudo systemctl start php8.1-fpm
```

> Tips: Note that the exact name of the PHP-FPM service may differ depending on your Linux distribution and PHP version.

3. Enable PHP-FPM to start on boot: To ensure that PHP-FPM starts automatically when the server boots up, run the following command.

```bash
sudo systemctl enable php8.1-fpm
```
