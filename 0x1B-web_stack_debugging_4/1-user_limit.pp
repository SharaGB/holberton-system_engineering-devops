# Change the default number of open files limit
exec { 'Holberton-hard-soft':
  environment => ['HARD_OLD=hard nofile 5',
                  'HARD_NEW=hard nofile 4096',
                  'SOFT_OLD=soft nofile 4',
                  'SOFT_NEW=soft nofile 4096'],
  command     => 'sudo sed -i "s/$HARD_OLD/$HARD_NEW/" /etc/security/limits.conf; \
                    sudo sed -i "s/$SOFT_OLD/$SOFT_NEW/" /etc/security/limits.conf',
  provider    => shell,
  returns     => [0, 1],
}
