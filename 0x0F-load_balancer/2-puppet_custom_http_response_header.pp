# Add a custom HTTP header with Puppet
exec { 'X-Served-By':
  command  => 'sudo apt-get update;
                sudo apt-get -y install nginx;
                echo "Hello World" > /var/www/html/index.nginx-debian.html
                sudo sed -i "/server_name _;/ a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default
                sudo sed -i "/server_name _;/ a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
                service nginx restart',
  provider => shell,
}
