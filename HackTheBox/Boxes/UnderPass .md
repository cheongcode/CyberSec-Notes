Category: Linux
Difficulty: Easy


| `-sC` | Run default scripts           | Uses **Nmap’s default scripts** (`/usr/share/nmap/scripts/`) to gather additional information about the target. Equivalent to `--script=default`. |
| ----- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-sV` | Service and Version detection | Attempts to determine the exact **version** of services running on open ports (e.g., Apache 2.4.52, OpenSSH 8.9).                                 |
| `-Pn` | No ping (assume host is up)   | Skips the **ICMP ping check**, useful when a firewall blocks pings.                                                                               |
| `-T4` | Aggressive timing             | **Speeds up the scan** by sending packets faster (T0 = slowest, T5 = fastest, T4 is a good balance).                                              |

```
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.11.48 -sSCV -Pn -T4
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-18 23:36 EST
Nmap scan report for 10.10.11.48
Host is up (0.045s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 48:b0:d2:c7:29:26:ae:3d:fb:b7:6b:0f:f5:4d:2a:ea (ECDSA)
|_  256 cb:61:64:b8:1b:1b:b5:ba:b8:45:86:c5:16:bb:e2:a2 (ED25519)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.40 seconds

```


| `-sU` | UDP Scan      | Scans **only UDP ports**, which are often ignored in regular scans. |
| ----- | ------------- | ------------------------------------------------------------------- |
| `-T5` | Insane Timing | **Fastest scan speed**, but can be unreliable due to packet drops.  |


```
┌──(kali㉿kali)-[~]
└─$ nmap -sU 10.10.11.48 -T5      
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-18 23:36 EST
Warning: 10.10.11.48 giving up on port because retransmission cap hit (2).
Nmap scan report for 10.10.11.48
Host is up (0.045s latency).                                                                                                                               
Not shown: 854 open|filtered udp ports (no-response), 145 closed udp ports (port-unreach)                                                                  
PORT    STATE SERVICE                                                                                                
161/udp open  snmp                                                                                                                           
Nmap done: 1 IP address (1 host up) scanned in 146.71 seconds 
```

sudo nmap -sU -T4 --min-rate=2000 --max-retries=2 -p- 10.10.11.48
or we can use this ^

- **`--min-rate=2000`** → Sends **at least 2000 packets/sec** (faster results).
- **`--max-retries=2`** → Allows some retries for better accuracy.
- **`-p-`** → Scans **all 65,535 UDP ports**.

```
┌──(kali㉿kali)-[~]
└─$ snmp-check 10.10.11.48                                                               
snmp-check v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)

[+] Try to connect to 10.10.11.48:161 using SNMPv1 and community 'public'

[*] System information:

  Host IP address               : 10.10.11.48
  Hostname                      : UnDerPass.htb is the only daloradius server in the basin!
  Description                   : Linux underpass 5.15.0-126-generic #136-Ubuntu SMP Wed Nov 6 10:38:22 UTC 2024 x86_64
  Contact                       : steve@underpass.htb
  Location                      : Nevada, U.S.A. but not Vegas
  Uptime snmp                   : 08:50:32.53
  Uptime system                 : 08:50:22.15
  System date                   : 2025-2-19 04:34:18.0

```


```
└─$ dirsearch -u "http://10.10.11.48/daloradius/" -t 50 

/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3                                                                                                                                                
Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 50 | Wordlist size: 11460

Output File: /home/kali/reports/http_10.10.11.48/_daloradius__25-02-19_00-03-19.txt

Target: http://10.10.11.48/

