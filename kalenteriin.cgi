#!/usr/bin/perl
#use strict;

use warnings;

use CGI;

print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";
print "<title>CSV to google calendar</title>";
print "</head>";
print "<body>";
print '<meta charset="UTF-8">'; 


my $cgi=new CGI; #read in parameters

print "Subject, Start Date, End Date, All Day Event, Start Time, End Time, Location, Description, Private, All Day Event";
print "<br>";
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

print "<br>";
}
$countd++;
}

print "</body>";
print "</html>";

1;
