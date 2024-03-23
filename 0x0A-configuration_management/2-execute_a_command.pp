# Manifest file: kill process

exec { 'killmenow':
  command     => '/bin/pkill -f killmenow',
  path        => ['/bin', '/usr/local/bin/'],
  refreshonly => true,
}
