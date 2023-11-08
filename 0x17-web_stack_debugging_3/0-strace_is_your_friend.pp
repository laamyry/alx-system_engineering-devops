#fix phpp extention to php
exec { 'fix-php-extention':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin'
}