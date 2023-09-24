#changes to our configuration file

file1 { 'ect/ssh/ssh_config':
  path    => 'ect/ssh/ssh_config',
  content => 'PasswordAuthentication no',
}
file2 { 'ect/ssh/ssh_config':
  path    => 'ect/ssh/ssh_config',
  content => 'IdentityFile ~/.ssh/school',
}
