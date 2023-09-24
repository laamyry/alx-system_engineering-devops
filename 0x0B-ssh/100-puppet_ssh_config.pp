#changes to our configuration file

file_1 {  'no_password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_1 {  'password_place':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}