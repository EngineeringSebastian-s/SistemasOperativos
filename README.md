# SistemasOperativos



## Clase 07 de Septiembre del 2024


```bash
┌──(root㉿kali)-[/home/kali/Desktop]
└─# pico nomina

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '{print $1}' nomina
Rufina
Cinforosa
Matea
Anacarota
Bertulia
Rufina
Matea
Ana


┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '{print $1,$2,$3,$6}' nomina
Rufina Toro Pérez 860000
Cinforosa García Tobar 1700000
Matea Patiño Puerta 3000000
Anacarota Toro Rico 1700000
Bertulia Ruiz Moreno 860000
Rufina Toro Gómez 3000000
Matea Peña Toro 3000000
Ana Perez Botero 1700000


┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '{print $1 $2 $3 $6}' nomina
RufinaToroPérez860000
CinforosaGarcíaTobar1700000
MateaPatiñoPuerta3000000
AnacarotaToroRico1700000
BertuliaRuizMoreno860000
RufinaToroGómez3000000
MateaPeñaToro3000000
AnaPerezBotero1700000


┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$3~ /Rico/ {print $0}' nomina
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$3~ /Rico/ {print $0}' nomina>nomina12

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk nomina12
^X^C

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '{print}'  nomina12
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# more nomina12
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Solte
ra

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /Toro/ {print $0}' nomina
Rufina  Toro    Pérez   Ninguno Secretaria      860000  Soltera
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Soltera
Rufina  Toro    Gómez   Ingeniera       Analista        3000000 Casada

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /Toro/ && $6~ >1600000 {print $0}' nomina
awk: cmd. line:1: $2~ /Toro/ && $6~ >1600000 {print $0}
awk: cmd. line:1:                   ^ syntax error

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /Toro/ && $6>1600000 {print $0}' nomina
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Soltera
Rufina  Toro    Gómez   Ingeniera       Analista        3000000 Casada

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /Toro/ && $6>1600000 {print $0}' nomina>nomina14

┌──(root㉿kali)-[/home/kali/Desktop]
└─# more nomina14
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Solte
ra
Rufina  Toro    Gómez   Ingeniera       Analista        3000000 Casada

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /Ruiz/ ||  $6<1800000 {print $0}' nomina
Rufina  Toro    Pérez   Ninguno Secretaria      860000  Soltera
Cinforosa       García  Tobar   Tecnóloga       Programador     1700000 Casada
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Soltera
Bertulia        Ruiz    Moreno  Ninguno Secretaria      860000  Casada
Ana     Perez   Botero  Tecnóloga       Programador     1700000 Casada


┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /Ruiz/ ||  $6<1800000 {print $0}' nomina>nomina16

┌──(root㉿kali)-[/home/kali/Desktop]
└─# more nomina16
Rufina  Toro    Pérez   Ninguno Secretaria      860000  Soltera
Cinforosa       García  Tobar   Tecnóloga       Programador     1700000 Casad
a
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Solte
ra
Bertulia        Ruiz    Moreno  Ninguno Secretaria      860000  Casada
Ana     Perez   Botero  Tecnóloga       Programador     1700000 Casada


┌──(root㉿kali)-[/home/kali/Desktop]
└─# less nomina16

zsh: suspended  less nomina16

┌──(root㉿kali)-[/home/kali/Desktop]
└─# less nomina16

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$7~ /Soltera/ &&  $6>800000 {print $0}' nomina
Rufina  Toro    Pérez   Ninguno Secretaria      860000  Soltera
Matea   Patiño  Puerta  Ingeniera       Analista        3000000 Soltera
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Soltera
Matea   Peña    Toro    Ingeniera       Analista        3000000 Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$7~ /Soltera/ &&  $6>800000 && $1~ /a$/ {print $0}' nomina
Rufina  Toro    Pérez   Ninguno Secretaria      860000  Soltera
Matea   Patiño  Puerta  Ingeniera       Analista        3000000 Soltera
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Soltera
Matea   Peña    Toro    Ingeniera       Analista        3000000 Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$7~ /Soltera/ &&  $6>800000 && $1~ /a$/ {print $0}' nomina>nomina18

┌──(root㉿kali)-[/home/kali/Desktop]
└─# more nomina18
Rufina  Toro    Pérez   Ninguno Secretaria      860000  Soltera
Matea   Patiño  Puerta  Ingeniera       Analista        3000000 Soltera
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Solte
ra
Matea   Peña    Toro    Ingeniera       Analista        3000000 Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$1~ /^R/ && $2~ /o$/ && $3~ /z$/ && $7~ /Soltera/ {print $0}' nomina
Rufina  Toro    Pérez   Ninguno Secretaria      860000  Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$1~ /^R/ && $2~ /o$/ && $3~ /z$/ && $7~ /Soltera/ {print $0}' nomina>nomina20

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$1~ /a$/ && $2~ /^t/ && $5~ /Analista/ {print $0}' nomina

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$1~ /a$/ && $2~ /^t/ && $5~ /Analista/ && $7~ /Casada/ {print $0}' nomina

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /a$/ && $3~ /^t/ && $5~ /Analista/ && $7~ /Casada/ {print $0}' nomina

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /a$/ && $3~ /^t/ && $5~ /Analista/ && $7~ /Casada/ {print $0}' nomina>nomina22

┌──(root㉿kali)-[/home/kali/Desktop]
└─# cat nomina
Rufina  Toro    Pérez   Ninguno Secretaria      860000  Soltera
Cinforosa       García  Tobar   Tecnóloga       Programador     1700000 Casada
Matea   Patiño  Puerta  Ingeniera       Analista        3000000 Soltera
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Soltera
Bertulia        Ruiz    Moreno  Ninguno Secretaria      860000  Casada
Rufina  Toro    Gómez   Ingeniera       Analista        3000000 Casada
Matea   Peña    Toro    Ingeniera       Analista        3000000 Soltera
Ana     Perez   Botero  Tecnóloga       Programador     1700000 Casada


┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /a$/ && $3~ /^t/ && $5~ /Analista/ && $7~ /Soltera/ {print $0}' nomina>nomina22

┌──(root㉿kali)-[/home/kali/Desktop]
└─# cat nomina22

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /a$/ && $3~ /^t/ && $5~ /Analista/ && $7~ /Soltera/ {print $0}' nomina

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /a$/ && $3~ /^T/ && $5~ /Analista/ && $7~ /Soltera/ {print $0}' nomina
Matea   Peña    Toro    Ingeniera       Analista        3000000 Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~ /a$/ && $3~ /^T/ && $5~ /Analista/ && $7~ /Soltera/ {print $0}' nomina>nomina22

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ls -l nomina22
-rw-r--r-- 1 root root 52 Sep  7 13:01 nomina22

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ls -l nomina22 | awk '{print $1,$9}'
-rw-r--r-- nomina22

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2! /Toro/ && $7~ /Soltera/ && $1~ /a$/ {print $0}' nomina
Rufina  Toro    Pérez   Ninguno Secretaria      860000  Soltera
Matea   Patiño  Puerta  Ingeniera       Analista        3000000 Soltera
Anacarota       Toro    Rico    Tecnóloga       Programador     1700000 Soltera
Matea   Peña    Toro    Ingeniera       Analista        3000000 Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2!~ /Toro/ && $7~ /Soltera/ && $1~ /a$/ {print $0}' nomina
Matea   Patiño  Puerta  Ingeniera       Analista        3000000 Soltera
Matea   Peña    Toro    Ingeniera       Analista        3000000 Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2~~ /Toro/ && $7~ /Soltera/ && $1~ /a$/ {print $0}' nomina
awk: cmd. line:1: $2~~ /Toro/ && $7~ /Soltera/ && $1~ /a$/ {print $0}
awk: cmd. line:1:    ^ syntax error

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2!~ /Toro/ && $7~ /Soltera/ && $1~ /a$/ {print $0}' nomina
Matea   Patiño  Puerta  Ingeniera       Analista        3000000 Soltera
Matea   Peña    Toro    Ingeniera       Analista        3000000 Soltera

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2!~ /Toro/ && $7~ /Soltera/ && $1~ /a$/ {print $0}' nomina>24

┌──(root㉿kali)-[/home/kali/Desktop]
└─# awk '$2!~ /Toro/ && $7~ /Soltera/ && $1~ /a$/ {print $0}' nomina>nomina24

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.6  22640 13012 ?        Ss   09:11   0:00 /sbin/init
root           2  0.0  0.0      0     0 ?        S    09:11   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    09:11   0:00 [pool_work
root           4  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root           5  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root           6  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root           7  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          11  0.0  0.0      0     0 ?        I    09:11   0:00 [kworker/u
root          12  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          13  0.0  0.0      0     0 ?        I    09:11   0:00 [rcu_tasks
root          14  0.0  0.0      0     0 ?        I    09:11   0:00 [rcu_tasks
root          15  0.0  0.0      0     0 ?        I    09:11   0:00 [rcu_tasks
root          16  0.0  0.0      0     0 ?        S    09:11   0:00 [ksoftirqd
root          17  0.0  0.0      0     0 ?        I    09:11   0:02 [rcu_preem
root          18  0.0  0.0      0     0 ?        S    09:11   0:00 [migration
root          19  0.0  0.0      0     0 ?        S    09:11   0:00 [idle_inje
root          20  0.0  0.0      0     0 ?        S    09:11   0:00 [cpuhp/0]
root          21  0.0  0.0      0     0 ?        S    09:11   0:00 [cpuhp/1]
root          22  0.0  0.0      0     0 ?        S    09:11   0:00 [idle_inje
root          23  0.0  0.0      0     0 ?        S    09:11   0:00 [migration
root          24  0.0  0.0      0     0 ?        S    09:11   0:00 [ksoftirqd
root          26  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/1
root          31  0.0  0.0      0     0 ?        S    09:11   0:00 [kdevtmpfs
root          32  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          33  0.0  0.0      0     0 ?        S    09:11   0:00 [kauditd]
root          35  0.0  0.0      0     0 ?        S    09:11   0:00 [khungtask
root          36  0.0  0.0      0     0 ?        S    09:11   0:00 [oom_reape
root          38  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          39  0.0  0.0      0     0 ?        S    09:11   0:00 [kcompactd
root          40  0.0  0.0      0     0 ?        SN   09:11   0:00 [ksmd]
root          41  0.0  0.0      0     0 ?        SN   09:11   0:00 [khugepage
root          42  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          43  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          44  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          45  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          46  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          47  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          49  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/0
root          50  0.0  0.0      0     0 ?        S    09:11   0:00 [kswapd0]
root          57  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          59  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          60  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          61  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          66  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root          68  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u
root          69  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u
root          70  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u
root          80  0.0  0.0      0     0 ?        I    09:11   0:00 [kworker/u
root         168  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/1
root         171  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root         177  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root         182  0.0  0.0      0     0 ?        S    09:11   0:00 [irq/18-vm
root         183  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root         188  0.0  0.0      0     0 ?        S    09:11   0:00 [scsi_eh_0
root         195  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root         196  0.0  0.0      0     0 ?        S    09:11   0:00 [scsi_eh_1
root         197  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root         203  0.0  0.0      0     0 ?        S    09:11   0:00 [scsi_eh_2
root         204  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
root         242  0.0  0.0      0     0 ?        I    09:11   0:02 [kworker/0
root         245  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/0
root         278  0.0  0.0      0     0 ?        S    09:12   0:00 [jbd2/sda1
root         279  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/R
root         336  0.0  1.0  51420 20872 ?        Ss   09:12   0:00 /usr/lib/s
root         371  0.0  0.0      0     0 ?        I    09:12   0:00 [kworker/u
root         395  0.0  0.3  29324  7728 ?        Ss   09:12   0:00 /usr/lib/s
root         448  0.0  0.3   8276  6084 ?        Ss   09:12   0:00 /usr/sbin/
root         475  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/R
root         476  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/R
root         496  0.0  0.0      0     0 ?        S    09:12   0:00 [psimon]
root         762  0.0  0.4 310992  9700 ?        Ssl  09:12   0:00 /usr/libex
root         763  0.0  0.1   6652  2560 ?        Ss   09:12   0:00 /usr/sbin/
message+     764  0.0  0.2  10740  5760 ?        Ss   09:12   0:01 /usr/bin/d
polkitd      767  0.0  0.5 384376 10224 ?        Ssl  09:12   0:00 /usr/lib/p
root         769  0.0  0.4  18992  8960 ?        Ss   09:12   0:00 /usr/lib/s
root         801  0.0  1.1 335636 23528 ?        Ssl  09:12   0:00 /usr/sbin/
root         810  0.0  0.1 293028  3332 ?        Sl   09:12   0:01 /usr/sbin/
root         818  0.0  0.7 392236 14420 ?        Ssl  09:12   0:00 /usr/sbin/
root         867  0.0  0.3 380380  7096 ?        SLsl 09:12   0:00 /usr/sbin/
root         880  0.0  0.1   9480  2944 tty1     Ss+  09:12   0:00 /sbin/aget
root         881  0.2  8.0 492500 163900 tty7    Ssl+ 09:12   0:32 /usr/lib/x
root         906  0.0  0.0      0     0 ?        S    09:12   0:00 [psimon]
rtkit        936  0.0  0.1  22824  3200 ?        SNsl 09:12   0:00 /usr/libex
root        1006  0.0  0.4 234384  8120 ?        Sl   09:13   0:00 lightdm --
kali        1013  0.0  0.5  21248 11776 ?        Ss   09:13   0:00 /usr/lib/s
kali        1014  0.0  0.1  21904  3256 ?        S    09:13   0:00 (sd-pam)
kali        1029  0.0  0.7 117360 15116 ?        S<sl 09:13   0:00 /usr/bin/p
kali        1030  0.0  0.2  95252  6016 ?        Ssl  09:13   0:00 /usr/bin/p
kali        1033  0.0  1.8 642448 37960 ?        S<sl 09:13   0:00 /usr/bin/w
kali        1034  0.0  0.4 101496  9600 ?        S<sl 09:13   0:00 /usr/bin/p
kali        1035  0.0  0.6 314332 12240 ?        SLsl 09:13   0:00 /usr/bin/g
kali        1036  0.0  0.2   9864  5608 ?        Ss   09:13   0:00 /usr/bin/d
kali        1059  0.0  1.3 339248 26772 ?        Ssl  09:13   0:00 xfce4-sess
kali        1113  0.0  0.0  17148  1536 ?        S    09:13   0:00 /usr/bin/V
kali        1114  0.0  0.2 215336  4096 ?        Sl   09:13   0:00 /usr/bin/V
kali        1128  0.0  0.0  17148  1536 ?        S    09:13   0:00 /usr/bin/V
kali        1129  0.0  0.1 215444  3200 ?        Sl   09:13   0:06 /usr/bin/V
kali        1136  0.0  0.0  17148  1536 ?        S    09:13   0:00 /usr/bin/V
kali        1137  0.1  0.1 215960  3200 ?        Sl   09:13   0:17 /usr/bin/V
kali        1149  0.0  0.0   9736  1568 ?        Ss   09:13   0:00 /usr/bin/s
kali        1160  0.0  0.4 383180  9952 ?        Ssl  09:13   0:00 /usr/libex
kali        1167  0.0  0.2   9444  4864 ?        S    09:13   0:00 /usr/bin/d
kali        1178  0.0  0.5 236432 10272 ?        Sl   09:13   0:00 /usr/libex
kali        1191  0.0  0.2  81252  5432 ?        SLs  09:13   0:00 /usr/bin/g
kali        1193  0.1  2.1 388712 44136 ?        Sl   09:13   0:15 xfwm4
kali        1197  0.0  0.4 311936  9720 ?        Ssl  09:13   0:00 /usr/libex
kali        1203  0.0  0.5 457364 11252 ?        Sl   09:13   0:00 /usr/libex
kali        1218  0.0  0.0  17148  1792 ?        S    09:13   0:00 /usr/bin/V
kali        1219  0.0  0.1 215552  3840 ?        Sl   09:13   0:01 /usr/bin/V
kali        1223  0.0  1.4 303808 30148 ?        Sl   09:13   0:01 xfsettings
root        1227  0.0  0.5 315732 11200 ?        Ssl  09:13   0:00 /usr/libex
kali        1233  0.0  2.2 460832 45976 ?        Sl   09:13   0:01 xfce4-pane
kali        1238  0.0  1.3 413104 28024 ?        Sl   09:13   0:00 Thunar --d
kali        1249  0.0  4.9 562064 99328 ?        Sl   09:13   0:03 xfdesktop
kali        1253  0.0  2.4 534612 48756 ?        Sl   09:13   0:00 /usr/lib/x
kali        1257  0.0  2.7 515204 55320 ?        Sl   09:13   0:00 /usr/bin/p
kali        1259  0.0  0.9 259400 19856 ?        Sl   09:13   0:00 xfce4-powe
kali        1261  0.0  0.9 258432 18596 ?        Sl   09:13   0:00 /usr/lib/p
kali        1263  0.0  1.5 413700 30400 ?        Sl   09:13   0:00 light-lock
kali        1269  0.0  0.1  12632  2220 ?        Ssl  09:13   0:00 xcape -e S
kali        1271  0.0  0.4 307944  8704 ?        Sl   09:13   0:00 xiccd
kali        1279  0.0  2.3 619840 47496 ?        Sl   09:13   0:00 nm-applet
kali        1288  0.0  0.2 230356  5632 ?        Ssl  09:13   0:00 /usr/libex
kali        1290  0.0  1.8  62380 36736 ?        S    09:13   0:00 /usr/bin/p
colord      1295  0.0  0.8 317868 16396 ?        Ssl  09:13   0:00 /usr/libex
kali        1309  0.0  1.0 408860 22104 ?        Ssl  09:13   0:01 /usr/lib/x
kali        1319  0.0  0.4 307952  8188 ?        Sl   09:13   0:00 /usr/libex
kali        1388  0.1  2.6 363316 53884 ?        Sl   09:13   0:21 /usr/lib/x
kali        1389  0.0  1.4 411988 29404 ?        Sl   09:13   0:00 /usr/lib/x
kali        1390  0.1  1.5 340272 32020 ?        Sl   09:13   0:22 /usr/lib/x
kali        1391  0.0  2.0 455764 41100 ?        Sl   09:13   0:00 /usr/lib/x
kali        1392  0.0  2.2 458784 44708 ?        Sl   09:13   0:00 /usr/lib/x
kali        1393  0.0  2.2 385824 45992 ?        Sl   09:13   0:00 /usr/lib/x
kali        1402  0.0  2.0 385460 41252 ?        Sl   09:13   0:00 /usr/lib/x
kali        1450  0.0  0.3  49204  7936 ?        Ss   09:13   0:00 /usr/libex
kali        1463  0.0  0.8 425988 17044 ?        Ssl  09:13   0:00 /usr/libex
root        1467  0.0  0.8 470200 17776 ?        Ssl  09:13   0:00 /usr/libex
kali        1476  0.0  0.5 388476 10208 ?        Ssl  09:13   0:00 /usr/libex
kali        1482  0.0  0.5 307440 10748 ?        Ssl  09:13   0:00 /usr/libex
kali        1487  0.0  0.4 307416  8460 ?        Ssl  09:13   0:00 /usr/libex
kali        1492  0.0  0.5 308400 10816 ?        Ssl  09:13   0:00 /usr/libex
kali        1502  0.0  0.5 533248 10920 ?        Sl   09:13   0:00 /usr/libex
kali        1510  0.0  0.4 233948  8596 ?        Ssl  09:13   0:00 /usr/libex
root       28408  0.0  0.0      0     0 ?        I    10:09   0:02 [kworker/1
root       68526  0.0  0.0      0     0 ?        I    11:33   0:00 [kworker/u
kali       82069  0.1  4.8 453944 98716 ?        Sl   12:01   0:05 /usr/bin/q
kali       82072  0.0  0.3  10344  6456 pts/0    Ss   12:01   0:00 /usr/bin/z
root       82162  0.0  0.3  17760  6780 pts/0    S+   12:01   0:00 sudo su
root       82187  0.0  0.1  17760  2336 pts/1    Ss   12:01   0:00 sudo su
root       82188  0.0  0.2   9196  4096 pts/1    S    12:01   0:00 su
root       82189  0.2  0.3  10640  6856 pts/1    S    12:01   0:09 zsh
root       86062  0.0  0.0      0     0 ?        I    12:09   0:00 [kworker/1
root       86751  0.0  0.0      0     0 ?        I    12:10   0:00 [kworker/u
root       88311  0.0  0.1   5896  2560 pts/1    T    12:14   0:00 less nomin
root      100868  0.0  0.1   5896  2560 pts/1    T    12:39   0:00 less nomin
root      101019  0.0  0.0      0     0 ?        I    12:39   0:00 [kworker/u
root      101084  0.0  0.0      0     0 ?        I    12:39   0:00 [kworker/0
root      107841  0.0  0.0      0     0 ?        I    12:53   0:00 [kworker/u
root      108050  0.0  0.0      0     0 ?        I    12:53   0:00 [kworker/u
kali      112916  0.0  0.4 307180  8172 ?        Sl   13:03   0:00 /usr/lib/x
root      114065  0.0  0.0      0     0 ?        I    13:05   0:00 [kworker/0
kali      114287  0.2  1.5 646448 30580 ?        SNsl 13:05   0:00 /usr/lib/x
root      114483  0.0  0.2  12140  4992 pts/1    R+   13:06   0:00 ps -aux

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux | more
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.6  22640 13012 ?        Ss   09:11   0:00 /sbin/init
 splash
root           2  0.0  0.0      0     0 ?        S    09:11   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    09:11   0:00 [pool_work
queue_release]
root           4  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-rcu_g]
root           5  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-rcu_p]
root           6  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-slub_]
root           7  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-netns]
root          11  0.0  0.0      0     0 ?        I    09:11   0:00 [kworker/u
4:0-ext4-rsv-conversion]
root          12  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-mm_pe]
root          13  0.0  0.0      0     0 ?        I    09:11   0:00 [rcu_tasks
_kthread]
root          14  0.0  0.0      0     0 ?        I    09:11   0:00 [rcu_tasks
_rude_kthread]
root          15  0.0  0.0      0     0 ?        I    09:11   0:00 [rcu_tasks
_trace_kthread]
root          16  0.0  0.0      0     0 ?        S    09:11   0:00 [ksoftirqd
/0]

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux | more | awk '$2>50 {print $0}'
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          57  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-kthro]
root          59  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-acpi_]
root          60  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-mld]
root          61  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-ipv6_]
root          66  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-kstrp]
root          68  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u7:0]
root          69  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u8:0]
root          70  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u9:0]
root          80  0.0  0.0      0     0 ?        I    09:11   0:00 [kworker/u6:2-writeback]
root         168  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/1:1H-kblockd]
root         171  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-crypt]
root         177  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-ata_s]
root         182  0.0  0.0      0     0 ?        S    09:11   0:00 [irq/18-vmwgfx]
root         183  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-ttm]
root         188  0.0  0.0      0     0 ?        S    09:11   0:00 [scsi_eh_0]
root         195  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-scsi_]
root         196  0.0  0.0      0     0 ?        S    09:11   0:00 [scsi_eh_1]
root         197  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-scsi_]
root         203  0.0  0.0      0     0 ?        S    09:11   0:00 [scsi_eh_2]
root         204  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-scsi_]
root         242  0.0  0.0      0     0 ?        I    09:11   0:02 [kworker/0:4-events]
root         245  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/0:2H-kblockd]
root         278  0.0  0.0      0     0 ?        S    09:12   0:00 [jbd2/sda1-8]
root         279  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/R-ext4-]
root         336  0.0  0.8  51420 16984 ?        Ss   09:12   0:00 /usr/lib/systemd/systemd-journald
root         371  0.0  0.0      0     0 ?        I    09:12   0:00 [kworker/u4:1-ext4-rsv-conversion]
root         395  0.0  0.3  29324  7728 ?        Ss   09:12   0:00 /usr/lib/systemd/systemd-udevd
root         448  0.0  0.3   8276  6084 ?        Ss   09:12   0:00 /usr/sbin/haveged --Foreground --verbose=1
root         475  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/R-rpcio]
root         476  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/R-xprti]
root         496  0.0  0.0      0     0 ?        S    09:12   0:00 [psimon]
root         762  0.0  0.4 310992  9700 ?        Ssl  09:12   0:00 /usr/libexec/accounts-daemon
root         763  0.0  0.1   6652  2560 ?        Ss   09:12   0:00 /usr/sbin/cron -f
message+     764  0.0  0.2  10740  5760 ?        Ss   09:12   0:01 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
polkitd      767  0.0  0.5 384376 10224 ?        Ssl  09:12   0:00 /usr/lib/polkit-1/polkitd --no-debug
root         769  0.0  0.4  18992  8960 ?        Ss   09:12   0:00 /usr/lib/systemd/systemd-logind
root         801  0.0  1.1 335636 23528 ?        Ssl  09:12   0:00 /usr/sbin/NetworkManager --no-daemon
root         810  0.0  0.1 293028  3332 ?        Sl   09:12   0:01 /usr/sbin/VBoxService
root         818  0.0  0.7 392236 14420 ?        Ssl  09:12   0:00 /usr/sbin/ModemManager
root         867  0.0  0.3 380380  7096 ?        SLsl 09:12   0:00 /usr/sbin/lightdm
root         880  0.0  0.1   9480  2944 tty1     Ss+  09:12   0:00 /sbin/agetty -o -p -- \u --noclear - linux
root         881  0.2  8.0 492500 163900 tty7    Ssl+ 09:12   0:32 /usr/lib/xorg/Xorg :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
root         906  0.0  0.0      0     0 ?        S    09:12   0:00 [psimon]
rtkit        936  0.0  0.1  22824  3200 ?        SNsl 09:12   0:00 /usr/libexec/rtkit-daemon
root        1006  0.0  0.4 234384  8120 ?        Sl   09:13   0:00 lightdm --session-child 13 24
kali        1013  0.0  0.5  21248 11776 ?        Ss   09:13   0:00 /usr/lib/systemd/systemd --user
kali        1014  0.0  0.1  21904  3256 ?        S    09:13   0:00 (sd-pam)
kali        1029  0.0  0.7 117360 15116 ?        S<sl 09:13   0:00 /usr/bin/pipewire
kali        1030  0.0  0.2  95252  6016 ?        Ssl  09:13   0:00 /usr/bin/pipewire -c filter-chain.conf
kali        1033  0.0  1.8 642448 37960 ?        S<sl 09:13   0:00 /usr/bin/wireplumber
kali        1034  0.0  0.4 101496  9600 ?        S<sl 09:13   0:00 /usr/bin/pipewire-pulse
kali        1035  0.0  0.6 314332 12240 ?        SLsl 09:13   0:00 /usr/bin/gnome-keyring-daemon --foreground --components=pkcs11,secrets --control-directory=/run/user/1000/keyring
kali        1036  0.0  0.2   9864  5608 ?        Ss   09:13   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
kali        1059  0.0  1.3 339248 26772 ?        Ssl  09:13   0:00 xfce4-session
kali        1113  0.0  0.0  17148  1536 ?        S    09:13   0:00 /usr/bin/VBoxClient --clipboard
kali        1114  0.0  0.2 215336  4096 ?        Sl   09:13   0:00 /usr/bin/VBoxClient --clipboard
kali        1128  0.0  0.0  17148  1536 ?        S    09:13   0:00 /usr/bin/VBoxClient --seamless
kali        1129  0.0  0.1 215444  3200 ?        Sl   09:13   0:06 /usr/bin/VBoxClient --seamless
kali        1136  0.0  0.0  17148  1536 ?        S    09:13   0:00 /usr/bin/VBoxClient --draganddrop
kali        1137  0.1  0.1 215960  3200 ?        Sl   09:13   0:17 /usr/bin/VBoxClient --draganddrop
kali        1149  0.0  0.0   9736  1568 ?        Ss   09:13   0:00 /usr/bin/ssh-agent x-session-manager
kali        1160  0.0  0.4 383180  9952 ?        Ssl  09:13   0:00 /usr/libexec/at-spi-bus-launcher
kali        1167  0.0  0.2   9444  4864 ?        S    09:13   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 11 --address=unix:path=/run/user/1000/at-spi/bus_0
kali        1178  0.0  0.5 236432 10272 ?        Sl   09:13   0:00 /usr/libexec/at-spi2-registryd --use-gnome-session
kali        1191  0.0  0.2  81252  5432 ?        SLs  09:13   0:00 /usr/bin/gpg-agent --supervised
kali        1193  0.1  2.1 388712 44136 ?        Sl   09:13   0:16 xfwm4
kali        1197  0.0  0.4 311936  9720 ?        Ssl  09:13   0:00 /usr/libexec/gvfsd
kali        1203  0.0  0.5 457364 11252 ?        Sl   09:13   0:00 /usr/libexec/gvfsd-fuse /run/user/1000/gvfs -f
kali        1218  0.0  0.0  17148  1792 ?        S    09:13   0:00 /usr/bin/VBoxClient --vmsvga
kali        1219  0.0  0.1 215552  3840 ?        Sl   09:13   0:01 /usr/bin/VBoxClient --vmsvga
kali        1223  0.0  1.4 303808 30148 ?        Sl   09:13   0:01 xfsettingsd
root        1227  0.0  0.5 315732 11200 ?        Ssl  09:13   0:00 /usr/libexec/upowerd
kali        1233  0.0  2.2 460832 45976 ?        Sl   09:13   0:01 xfce4-panel
kali        1238  0.0  1.4 413104 29944 ?        Sl   09:13   0:00 Thunar --daemon
kali        1249  0.0  4.9 562064 99328 ?        Sl   09:13   0:03 xfdesktop
kali        1253  0.0  2.4 534612 48756 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libwhiskermenu.so 1 27262983 whiskermenu Whisker Menu Show a menu to easily access installed applications
kali        1257  0.0  2.7 515204 55320 ?        Sl   09:13   0:00 /usr/bin/python3 /usr/bin/blueman-applet
kali        1259  0.0  0.9 259400 19856 ?        Sl   09:13   0:00 xfce4-power-manager
kali        1261  0.0  0.9 258432 18596 ?        Sl   09:13   0:00 /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1
kali        1263  0.0  1.5 413700 30400 ?        Sl   09:13   0:00 light-locker
kali        1269  0.0  0.1  12632  2220 ?        Ssl  09:13   0:00 xcape -e Super_L Control_L Escape
kali        1271  0.0  0.4 307944  8704 ?        Sl   09:13   0:00 xiccd
kali        1279  0.0  2.3 619840 47496 ?        Sl   09:13   0:00 nm-applet
kali        1288  0.0  0.2 230356  5632 ?        Ssl  09:13   0:00 /usr/libexec/dconf-service
kali        1290  0.0  1.8  62380 36736 ?        S    09:13   0:00 /usr/bin/python3 /usr/share/system-config-printer/applet.py
colord      1295  0.0  0.8 317868 16396 ?        Ssl  09:13   0:00 /usr/libexec/colord
kali        1309  0.0  1.0 408860 22104 ?        Ssl  09:13   0:01 /usr/lib/x86_64-linux-gnu/xfce4/notifyd/xfce4-notifyd
kali        1319  0.0  0.4 307952  8188 ?        Sl   09:13   0:00 /usr/libexec/geoclue-2.0/demos/agent
kali        1388  0.1  2.6 363316 53884 ?        Sl   09:13   0:22 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libcpugraph.so 13 27262988 cpugraph CPU Graph Graphical representation of the CPU load
kali        1389  0.0  1.4 411988 29404 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libsystray.so 14 27262989 systray Status Tray Plugin Provides status notifier items (application indicators) and legacy systray items
kali        1390  0.1  1.5 340272 32020 ?        Sl   09:13   0:23 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libgenmon.so 15 27262990 genmon Generic Monitor Show output of a command.
kali        1391  0.0  2.0 455764 41100 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libpulseaudio-plugin.so 16 27262991 pulseaudio PulseAudio Plugin Adjust the audio volume of the PulseAudio sound system
kali        1392  0.0  2.2 458784 44708 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libnotification-plugin.so 17 27262992 notification-plugin Notification Plugin Notification plugin for the Xfce panel
kali        1393  0.0  2.2 385824 45992 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libxfce4powermanager.so 18 27262993 power-manager-plugin Power Manager Plugin Display the battery levels of your devices and control the brightness of your display
kali        1402  0.0  2.0 385460 41252 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libactions.so 22 27262994 actions Action Buttons Log out, lock or other system actions
kali        1450  0.0  0.3  49204  7936 ?        Ss   09:13   0:00 /usr/libexec/bluetooth/obexd
kali        1463  0.0  0.8 425988 17044 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-udisks2-volume-monitor
root        1467  0.0  0.8 470200 17776 ?        Ssl  09:13   0:00 /usr/libexec/udisks2/udisksd
kali        1476  0.0  0.5 388476 10208 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-afc-volume-monitor
kali        1482  0.0  0.5 307440 10748 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-mtp-volume-monitor
kali        1487  0.0  0.4 307416  8460 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-goa-volume-monitor
kali        1492  0.0  0.5 308400 10816 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-gphoto2-volume-monitor
kali        1502  0.0  0.5 533248 10920 ?        Sl   09:13   0:00 /usr/libexec/gvfsd-trash --spawner :1.21 /org/gtk/gvfs/exec_spaw/0
kali        1510  0.0  0.4 233948  8596 ?        Ssl  09:13   0:00 /usr/libexec/gvfsd-metadata
root       28408  0.0  0.0      0     0 ?        I    10:09   0:03 [kworker/1:1-mm_percpu_wq]
root       68526  0.0  0.0      0     0 ?        I    11:33   0:00 [kworker/u5:0-events_unbound]
kali       82069  0.1  4.8 453944 98660 ?        Sl   12:01   0:05 /usr/bin/qterminal
kali       82072  0.0  0.3  10344  6456 pts/0    Ss   12:01   0:00 /usr/bin/zsh
root       82162  0.0  0.3  17760  6780 pts/0    S+   12:01   0:00 sudo su
root       82187  0.0  0.1  17760  2336 pts/1    Ss   12:01   0:00 sudo su
root       82188  0.0  0.2   9196  4096 pts/1    S    12:01   0:00 su
root       82189  0.2  0.3  13960  7624 pts/1    S    12:01   0:10 zsh
root       86062  0.0  0.0      0     0 ?        I    12:09   0:00 [kworker/1:0-cgroup_destroy]
root       86751  0.0  0.0      0     0 ?        I    12:10   0:00 [kworker/u5:2-events_unbound]
root       88311  0.0  0.1   5896  2560 pts/1    T    12:14   0:00 less nomina
root      100868  0.0  0.1   5896  2560 pts/1    T    12:39   0:00 less nomina16
root      101019  0.0  0.0      0     0 ?        I    12:39   0:00 [kworker/u6:3-events_unbound]
root      101084  0.0  0.0      0     0 ?        I    12:39   0:00 [kworker/0:0-ata_sff]
root      107841  0.0  0.0      0     0 ?        I    12:53   0:00 [kworker/u5:3-flush-8:0]
root      108050  0.0  0.0      0     0 ?        I    12:53   0:00 [kworker/u6:0]
root      114065  0.0  0.0      0     0 ?        I    13:05   0:00 [kworker/0:1-ata_sff]
kali      114287  0.0  1.5 646448 30580 ?        SNsl 13:05   0:00 /usr/lib/x86_64-linux-gnu/tumbler-1/tumblerd
root      115621  0.0  0.2  12140  4992 pts/1    R+   13:08   0:00 ps -aux
root      115622  0.0  0.1   5716  2048 pts/1    S+   13:08   0:00 more
root      115623  0.0  0.1   8996  3840 pts/1    S+   13:08   0:00 awk $2>50 {print $0}

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux | more | awk '$2>50 {print $0}'
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          57  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-kthro]
root          59  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-acpi_]
root          60  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-mld]
root          61  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-ipv6_]
root          66  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-kstrp]
root          68  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u7:0]
root          69  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u8:0]
root          70  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u9:0]
root          80  0.0  0.0      0     0 ?        I    09:11   0:00 [kworker/u6:2-writeback]
root         168  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/1:1H-kblockd]
root         171  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-crypt]
root         177  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-ata_s]
root         182  0.0  0.0      0     0 ?        S    09:11   0:00 [irq/18-vmwgfx]
root         183  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-ttm]
root         188  0.0  0.0      0     0 ?        S    09:11   0:00 [scsi_eh_0]
root         195  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-scsi_]
root         196  0.0  0.0      0     0 ?        S    09:11   0:00 [scsi_eh_1]
root         197  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-scsi_]
root         203  0.0  0.0      0     0 ?        S    09:11   0:00 [scsi_eh_2]
root         204  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R-scsi_]
root         242  0.0  0.0      0     0 ?        I    09:11   0:02 [kworker/0:4-events_freezable_power_]
root         245  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/0:2H-kblockd]
root         278  0.0  0.0      0     0 ?        S    09:12   0:00 [jbd2/sda1-8]
root         279  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/R-ext4-]
root         336  0.0  0.8  51420 16984 ?        Ss   09:12   0:00 /usr/lib/systemd/systemd-journald
root         371  0.0  0.0      0     0 ?        I    09:12   0:00 [kworker/u4:1-ext4-rsv-conversion]
root         395  0.0  0.3  29324  7728 ?        Ss   09:12   0:00 /usr/lib/systemd/systemd-udevd
root         448  0.0  0.3   8276  6084 ?        Ss   09:12   0:00 /usr/sbin/haveged --Foreground --verbose=1
root         475  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/R-rpcio]
root         476  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/R-xprti]
root         496  0.0  0.0      0     0 ?        S    09:12   0:00 [psimon]
root         762  0.0  0.4 310992  9700 ?        Ssl  09:12   0:00 /usr/libexec/accounts-daemon
root         763  0.0  0.1   6652  2560 ?        Ss   09:12   0:00 /usr/sbin/cron -f
message+     764  0.0  0.2  10740  5760 ?        Ss   09:12   0:01 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
polkitd      767  0.0  0.5 384376 10224 ?        Ssl  09:12   0:00 /usr/lib/polkit-1/polkitd --no-debug
root         769  0.0  0.4  18992  8960 ?        Ss   09:12   0:00 /usr/lib/systemd/systemd-logind
root         801  0.0  1.1 335636 23528 ?        Ssl  09:12   0:00 /usr/sbin/NetworkManager --no-daemon
root         810  0.0  0.1 293028  3332 ?        Sl   09:12   0:01 /usr/sbin/VBoxService
root         818  0.0  0.7 392236 14420 ?        Ssl  09:12   0:00 /usr/sbin/ModemManager
root         867  0.0  0.3 380380  7096 ?        SLsl 09:12   0:00 /usr/sbin/lightdm
root         880  0.0  0.1   9480  2944 tty1     Ss+  09:12   0:00 /sbin/agetty -o -p -- \u --noclear - linux
root         881  0.2  8.0 492500 163900 tty7    Ssl+ 09:12   0:32 /usr/lib/xorg/Xorg :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
root         906  0.0  0.0      0     0 ?        S    09:12   0:00 [psimon]
rtkit        936  0.0  0.1  22824  3200 ?        SNsl 09:12   0:00 /usr/libexec/rtkit-daemon
root        1006  0.0  0.4 234384  8120 ?        Sl   09:13   0:00 lightdm --session-child 13 24
kali        1013  0.0  0.5  21248 11776 ?        Ss   09:13   0:00 /usr/lib/systemd/systemd --user
kali        1014  0.0  0.1  21904  3256 ?        S    09:13   0:00 (sd-pam)
kali        1029  0.0  0.7 117360 15116 ?        S<sl 09:13   0:00 /usr/bin/pipewire
kali        1030  0.0  0.2  95252  6016 ?        Ssl  09:13   0:00 /usr/bin/pipewire -c filter-chain.conf
kali        1033  0.0  1.8 642448 37960 ?        S<sl 09:13   0:00 /usr/bin/wireplumber
kali        1034  0.0  0.4 101496  9600 ?        S<sl 09:13   0:00 /usr/bin/pipewire-pulse
kali        1035  0.0  0.6 314332 12240 ?        SLsl 09:13   0:00 /usr/bin/gnome-keyring-daemon --foreground --components=pkcs11,secrets --control-directory=/run/user/1000/keyring
kali        1036  0.0  0.2   9864  5608 ?        Ss   09:13   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
kali        1059  0.0  1.3 339248 26772 ?        Ssl  09:13   0:00 xfce4-session
kali        1113  0.0  0.0  17148  1536 ?        S    09:13   0:00 /usr/bin/VBoxClient --clipboard
kali        1114  0.0  0.2 215336  4096 ?        Sl   09:13   0:00 /usr/bin/VBoxClient --clipboard
kali        1128  0.0  0.0  17148  1536 ?        S    09:13   0:00 /usr/bin/VBoxClient --seamless
kali        1129  0.0  0.1 215444  3200 ?        Sl   09:13   0:06 /usr/bin/VBoxClient --seamless
kali        1136  0.0  0.0  17148  1536 ?        S    09:13   0:00 /usr/bin/VBoxClient --draganddrop
kali        1137  0.1  0.1 215960  3200 ?        Sl   09:13   0:17 /usr/bin/VBoxClient --draganddrop
kali        1149  0.0  0.0   9736  1568 ?        Ss   09:13   0:00 /usr/bin/ssh-agent x-session-manager
kali        1160  0.0  0.4 383180  9952 ?        Ssl  09:13   0:00 /usr/libexec/at-spi-bus-launcher
kali        1167  0.0  0.2   9444  4864 ?        S    09:13   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 11 --address=unix:path=/run/user/1000/at-spi/bus_0
kali        1178  0.0  0.5 236432 10272 ?        Sl   09:13   0:00 /usr/libexec/at-spi2-registryd --use-gnome-session
kali        1191  0.0  0.2  81252  5432 ?        SLs  09:13   0:00 /usr/bin/gpg-agent --supervised
kali        1193  0.1  2.1 388712 44136 ?        Sl   09:13   0:16 xfwm4
kali        1197  0.0  0.4 311936  9720 ?        Ssl  09:13   0:00 /usr/libexec/gvfsd
kali        1203  0.0  0.5 457364 11252 ?        Sl   09:13   0:00 /usr/libexec/gvfsd-fuse /run/user/1000/gvfs -f
kali        1218  0.0  0.0  17148  1792 ?        S    09:13   0:00 /usr/bin/VBoxClient --vmsvga
kali        1219  0.0  0.1 215552  3840 ?        Sl   09:13   0:01 /usr/bin/VBoxClient --vmsvga
kali        1223  0.0  1.4 303808 30148 ?        Sl   09:13   0:01 xfsettingsd
root        1227  0.0  0.5 315732 11200 ?        Ssl  09:13   0:00 /usr/libexec/upowerd
kali        1233  0.0  2.2 460832 45976 ?        Sl   09:13   0:01 xfce4-panel
kali        1238  0.0  1.4 413104 29944 ?        Sl   09:13   0:00 Thunar --daemon
kali        1249  0.0  4.9 562064 99328 ?        Sl   09:13   0:03 xfdesktop
kali        1253  0.0  2.4 534612 48756 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libwhiskermenu.so 1 27262983 whiskermenu Whisker Menu Show a menu to easily access installed applications
kali        1257  0.0  2.7 515204 55320 ?        Sl   09:13   0:00 /usr/bin/python3 /usr/bin/blueman-applet
kali        1259  0.0  0.9 259400 19856 ?        Sl   09:13   0:00 xfce4-power-manager
kali        1261  0.0  0.9 258432 18596 ?        Sl   09:13   0:00 /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1
kali        1263  0.0  1.5 413700 30400 ?        Sl   09:13   0:00 light-locker
kali        1269  0.0  0.1  12632  2220 ?        Ssl  09:13   0:00 xcape -e Super_L Control_L Escape
kali        1271  0.0  0.4 307944  8704 ?        Sl   09:13   0:00 xiccd
kali        1279  0.0  2.3 619840 47496 ?        Sl   09:13   0:00 nm-applet
kali        1288  0.0  0.2 230356  5632 ?        Ssl  09:13   0:00 /usr/libexec/dconf-service
kali        1290  0.0  1.8  62380 36736 ?        S    09:13   0:00 /usr/bin/python3 /usr/share/system-config-printer/applet.py
colord      1295  0.0  0.8 317868 16396 ?        Ssl  09:13   0:00 /usr/libexec/colord
kali        1309  0.0  1.0 408860 22104 ?        Ssl  09:13   0:01 /usr/lib/x86_64-linux-gnu/xfce4/notifyd/xfce4-notifyd
kali        1319  0.0  0.4 307952  8188 ?        Sl   09:13   0:00 /usr/libexec/geoclue-2.0/demos/agent
kali        1388  0.1  2.6 363316 53884 ?        Sl   09:13   0:22 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libcpugraph.so 13 27262988 cpugraph CPU Graph Graphical representation of the CPU load
kali        1389  0.0  1.4 411988 29404 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libsystray.so 14 27262989 systray Status Tray Plugin Provides status notifier items (application indicators) and legacy systray items
kali        1390  0.1  1.5 340272 32020 ?        Sl   09:13   0:23 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libgenmon.so 15 27262990 genmon Generic Monitor Show output of a command.
kali        1391  0.0  2.0 455764 41100 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libpulseaudio-plugin.so 16 27262991 pulseaudio PulseAudio Plugin Adjust the audio volume of the PulseAudio sound system
kali        1392  0.0  2.2 458784 44708 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libnotification-plugin.so 17 27262992 notification-plugin Notification Plugin Notification plugin for the Xfce panel
kali        1393  0.0  2.2 385824 45992 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libxfce4powermanager.so 18 27262993 power-manager-plugin Power Manager Plugin Display the battery levels of your devices and control the brightness of your display
kali        1402  0.0  2.0 385460 41252 ?        Sl   09:13   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libactions.so 22 27262994 actions Action Buttons Log out, lock or other system actions
kali        1450  0.0  0.3  49204  7936 ?        Ss   09:13   0:00 /usr/libexec/bluetooth/obexd
kali        1463  0.0  0.8 425988 17044 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-udisks2-volume-monitor
root        1467  0.0  0.8 470200 17776 ?        Ssl  09:13   0:00 /usr/libexec/udisks2/udisksd
kali        1476  0.0  0.5 388476 10208 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-afc-volume-monitor
kali        1482  0.0  0.5 307440 10748 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-mtp-volume-monitor
kali        1487  0.0  0.4 307416  8460 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-goa-volume-monitor
kali        1492  0.0  0.5 308400 10816 ?        Ssl  09:13   0:00 /usr/libexec/gvfs-gphoto2-volume-monitor
kali        1502  0.0  0.5 533248 10920 ?        Sl   09:13   0:00 /usr/libexec/gvfsd-trash --spawner :1.21 /org/gtk/gvfs/exec_spaw/0
kali        1510  0.0  0.4 233948  8596 ?        Ssl  09:13   0:00 /usr/libexec/gvfsd-metadata
root       28408  0.0  0.0      0     0 ?        I    10:09   0:03 [kworker/1:1-events]
root       68526  0.0  0.0      0     0 ?        I    11:33   0:00 [kworker/u5:0-events_unbound]
kali       82069  0.1  4.8 453944 98660 ?        Sl   12:01   0:05 /usr/bin/qterminal
kali       82072  0.0  0.3  10344  6456 pts/0    Ss   12:01   0:00 /usr/bin/zsh
root       82162  0.0  0.3  17760  6780 pts/0    S+   12:01   0:00 sudo su
root       82187  0.0  0.1  17760  2336 pts/1    Ss   12:01   0:00 sudo su
root       82188  0.0  0.2   9196  4096 pts/1    S    12:01   0:00 su
root       82189  0.2  0.3  13960  7624 pts/1    S    12:01   0:10 zsh
root       86062  0.0  0.0      0     0 ?        I    12:09   0:00 [kworker/1:0-cgroup_destroy]
root       86751  0.0  0.0      0     0 ?        I    12:10   0:00 [kworker/u5:2-events_unbound]
root       88311  0.0  0.1   5896  2560 pts/1    T    12:14   0:00 less nomina
root      100868  0.0  0.1   5896  2560 pts/1    T    12:39   0:00 less nomina16
root      101019  0.0  0.0      0     0 ?        I    12:39   0:00 [kworker/u6:3-events_unbound]
root      101084  0.0  0.0      0     0 ?        I    12:39   0:00 [kworker/0:0-ata_sff]
root      107841  0.0  0.0      0     0 ?        I    12:53   0:00 [kworker/u5:3-flush-8:0]
root      108050  0.0  0.0      0     0 ?        I    12:53   0:00 [kworker/u6:0]
root      114065  0.0  0.0      0     0 ?        I    13:05   0:00 [kworker/0:1-ata_sff]
kali      114287  0.0  1.5 646448 30580 ?        SNsl 13:05   0:00 /usr/lib/x86_64-linux-gnu/tumbler-1/tumblerd
root      115689  0.0  0.2  12140  4992 pts/1    R+   13:08   0:00 ps -aux
root      115690  0.0  0.1   5716  2048 pts/1    S+   13:08   0:00 more
root      115691  0.0  0.1   8996  3840 pts/1    S+   13:08   0:00 awk $2>50 {print $0}

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux | more | awk '$2>50 {print $0}' | more
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          57  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-kthro]
root          59  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-acpi_]
root          60  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-mld]
root          61  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-ipv6_]
root          66  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-kstrp]
root          68  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u
7:0]
root          69  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u
8:0]
root          70  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u
9:0]
root          80  0.0  0.0      0     0 ?        I    09:11   0:00 [kworker/u
6:2-writeback]
root         168  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/1
:1H-kblockd]
root         171  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-crypt]
root         177  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-ata_s]
root         182  0.0  0.0      0     0 ?        S    09:11   0:00 [irq/18-vm

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux | more | awk '$2>50 {print $7}' | more
TTY
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux | more | awk '$2>50 $7~ /?/ {print $7}' | more

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux | more | awk '$2>50 $7~ /?/ {print $0}' | more

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux | more | awk '$2>50 && $7~ /?/ {print $0}' | more
root          57  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-kthro]
root          59  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-acpi_]
root          60  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-mld]
root          61  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-ipv6_]
root          66  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-kstrp]
root          68  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u
7:0]
root          69  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u
8:0]
root          70  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u
9:0]
root          80  0.0  0.0      0     0 ?        I    09:11   0:00 [kworker/u
6:2-flush-8:0]
root         168  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/1
:1H-kblockd]
root         171  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-crypt]
root         177  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/R
-ata_s]
root         182  0.0  0.0      0     0 ?        S    09:11   0:00 [irq/18-vm
wgfx]

┌──(root㉿kali)-[/home/kali/Desktop]
└─# ps -aux | more | awk '$2>50 && $7~ /?/ {print $7}' | more
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
?
```

