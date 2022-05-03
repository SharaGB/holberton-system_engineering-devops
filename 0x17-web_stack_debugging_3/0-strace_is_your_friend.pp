# Using strace, find out why Apache is returning a 500 error

exec { 'Fix_error_500':
    command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
    provider => shell,
}
