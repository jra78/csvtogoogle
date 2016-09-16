#!/usr/bin/perl

use CGI;

print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";
print "<title>Maraplan to google calendar</title>";
print "</head>";
print "<body>";
print '<meta charset="UTF-8">'; 



#how many works days
my $cgi=new CGI; #read in parameters
use Time::Local;
#                   sec, min hour, day, mon,  year

#$cgi->param('sdate'), $cgi->param('smonth'), $cgi->param('syear')
#$cgi->param('esate'), $cgi->param('emonth'), $cgi->param('eyear')

$alpaiv=$cgi->param('sdate');
$alkuuk=$cgi->param('smonth');
$alvuosi=$cgi->param('syear');

$alkuuk=$alkuuk-1;



$loppaiv=$cgi->param('edate');
$lopkuu=$cgi->param('vittu');
$lopvuosi=$cgi->param('eyear');

$lopkuu=$lopkuu-1;



$lopetuspv = timelocal(0, 0,  0, "$loppaiv", "$lopkuu", "$lopvuosi" );
$aloituspv = timelocal(0, 0,  0, "$alpaiv", "$alkuuk", "$alvuosi");

$paivia=$lopetuspv - $aloituspv;
$paivia= $paivia/86400;



#make boxes for each day
print '<FORM action="/cgi-bin/kalenteriin.cgi" method="POST">';
$countd=1;
print "Anna aloitus- ja lopetusaika (xx:xx muodossa) sekä kuvaus";
for ( $a=0; $a<= $paivia; $a++ ){
print "<br>";

use Time::localtime;
$tm = localtime($aloituspv);
printf(" %02d.%02d. %04d\n", $tm->mday,$tm->mon+1,$tm->year+1900);
$d1=$tm->mday;
$d2=$tm->mon+1;
$d3=$tm->year+1900;
print "<input type=\"hidden\" name=\"date$countd\" value=\"$d1\/$d2\/$d3\"> " ;


print "<input type=\"text\" name=\"start$countd\" value=\"$countd\" maxlength=\"5\" pattern=\"[0-9:]{5}\"> " ;
print "<input type=\"text\" name=\"end$countd\" maxlength=\"5\" pattern=\"[0-9:]{5}\"> " ;
print "<input type=\"text\" name=\"desc$countd\"maxlength=\"30\" pattern=\"[A-Za-z0-9^;]{0-30}\">  <br>" ;

$countd++;
$aloituspv=$aloituspv+86400;
}
#$paivia++;
print "<input type=\"hidden\" name=\"paivia\" value=\"$paivia\" maxlength=\"2\">  <br>" ;
print "Kopioi seuraava sivu, tallenna se \".csv\" päätteen kanssa ja anna googlen kalenterin tehdä \"taikojaan\" \"Tuo kalenteri\" toiminnon kautta";
print '<input type="submit" value="Submit">';
print "</FORM>";


print "</body>";
print "</html>";

1;