[00:03:19] Starting: daloradius/                                                                                                                           
[00:03:22] 200 -  221B  - /daloradius/.gitignore                            
[00:03:28] 301 -  319B  - /daloradius/app  ->  http://10.10.11.48/daloradius/app/
[00:03:29] 200 -   24KB - /daloradius/ChangeLog                             
[00:03:31] 200 -    2KB - /daloradius/docker-compose.yml                    
[00:03:31] 200 -    2KB - /daloradius/Dockerfile                            
[00:03:31] 301 -  319B  - /daloradius/doc  ->  http://10.10.11.48/daloradius/doc/
[00:03:34] 301 -  323B  - /daloradius/library  ->  http://10.10.11.48/daloradius/library/
[00:03:34] 200 -   18KB - /daloradius/LICENSE                               
[00:03:37] 200 -   10KB - /daloradius/README.md                             
[00:03:38] 301 -  321B  - /daloradius/setup  ->  http://10.10.11.48/daloradius/setup/
Task Completed   
```

```
┌──(kali㉿kali)-[~]
└─$ feroxbuster -u http://10.10.11.48/daloradius/ -t 200 -r

                                                                                                                                                           
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.11.48/daloradius/
 🚀  Threads               │ 200
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 📍  Follow Redirects      │ true
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        9l       31w      273c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       28w      276c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       19l      120w    10373c http://10.10.11.48/daloradius/app/users/static/images/daloradius_small.png
200      GET       15l       70w     5742c http://10.10.11.48/daloradius/app/users/static/images/favicon/favicon-32x32.png
200      GET        1l        1w      263c http://10.10.11.48/daloradius/app/users/static/images/favicon/site.webmanifest
200      GET        7l       21w     1707c http://10.10.11.48/daloradius/app/users/static/images/favicon/favicon-16x16.png
200      GET      146l      911w    74623c http://10.10.11.48/daloradius/app/users/static/images/favicon/apple-touch-icon.png
200      GET        7l     1222w    80420c http://10.10.11.48/daloradius/app/users/static/js/bootstrap.bundle.min.js
200      GET        5l       21w    85875c http://10.10.11.48/daloradius/app/users/static/css/icons/bootstrap-icons.min.css
200      GET        7l     2189w   194901c http://10.10.11.48/daloradius/app/users/static/css/bootstrap.min.css
200      GET      112l      352w     4421c http://10.10.11.48/daloradius/app/users/login.php
200      GET      340l     2968w    18011c http://10.10.11.48/daloradius/LICENSE
[####################] - 65s   330017/330017  0s      found:10      errors:272563 
[####################] - 31s    30000/30000   977/s   http://10.10.11.48/daloradius/ 
[####################] - 30s    30000/30000   991/s   http://10.10.11.48/daloradius/library/ 
[####################] - 30s    30000/30000   988/s   http://10.10.11.48/daloradius/doc/ 
[####################] - 29s    30000/30000   1025/s  http://10.10.11.48/daloradius/contrib/ 
[####################] - 27s    30000/30000   1113/s  http://10.10.11.48/daloradius/setup/ 
[####################] - 58s    30000/30000   521/s   http://10.10.11.48/daloradius/app/ 
[####################] - 23s    30000/30000   1312/s  http://10.10.11.48/daloradius/contrib/db/ 
[####################] - 23s    30000/30000   1325/s  http://10.10.11.48/daloradius/app/common/ 
[####################] - 22s    30000/30000   1357/s  http://10.10.11.48/daloradius/app/common/includes/ 
[####################] - 22s    30000/30000   1347/s  http://10.10.11.48/daloradius/app/common/templates/ 
[####################] - 22s    30000/30000   1346/s  http://10.10.11.48/daloradius/app/common/library/                                                                                                                                                                  
```

Re fuzz again

```
─$ feroxbuster -u http://10.10.11.48/daloradius/app -t 200 -r
                                                                                                                                                           
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.11.48/daloradius/app
 🚀  Threads               │ 200
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 📍  Follow Redirects      │ true
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        9l       31w      273c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       28w      276c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       15l       70w     5742c http://10.10.11.48/daloradius/app/users/static/images/favicon/favicon-32x32.png
200      GET      146l      911w    74623c http://10.10.11.48/daloradius/app/users/static/images/favicon/apple-touch-icon.png
200      GET        5l       21w    85875c http://10.10.11.48/daloradius/app/users/static/css/icons/bootstrap-icons.min.css
200      GET        7l     1222w    80420c http://10.10.11.48/daloradius/app/users/static/js/bootstrap.bundle.min.js
200      GET      112l      352w     4421c http://10.10.11.48/daloradius/app/users/login.php
200      GET       19l      120w    10373c http://10.10.11.48/daloradius/app/users/static/images/daloradius_small.png
200      GET        7l     2189w   194901c http://10.10.11.48/daloradius/app/users/static/css/bootstrap.min.css
200      GET        1l        1w      263c http://10.10.11.48/daloradius/app/users/static/images/favicon/site.webmanifest
200      GET        7l       21w     1707c http://10.10.11.48/daloradius/app/users/static/images/favicon/favicon-16x16.png
200      GET        1l        1w      263c http://10.10.11.48/daloradius/app/operators/static/images/favicon/site.webmanifest
200      GET        7l     1222w    80420c http://10.10.11.48/daloradius/app/operators/static/js/bootstrap.bundle.min.js
200      GET      146l      911w    74623c http://10.10.11.48/daloradius/app/operators/static/images/favicon/apple-touch-icon.png
200      GET       97l      192w     2763c http://10.10.11.48/daloradius/app/operators/login.php
200      GET       19l      120w    10373c http://10.10.11.48/daloradius/app/operators/static/images/daloradius_small.png
200      GET       15l       70w     5742c http://10.10.11.48/daloradius/app/operators/static/images/favicon/favicon-32x32.png
200      GET        7l       21w     1707c http://10.10.11.48/daloradius/app/operators/static/images/favicon/favicon-16x16.png
200      GET        7l     2189w   194901c http://10.10.11.48/daloradius/app/operators/static/css/bootstrap.min.css
200      GET        1l        1w        6c http://10.10.11.48/daloradius/app/common/library/dompdf/VERSION
[####################] - 2m    210032/210032  0s      found:18      errors:7097   
[####################] - 40s    30000/30000   745/s   http://10.10.11.48/daloradius/app/ 
[####################] - 48s    30000/30000   619/s   http://10.10.11.48/daloradius/app/common/ 
[####################] - 68s    30000/30000   440/s   http://10.10.11.48/daloradius/app/common/library/ 
[####################] - 74s    30000/30000   405/s   http://10.10.11.48/daloradius/app/common/templates/ 
[####################] - 59s    30000/30000   507/s   http://10.10.11.48/daloradius/app/common/includes/ 
[####################] - 76s    30000/30000   394/s   http://10.10.11.48/daloradius/app/common/library/phpmailer/ 
[####################] - 58s    30000/30000   516/s   http://10.10.11.48/daloradius/app/common/library/dompdf/     
```

![[Pasted image 20250219142818.png]]
![[Pasted image 20250219142743.png]]
![[Pasted image 20250219143048.png]]

mosh --server="sudo /usr/bin/mosh-server" localhost

sudo /usr/bin/mosh-server new -p 61113
MOSH_KEY=QzOh2gOWZ3672OIDhszC0A mosh-client 127.0.0.1 61113
