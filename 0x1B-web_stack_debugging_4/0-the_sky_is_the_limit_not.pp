# Fix Nginx Failure Under High Volume Requests
exec { 'ULIMITE':
  environment => ['OLD=ULIMIT="-n 15"',
                  'NEW=ULIMIT="-n 4096"'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" /etc/default/nginx; service nginx restart',
  provider    => shell,
  returns     => [0, 1],
}
