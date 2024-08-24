# SistemasOperativos

## Clase 24/08/2024

### Admin:
```bash                                                                        
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
systemd-timesync:x:997:997:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:107::/nonexistent:/usr/sbin/nologin
tss:x:101:109:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:110::/nonexistent:/usr/sbin/nologin
usbmux:x:104:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
dnsmasq:x:106:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
avahi:x:107:112:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:108:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
saned:x:109:115::/var/lib/saned:/usr/sbin/nologin
lightdm:x:110:116:Light Display Manager:/var/lib/lightdm:/bin/false
polkitd:x:996:996:polkit:/nonexistent:/usr/sbin/nologin
rtkit:x:111:117:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:118:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:119:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:120:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
mysql:x:115:122:MySQL Server,,,:/nonexistent:/bin/false
stunnel4:x:995:995:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:116:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:117:124::/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:x:118:125::/var/lib/snmp:/bin/false
sslh:x:119:127::/nonexistent:/usr/sbin/nologin
ntpsec:x:120:130::/nonexistent:/usr/sbin/nologin
redsocks:x:121:131::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:122:65534::/var/spool/rwho:/usr/sbin/nologin
iodine:x:123:65534::/run/iodine:/usr/sbin/nologin
miredo:x:124:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:125:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:126:132::/var/lib/redis:/usr/sbin/nologin
postgres:x:127:133:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
mosquitto:x:128:135::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:129:136::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:130:138::/var/lib/openvas:/usr/sbin/nologin
king-phisher:x:131:139::/var/lib/king-phisher:/usr/sbin/nologin
kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh
fwupd-refresh:x:132:142:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
Debian-gdm:x:133:143:Gnome Display Manager:/var/lib/gdm3:/bin/false
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/groups
cat: /etc/groups: No such file or directory
                                                                             
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
audio:x:29:kali
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
crontab:x:101:
input:x:102:
sgx:x:103:
kvm:x:104:
render:x:105:
netdev:x:106:kali
systemd-timesync:x:997:
messagebus:x:107:
_ssh:x:108:
tss:x:109:
tcpdump:x:110:
bluetooth:x:111:kali
avahi:x:112:
pipewire:x:113:
scanner:x:114:saned,kali
saned:x:115:
lightdm:x:116:
polkitd:x:996:
rtkit:x:117:
colord:x:118:
nm-openvpn:x:119:
nm-openconnect:x:120:
kali-trusted:x:121:
mysql:x:122:
rdma:x:123:
stunnel4:x:995:stunnel4
geoclue:x:124:
Debian-snmp:x:125:
kismet:x:126:
sslh:x:127:
ssl-cert:x:128:postgres
i2c:x:129:
ntpsec:x:130:
redsocks:x:131:
redis:x:132:_gvm
postgres:x:133:
plocate:x:134:
mosquitto:x:135:
sambashare:x:994:
inetsim:x:136:
wireshark:x:137:kali
_gvm:x:138:
kpadmins:x:139:
kali:x:1000:
kaboxer:x:140:kali
vboxsf:x:141:kali
fwupd-refresh:x:142:
Debian-gdm:x:143:
Matematicas:x:1002:
Fisica:x:1003:
Linux25:x:1004:
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# useradd -g Linux25 -d /home/labor -m -s /bin/bash Anacreta
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# useradd -g Matematicas -d /home/prac -m -s /bin/bash Marcela
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# passwd Anacreta
New password: 
Retype new password: 
No password has been supplied.
New password: 
Retype new password: 
passwd: password updated successfully
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# passwd Marcela 
New password: 
Retype new password: 
passwd: password updated successfully
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# passwd Anacreta
New password: 
Retype new password: 
Sorry, passwords do not match.
passwd: Authentication token manipulation error
passwd: password unchanged
                                                                                 
┌──(root㉿kali)-[/home/kali]
└─# passwd Anacreta
New password: 
Retype new password: 
passwd: password updated successfully
                                                                                 
┌──(root㉿kali)-[/home/kali]
└─# useradd -g Fisica -d /home/ejer -m -s /bin/bash Lorena
                                                                                 
┌──(root㉿kali)-[/home/kali]
└─# passwd Lorena                                         
New password: 
Retype new password: 
passwd: password updated successfully
                                                                                 
┌──(root㉿kali)-[/home/kali]
└─# ls
Desktop    Downloads  Pictures  Templates
Documents  Music      Public    Videos
                                                   
┌──(root㉿kali)-[/home/kali]
└─# cd ..         
                                                   
┌──(root㉿kali)-[/home]
└─# ls
ejer  kali  labor  prac
                                                   
┌──(root㉿kali)-[/home]
└─# dir
ejer  kali  labor  prac
                                                   
┌──(root㉿kali)-[/home]
└─# cd ..
                                                   
┌──(root㉿kali)-[/]
└─# dir
bin             lib         opt       sys
boot            lib32       proc      tmp
dev             lib64       root      usr
etc             libx32      run       var
home            lost+found  sbin      vmlinuz
initrd.img      media       srv       vmlinuz.old
initrd.img.old  mnt         swapfile
                                                   
┌──(root㉿kali)-[/]
└─# cd bin
┌──(root㉿kali)-[/bin]
└─# chmod 747 cat
                                                   
┌──(root㉿kali)-[/bin]
└─# chmod 555 grep 
                                                   
┌──(root㉿kali)-[/bin]
└─# chmod 555 wc  
                                                   
┌──(root㉿kali)-[/bin]
└─# chmod 555 more
                                                   
┌──(root㉿kali)-[/bin]
└─# chmod 555 less
                                                   
┌──(root㉿kali)-[/bin]
└─# chmod 555 nl  
                                                   
┌──(root㉿kali)-[/bin]
└─# which cat
/usr/bin/cat

```
## Lorena

