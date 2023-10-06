#!/usr/bin/env bash
# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

exec {'apt_update':
  command => '/usr/bin/apt-get -y update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'restart':
  command => '/usr/sbin/service nginx restart',
}