## Clase 02/11/2024
### Admin:
```bash
┌──(kali㉿kali)-[~]
└─$ sudo su
[sudo] password for kali: 
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/passwd
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:992:992:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
tss:x:101:104:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:105::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:105:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:x:106:108:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:107:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
pulse:x:108:110:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
lightdm:x:109:112:Light Display Manager:/var/lib/lightdm:/bin/false
saned:x:110:114::/var/lib/saned:/usr/sbin/nologin
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:116:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:117:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:118:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:x:115:65534::/nonexistent:/usr/sbin/nologin
mysql:x:116:120:MariaDB Server,,,:/nonexistent:/bin/false
stunnel4:x:990:990:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:122::/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:x:119:123::/var/lib/snmp:/bin/false
sslh:x:120:124::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:127::/nonexistent:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
_gophish:x:124:130::/var/lib/gophish:/usr/sbin/nologin
iodine:x:125:65534::/run/iodine:/usr/sbin/nologin
miredo:x:126:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:127:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin
postgres:x:129:132:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
mosquitto:x:130:133::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:131:134::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:132:135::/var/lib/openvas:/usr/sbin/nologin
kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# groupadd linuxpero56
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/passwd     
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:992:992:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
tss:x:101:104:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:105::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:105:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:x:106:108:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:107:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
pulse:x:108:110:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
lightdm:x:109:112:Light Display Manager:/var/lib/lightdm:/bin/false
saned:x:110:114::/var/lib/saned:/usr/sbin/nologin
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:116:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:117:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:118:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:x:115:65534::/nonexistent:/usr/sbin/nologin
mysql:x:116:120:MariaDB Server,,,:/nonexistent:/bin/false
stunnel4:x:990:990:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:122::/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:x:119:123::/var/lib/snmp:/bin/false
sslh:x:120:124::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:127::/nonexistent:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
_gophish:x:124:130::/var/lib/gophish:/usr/sbin/nologin
iodine:x:125:65534::/run/iodine:/usr/sbin/nologin
miredo:x:126:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:127:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin
postgres:x:129:132:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
mosquitto:x:130:133::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:131:134::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:132:135::/var/lib/openvas:/usr/sbin/nologin
kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/group      
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:kali
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:kali
fax:x:21:
voice:x:22:
cdrom:x:24:kali
floppy:x:25:kali
tape:x:26:
sudo:x:27:kali
audio:x:29:pulse,kali
dip:x:30:kali
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
shadow:x:42:
utmp:x:43:
video:x:44:kali
sasl:x:45:
plugdev:x:46:kali
staff:x:50:
games:x:60:
users:x:100:kali
nogroup:x:65534:
systemd-journal:x:999:
systemd-network:x:998:
crontab:x:997:
input:x:996:
sgx:x:995:
kvm:x:994:
render:x:993:
netdev:x:101:kali
systemd-timesync:x:992:
messagebus:x:102:
_ssh:x:103:
tss:x:104:
tcpdump:x:105:
bluetooth:x:106:kali
plocate:x:107:
avahi:x:108:
pipewire:x:109:
pulse:x:110:
pulse-access:x:111:
lightdm:x:112:
scanner:x:113:saned,kali
saned:x:114:
polkitd:x:991:
rtkit:x:115:
colord:x:116:
nm-openvpn:x:117:
nm-openconnect:x:118:
kali-trusted:x:119:
mysql:x:120:
rdma:x:121:
stunnel4:x:990:stunnel4
geoclue:x:122:
Debian-snmp:x:123:
sslh:x:124:
ssl-cert:x:125:postgres
i2c:x:126:
ntpsec:x:127:
redsocks:x:128:
kismet:x:129:
_gophish:x:130:
sambashare:x:989:
redis:x:131:_gvm
postgres:x:132:
mosquitto:x:133:
inetsim:x:134:
_gvm:x:135:
wireshark:x:136:kali
kali:x:1000:
kaboxer:x:137:kali
vboxsf:x:138:kali
linuxpero56:x:1001:
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# useradd -g linuxpero56 /home/practicas44 -m -s /bin/bash Sebastian
Usage: useradd [options] LOGIN
       useradd -D
       useradd -D [options]

Options:
      --badname                 do not check for bad names
  -b, --base-dir BASE_DIR       base directory for the home directory of the
                                new account
      --btrfs-subvolume-home    use BTRFS subvolume for home directory
  -c, --comment COMMENT         GECOS field of the new account
  -d, --home-dir HOME_DIR       home directory of the new account
  -D, --defaults                print or change default useradd configuration
  -e, --expiredate EXPIRE_DATE  expiration date of the new account
  -f, --inactive INACTIVE       password inactivity period of the new account
  -F, --add-subids-for-system   add entries to sub[ud]id even when adding a system user
  -g, --gid GROUP               name or ID of the primary group of the new
                                account
  -G, --groups GROUPS           list of supplementary groups of the new
                                account
  -h, --help                    display this help message and exit
  -k, --skel SKEL_DIR           use this alternative skeleton directory
  -K, --key KEY=VALUE           override /etc/login.defs defaults
  -m, --create-home             create the user's home directory
  -M, --no-create-home          do not create the user's home directory
  -N, --no-user-group           do not create a group with the same name as
                                the user
  -o, --non-unique              allow to create users with duplicate
                                (non-unique) UID
  -p, --password PASSWORD       encrypted password of the new account
  -r, --system                  create a system account
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  -s, --shell SHELL             login shell of the new account
  -u, --uid UID                 user ID of the new account
  -U, --user-group              create a group with the same name as the user
  -Z, --selinux-user SEUSER     use a specific SEUSER for the SELinux user mapping
      --selinux-range SERANGE   use a specific MLS range for the SELinux user mapping

                                                                             
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/passwd                                                   
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:992:992:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
tss:x:101:104:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:105::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:105:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:x:106:108:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:107:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
pulse:x:108:110:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
lightdm:x:109:112:Light Display Manager:/var/lib/lightdm:/bin/false
saned:x:110:114::/var/lib/saned:/usr/sbin/nologin
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:116:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:117:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:118:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:x:115:65534::/nonexistent:/usr/sbin/nologin
mysql:x:116:120:MariaDB Server,,,:/nonexistent:/bin/false
stunnel4:x:990:990:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:122::/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:x:119:123::/var/lib/snmp:/bin/false
sslh:x:120:124::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:127::/nonexistent:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
_gophish:x:124:130::/var/lib/gophish:/usr/sbin/nologin
iodine:x:125:65534::/run/iodine:/usr/sbin/nologin
miredo:x:126:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:127:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin
postgres:x:129:132:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
mosquitto:x:130:133::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:131:134::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:132:135::/var/lib/openvas:/usr/sbin/nologin
kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# useradd -g linuxpero56 -d  /home/practicas44 -m -s /bin/bash Sebastian
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/passwd                                                       
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:992:992:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
tss:x:101:104:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:105::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:105:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:x:106:108:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:107:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
pulse:x:108:110:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
lightdm:x:109:112:Light Display Manager:/var/lib/lightdm:/bin/false
saned:x:110:114::/var/lib/saned:/usr/sbin/nologin
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:116:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:117:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:118:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:x:115:65534::/nonexistent:/usr/sbin/nologin
mysql:x:116:120:MariaDB Server,,,:/nonexistent:/bin/false
stunnel4:x:990:990:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:122::/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:x:119:123::/var/lib/snmp:/bin/false
sslh:x:120:124::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:127::/nonexistent:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
_gophish:x:124:130::/var/lib/gophish:/usr/sbin/nologin
iodine:x:125:65534::/run/iodine:/usr/sbin/nologin
miredo:x:126:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:127:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin
postgres:x:129:132:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
mosquitto:x:130:133::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:131:134::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:132:135::/var/lib/openvas:/usr/sbin/nologin
kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh
Sebastian:x:1001:1001::/home/practicas44:/bin/bash
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# passwd Sebastian
New password: 
Retype new password: 
passwd: password updated successfully
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# 

```

