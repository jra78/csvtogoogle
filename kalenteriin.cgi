#!/usr/bin/perl
#use strict;

use warnings;

use CGI;

print "Content-Type:application/octet-stream; name=\"csvtogoogle.csv\"\r\n";
print "Content-Disposition: attachment; filename=\"csvtogoogle.csv\"\r\n\n";

my $cgi=new CGI; #read in parameters

print "Subject, Start Date, End Date, All Day Event, Start Time, End Time, Location, Description, Private, All Day Event";
print "\r\n";
$countd=1;
$paivia=$cgi->param('paivia');
for ( $a=0; $a<= $paivia; $a++ ){
$d1="start$countd";
$d2="end$countd";
$d3="desc$countd";
$d4="date$countd";

$startdd=$cgi->param($d1);
$enddd=$cgi->param($d2);


if ($startdd eq $enddd ) {
#print nothing

}
else
{

print "\"" , $cgi->param($d3), "\"", "," ,$cgi->param($d4), "," ,$cgi->param($d4), "," , "FALSE" , "," ,$cgi->param($d1), "," ,$cgi->param($d2), "," , "," ,"työ" , "," , "TRUE" , "," , "FALSE";

print "\r\n";
}
$countd++;
}

1;
