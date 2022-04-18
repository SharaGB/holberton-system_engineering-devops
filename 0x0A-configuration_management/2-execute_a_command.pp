# Create a manifest that kills a process named killmenow.
exec { 'killmenow':
  command  => 'pkill -x killmenow',
  provider => shell,
}
