# Add a custom HTTP header with Puppet
file_line {'X-Served-By':
    after => 'server_name _;',
    path  => '/etc/nginx/sites-available/default',
    line  => 'add_header X-Served-By $HOSTNAME',
}
