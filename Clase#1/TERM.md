### Admin:
```bash                                                                        
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/passwd                     
root:x:0:0:root:/root:/usr/bin/zsh
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/groups
cat: /etc/groups: No such file or directory
                                                                             
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/group 
root:x:0:
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
### Lorena

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

### Marcela

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

### Anacreta

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