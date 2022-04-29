# Add a custom HTTP header with Puppet
# exec { 'X-Served-By':
#  command  => 'sudo apt-get update;
#                sudo apt-get -y install nginx;
#                echo "Hello World" > /var/www/html/index.nginx-debian.html
#                sudo sed -i "/server_name _;/ a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default
#                sudo sed -i "/server_name _;/ a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
#                service nginx restart',
#  provider => shell,
# }  It also works!

exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file { '/var/www/html/index.html':
  content => 'Hello World',
  require => Package['nginx'],
}

file_line { '/redirect_me 301':
  ensure  => present,
  after   => 'listen 80 default_server;',
  path    => '/etc/nginx/sites-available/default',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
}

file_line { 'X-Served-By':
  ensure  => present,
  after   => 'listen 80 default_server;',
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $HOSTNAME;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