```bash
┌──(kali㉿kali)-[~]
└─$ su - Lorena
Password: 
┌──(Lorena㉿kali)-[~]
└─$ pico datos3

┌──(Lorena㉿kali)-[~]
└─$ more datos3
Marta Ochoa             22
Opita Lora              18
Marta Usuga             22
Julia Lopez             19






























(END)
[1]+  Stopped                 more datos3

┌──(Lorena㉿kali)-[~]
└─$ less datos3

[2]+  Stopped                 less datos3

┌──(Lorena㉿kali)-[~]
└─$ ls                                                    
datos3

┌──(Lorena㉿kali)-[~]
└─$ more datos3
Marta Ochoa             22
Opita Lora              18
Marta Usuga             22
Julia Lopez             19






























┌──(Lorena㉿kali)-[~]
└─$ chmod 666 datos3                                      

┌──(Lorena㉿kali)-[~]
└─$ ls -l datos3                                          
-rw-rw-rw- 1 Lorena Fisica 63 Aug 24 09:38 datos3

┌──(Lorena㉿kali)-[~]
└─$       
```

## Marcela

```bash
┌──(kali㉿kali)-[~]
└─$ su - Marcela
Password: 
┌──(Marcela㉿kali)-[~]
└─$ pico datos2

┌──(Marcela㉿kali)-[~]
└─$ more datos2
Opita Montoya           16
Opita Correa            40
Emma Perez              28
Debia Toro              39










┌──(Marcela㉿kali)-[~]
└─$ chmod 666 datos2

┌──(Marcela㉿kali)-[~]
└─$ ls -l datos2
-rw-rw-rw- 1 Marcela Matematicas 65 Aug 24 09:37 datos2

┌──(Marcela㉿kali)-[~]
└─$                                 
```

## Anacreta

```bash
                                                                                 
┌──(kali㉿kali)-[~]
└─$ su - Anacreta
Password: 
┌──(Anacreta㉿kali)-[~]
└─$ pico datos1

┌──(Anacreta㉿kali)-[~]
└─$ more datos1
Rufina Ruiz             21
Rufina Garcia           16
Optica Seguro           40
Luisa Manco             25











┌──(Anacreta㉿kali)-[~]
└─$ ls -l datos1
-rw-r--r-- 1 Anacreta Linux25 69 Aug 24 09:36 datos1

┌──(Anacreta㉿kali)-[~]
└─$ chmod 666 datos1                                

┌──(Anacreta㉿kali)-[~]
└─$ ls -l datos1
-rw-rw-rw- 1 Anacreta Linux25 69 Aug 24 09:36 datos1

┌──(Anacreta㉿kali)-[~]
└─$ ls -l /etc/cat
ls: cannot access '/etc/cat': No such file or directory

┌──(Anacreta㉿kali)-[~]
└─$ cat datos1 datos2 datos3 | grep Opita | wc -l
cat: datos2: No such file or directory
cat: datos3: No such file or directory
0

┌──(Anacreta㉿kali)-[~]
└─$ cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita | wc -l
3

┌──(Anacreta㉿kali)-[~]
└─$ cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita 
Opita Montoya           16
Opita Correa            40
Opita Lora              18

┌──(Anacreta㉿kali)-[~]
└─$ vi datos1                                       

┌──(Anacreta㉿kali)-[~]
└─$ cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita
Opita Seguro            40
Opita Montoya           16
Opita Correa            40
Opita Lora              18

┌──(Anacreta㉿kali)-[~]
└─$ cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita | wc -l
4

┌──(Anacreta㉿kali)-[~]
└─$ 

```
