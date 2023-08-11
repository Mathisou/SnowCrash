#!/usr/bin/perl
# localhost:4747
# use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  print "test";
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
