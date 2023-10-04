#Install Nginx web server (w/ Puppet)

#check if nginx is installed
package { 'nginx':
  ensure => 'installed',
}

#check if nginx is running
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/laamyry permanent;',
}
#redirect_me
file { '/var/www/html/index.html':
  content => 'Hello World',
}

#start nginx
service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
