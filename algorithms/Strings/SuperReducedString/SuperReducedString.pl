#!/bin/perl

# hackerrank.com/challenges/reduced-string
my $str = <STDIN>;
while ($str =~ s/(.)\1//g){};
if ($str) {
  print $str;
} else {
  print "Empty String";
}