### Sebastian
```bash
                                                                             ┌──(kali㉿kali)-[~]
└─$ su - Sebastian
Password: 
┌──(Sebastian㉿kali)-[~]
└─$ pico Nomina

┌──(Sebastian㉿kali)-[~]
└─$ cat Nomina
Rufina!Toro!Moreno!860000!Secretaria!Ninguno!860000!Soltera
Cinforosa!García!Moreno!1700000!Programador!Tecnóloga!1700000!Casada
Matea!Patiño!Moreno!3000000!Analista!Ingeniera!3000000!Soltera
Anacarota!Pérez!Rico!1700000!Programador!Tecnóloga!1700000!Soltera
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada
Rufina!Toro!Gómez!3000000!Analista!Ingeniera!3000000!Casada
Matea!Pérez!Vélez!3000000!Analista!Ingeniera!3000000!Soltera
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk ' {print $1}' Nomina
Rufina!Toro!Moreno!860000!Secretaria!Ninguno!860000!Soltera
Cinforosa!García!Moreno!1700000!Programador!Tecnóloga!1700000!Casada
Matea!Patiño!Moreno!3000000!Analista!Ingeniera!3000000!Soltera
Anacarota!Pérez!Rico!1700000!Programador!Tecnóloga!1700000!Soltera
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada
Rufina!Toro!Gómez!3000000!Analista!Ingeniera!3000000!Casada
Matea!Pérez!Vélez!3000000!Analista!Ingeniera!3000000!Soltera
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk -F '!' '{print $1}' Nomina                                           
Rufina
Cinforosa
Matea
Anacarota
Bertulia
Rufina
Matea
Cipriana

┌──(Sebastian㉿kali)-[~]
└─$ awk -F '!' '{print $0}' Nomina                                           
Rufina!Toro!Moreno!860000!Secretaria!Ninguno!860000!Soltera
Cinforosa!García!Moreno!1700000!Programador!Tecnóloga!1700000!Casada
Matea!Patiño!Moreno!3000000!Analista!Ingeniera!3000000!Soltera
Anacarota!Pérez!Rico!1700000!Programador!Tecnóloga!1700000!Soltera
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada
Rufina!Toro!Gómez!3000000!Analista!Ingeniera!3000000!Casada
Matea!Pérez!Vélez!3000000!Analista!Ingeniera!3000000!Soltera
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$1!~ /Matea/ && $2~ /^P/ {print $0}' Nomina                
Anacarota!Pérez!Rico!1700000!Programador!Tecnóloga!1700000!Soltera
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$1!~ /Matea/ && $2~ /^P/ {print $0}' Nomina                
Anacarota!Pérez!Rico!1700000!Programador!Tecnóloga!1700000!Soltera
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$2~ /Toro/ && $6~ /a$/ {print $0}' NOMINA
awk: fatal: cannot open file `NOMINA' for reading: No such file or directory

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$2~ /Toro/ && $6~ /a$/ {print $0}' Nomina
Rufina!Toro!Gómez!3000000!Analista!Ingeniera!3000000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$2~ /Toro/ && $6~ /a$/ {print $0}' Nomina>Nomina22         

