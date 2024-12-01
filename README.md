# SistemasOperativos





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

