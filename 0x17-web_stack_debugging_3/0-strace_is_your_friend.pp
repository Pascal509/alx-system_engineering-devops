# This Puppet manifest fixes permission issues for Apache on Ubuntu 14.04

file { '/var/www/html':
  ensure  => 'directory',      # Ensures it is a directory
  owner   => 'www-data',       # Correct owner
  group   => 'www-data',       # Correct group
  mode    => '0755',           # Correct permissions
  require => Package['apache2'], # Dependency
}

# Ensure Apache is running
service { 'apache2':
  ensure     => running,
  enable     => true,
  subscribe  => File['/var/www/html'],
}
