#changes to our configuration file

file_line {  'no_password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line {  'password_place':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}