┌──(Sebastian㉿kali)-[~]
└─$ cat Nomina22
Rufina!Toro!Gómez!3000000!Analista!Ingeniera!3000000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$2~ /Restrepo/ || $4<900000 {print $0}' Nomina
Rufina!Toro!Moreno!860000!Secretaria!Ninguno!860000!Soltera
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$2~ /Restrepo/ || $4<900000 {print $0}' Nomina>Nomina30

┌──(Sebastian㉿kali)-[~]
└─$ cat Nomina30                                                             
Rufina!Toro!Moreno!860000!Secretaria!Ninguno!860000!Soltera
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$8!~ /Soltera/ && $4>688000 {print $0}' Nomina             
Cinforosa!García!Moreno!1700000!Programador!Tecnóloga!1700000!Casada
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada
Rufina!Toro!Gómez!3000000!Analista!Ingeniera!3000000!Casada
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$8!~ /Soltera/ && $4>688000 && $1!~ /^R/ {print $0}' NominaCinforosa!García!Moreno!1700000!Programador!Tecnóloga!1700000!Casada
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$8!~ /Soltera/ && $4>688000 && $1!~ /^R/ {print $0}' Nomina>Nomina31

┌──(Sebastian㉿kali)-[~]
└─$ cat Nomina31                                                             
Cinforosa!García!Moreno!1700000!Programador!Tecnóloga!1700000!Casada
Bertulia!Pérez!Moreno!860000!Secretaria!Ninguno!860000!Casada
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada


┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$1~ /a$/ && $2!~ /^T/  && $3~ /z$/ {print $0}' Nomina
Matea!Pérez!Vélez!3000000!Analista!Ingeniera!3000000!Soltera

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$1~ /a$/ && $2!~ /^T/  && $3~ /z$/ {print $0}' Nomina>Nomina32

┌──(Sebastian㉿kali)-[~]
└─$ cat Nomina32
Matea!Pérez!Vélez!3000000!Analista!Ingeniera!3000000!Soltera

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$2!~ /o$/ && $3~ /^P/  && $5!~ /Analista/ {print $0}' Nomina

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$2!~ /o$/ && $3~ /^P/  && $5!~ /Analista/ {print $0}' Nomina>Nomina33

┌──(Sebastian㉿kali)-[~]
└─$ cat Nomina33

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$2~ /^T/ || $3~ /r$/ {print $2,$3,$1,$4}' Nomina
Toro Moreno Rufina 860000
Toro Gómez Rufina 3000000

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$1!~ /Cinforosa/ && $4>=950000 && $4<=2600000  {print $0}' Nomina
Anacarota!Pérez!Rico!1700000!Programador!Tecnóloga!1700000!Soltera
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk  -F '!'  '$1!~ /Cinforosa/ && $4>=950000 && $4<=2600000  {print $0}' Nomina>Nomina34

