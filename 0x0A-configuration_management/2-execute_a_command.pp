# Create a manifest that kills a process named killmenow.
exec { 'killmenow':
  command  => 'pkill -f killmenow',
  provider => shell,
}
