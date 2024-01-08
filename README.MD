$> passive --help

Welcome to passive v1.0.0

OPTIONS:
-fn Search with full-name
-ip Search with ip address
-u Search with username

$> passive -fn "Jean Dupont"
First name: Jean
Last name: Dupont
Address: 7 rue du Progrès
75016 Paris
Number: +33601010101
Saved in result.txt

$> passive -ip 127.0.0.1
ISP: FSociety, S.A.
City Lat/Lon: (13.731) / (-1.1373)
Saved in result2.txt

$> passive -u "@user01"
Facebook : yes
Twitter : yes
Linkedin : yes
Instagram : no
Skype : yes
Saved in result3.txt