┌──(Sebastian㉿kali)-[~]
└─$ cat Nomina34                                                                          
Anacarota!Pérez!Rico!1700000!Programador!Tecnóloga!1700000!Soltera
Cipriana!Restrepo!Ranso!1700000!Programador!Tecnóloga!1700000!Casada

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '{print $0}' /etc/passwd                                                   
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:992:992:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
tss:x:101:104:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:105::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:105:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:x:106:108:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:107:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
pulse:x:108:110:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
lightdm:x:109:112:Light Display Manager:/var/lib/lightdm:/bin/false
saned:x:110:114::/var/lib/saned:/usr/sbin/nologin
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:116:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:117:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:118:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:x:115:65534::/nonexistent:/usr/sbin/nologin
mysql:x:116:120:MariaDB Server,,,:/nonexistent:/bin/false
stunnel4:x:990:990:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:122::/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:x:119:123::/var/lib/snmp:/bin/false
sslh:x:120:124::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:127::/nonexistent:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
_gophish:x:124:130::/var/lib/gophish:/usr/sbin/nologin
iodine:x:125:65534::/run/iodine:/usr/sbin/nologin
miredo:x:126:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:127:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin
postgres:x:129:132:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
mosquitto:x:130:133::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:131:134::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:132:135::/var/lib/openvas:/usr/sbin/nologin
kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh
Sebastian:x:1001:1001::/home/practicas44:/bin/bash

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '{print $1}' /etc/passwd                                                   
root
daemon
bin
sys
sync
games
man
lp
mail
news
uucp
proxy
www-data
backup
list
irc
_apt
nobody
systemd-network
systemd-timesync
messagebus
tss
strongswan
tcpdump
sshd
usbmux
dnsmasq
avahi
speech-dispatcher
pulse
lightdm
saned
polkitd
rtkit
colord
nm-openvpn
nm-openconnect
_galera
mysql
stunnel4
_rpc
geoclue
Debian-snmp
sslh
ntpsec
redsocks
rwhod
_gophish
iodine
miredo
statd
redis
postgres
mosquitto
inetsim
_gvm
kali
Sebastian

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '{print $3}' /etc/passwd                                                   
0
1
2
3
4
5
6
7
8
9
10
13
33
34
38
39
42
65534
998
992
100
101
102
103
104
105
999
106
107
108
109
110
991
111
112
113
114
115
116
990
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
1000
1001

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '$1~ /^C/ {print $3}' /etc/passwd                                          

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '$1~ /^C/ {print $1}' /etc/passwd                                          

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '$1~ /^C/ && $1~ /a$/ && $3>250 {print $0}' /etc/passwd 

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '$1!~ /^S/ && $1!~ /a$/ && $3<600 {print $0}' /etc/passwd                  
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
tss:x:101:104:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:105::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:105:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
avahi:x:106:108:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:107:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
pulse:x:108:110:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
lightdm:x:109:112:Light Display Manager:/var/lib/lightdm:/bin/false
saned:x:110:114::/var/lib/saned:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:116:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:117:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:118:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
mysql:x:116:120:MariaDB Server,,,:/nonexistent:/bin/false
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:122::/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:x:119:123::/var/lib/snmp:/bin/false
sslh:x:120:124::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:127::/nonexistent:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
_gophish:x:124:130::/var/lib/gophish:/usr/sbin/nologin
iodine:x:125:65534::/run/iodine:/usr/sbin/nologin
miredo:x:126:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:127:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin
postgres:x:129:132:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
mosquitto:x:130:133::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:131:134::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:132:135::/var/lib/openvas:/usr/sbin/nologin

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '$7~ /nologin$/ {print $0}' /etc/passwd                                    
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:992:992:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:105::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:105:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:x:106:108:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
pulse:x:108:110:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
saned:x:110:114::/var/lib/saned:/usr/sbin/nologin
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:116:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:117:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:118:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:x:115:65534::/nonexistent:/usr/sbin/nologin
stunnel4:x:990:990:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:122::/var/lib/geoclue:/usr/sbin/nologin
sslh:x:120:124::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:127::/nonexistent:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
_gophish:x:124:130::/var/lib/gophish:/usr/sbin/nologin
iodine:x:125:65534::/run/iodine:/usr/sbin/nologin
miredo:x:126:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:127:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin
mosquitto:x:130:133::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:131:134::/var/lib/inetsim:/usr/sbin/nologin

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '$1~ /^R/ && $3>400 && $3<700 {print $0}' /etc/passwd
                                                                                                                                                                                             
