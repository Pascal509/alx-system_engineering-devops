# This Puppet manifest ensures that Apache is installed, configured,
# and running with the correct permissions set on its web directory and necessary files.

# Ensure Apache package is installed
package { 'apache2':
  ensure => installed,
}

# Ensure the /var/www/html directory exists with the correct owner, group, and permissions
file { '/var/www/html':
  ensure  => 'directory',
  owner   => 'www-data',       # Usually, Apache runs as www-data in Ubuntu
  group   => 'www-data',
  mode    => '0755',
  require => Package['apache2'], # Dependency to ensure Apache is installed first
}

# Ensure the default index.html exists with correct permissions and content
file { '/var/www/html/index.html':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  content => "<html>\n<head>\n<title>Welcome</title>\n</head>\n<body>\n<p>Apache is running.</p>\n</body>\n</html>\n",
  require => File['/var/www/html'], # Ensures that the directory is set up before the file
}

# Ensure Apache is running and enabled to start at boot
service { 'apache2':
  ensure    => running,
  enable    => true,
  require   => Package['apache2'], # Ensures that the package is installed first
}

# Ensure mod_rewrite is enabled, but only after Apache is installed
exec { 'enable-mod-rewrite':
  command     => 'a2enmod rewrite && systemctl restart apache2',
  path        => ['/bin', '/usr/bin', '/usr/sbin'],
  unless      => '/usr/sbin/a2query -m rewrite | grep enabled',
  require     => Package['apache2'], # Ensures that Apache is installed before attempting to enable modules
  notify      => Service['apache2'], # Restart Apache service to apply changes
}
