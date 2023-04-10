# Configure Nginx

Once Nginx is installed, it must be configured to work with other components. Follow these steps to do that:

1. Edit the Nginx configuration file `/etc/nginx/sites-available/default`:

```bash
sudo vim /etc/nginx/sites-available/default
```

2. Replace the existing content with the following:

```txt
server {
     listen 80 default_server;
     listen [::]:80 default_server;

     root /var/www/html;
     index index.php index.html index.htm index.nginx-debian.html;

     server_name _;

     location / {
            index index.php index.html index.htm;
        }

     location ~ \.php$ {
            fastcgi_pass unix:/run/php/php-fpm.sock;
            fastcgi_index index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            include fastcgi_params;
        }
}
```

3. Check if the Nginx configuration is correct:

```bash
sudo nginx -t
```

4. Reload nginx

```bash
sudo nginx -s reload
```