┌──(Sebastian㉿kali)-[~]                                                                                                                                                                     
└─$ awk -F ':' '$1~ /^R/ && $3>=400 && $3<=700 {print $0}' /etc/passwd                                                                                                                       
                                                                                                                                                                                             
┌──(Sebastian㉿kali)-[~]                                                                                                                                                                     
└─$ awk -F ':' '$1~ /^R/ && $3>=400 && $3<=700 {print $0}' /etc/passwd                                                                                                                       
                                                                                                                                                                                             
┌──(Sebastian㉿kali)-[~]                                                                                                                                                                     
└─$ awk -F ':' '$1~ /^r/ && $3>=400 && $3<=700 {print $0}' /etc/passwd                                                                                                                       
                                                                                                                                                                                             
┌──(Sebastian㉿kali)-[~]                                                                                                                                                                     
└─$ awk -F ':' '$1~ /^r/ && $3<=400 {print $0}' /etc/passwd                                                                                                                       
root:x:0:0:root:/root:/usr/bin/zsh
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin

┌──(Sebastian㉿kali)-[~]
└─$ awk -F ':' '$1~ /^r/ && $3<=400 && $5~ /root/ {print $0}' /etc/passwd                                                                                                                    
root:x:0:0:root:/root:/usr/bin/zsh


```

