#changes to our configuration file

file { 'ect/ssh/ssh_config':
  ensure  => present,
  centent => "
    host *
    IdentityFile ~/.ssh/school,
    PasswordAuthentication no,
",
}
