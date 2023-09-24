#changes to our configuration file

file { 'ect/ssh/ssh_config':
  ensure  => present,
  path    => 'ect/ssh/ssh_config',
  centent => "
    #SSH configuration
    Host 
       PasswordAuthentication no
       IdentityFile ~/.ssh/school
",
}
