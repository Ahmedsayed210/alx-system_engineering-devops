Bwwddadad
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
C
C
C
C
C
C
C
C
C
C
# Create file in /tmp

file { '/tmp/school' :
    path    => '/tmp/school',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
    }
