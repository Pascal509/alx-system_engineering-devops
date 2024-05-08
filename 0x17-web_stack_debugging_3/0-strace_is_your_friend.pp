# This Puppet manifest fixes permission issues for Apache on Ubuntu 14.04

# Ensure Apache package is installed
package { 'apache2':
  ensure => installed,
}

file { '/var/www/html':
  ensure  => 'directory',      # Ensures it is a directory
  owner   => 'root',       # Correct owner
  group   => 'root',       # Correct group
  mode    => '0755',           # Correct permissions
  before => File['/var/www/html/index.html'],  # This ensures the directory is created before the file
}

# Ensure the needed file exists with correct permissions and content
file { '/path/to/needed/file':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "Content of the file\n",
}

# Ensure Apache is running
service { 'apache2':
  ensure     => running,
  enable     => true,
  require   => Package['apache2'], # Ensures that the package is installed first
}

exec { 'enable-mod-rewrite':
  command     => 'a2enmod rewrite',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,  # Only run this exec if notified by another resource
  subscribe   => Package['apache2'],  # This command runs after the apache2 package is handled
  notify      => Service['apache2'],  # Notify the apache service to restart after running this command
}
