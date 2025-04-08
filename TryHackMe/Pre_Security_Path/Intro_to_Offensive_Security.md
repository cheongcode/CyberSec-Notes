**Task 1**

Offensive security involves breaking into systems, exploiting bugs, and finding vulnerabilities to gain unauthorized access, while defensive security focuses on protecting systems by analyzing and securing against digital threats. Offensive roles simulate a hacker’s actions to find weaknesses and recommend patches, whereas defensive roles investigate hacks, track cybercriminals, and monitor for malicious activity.

Answer the questions below

Which of the following options better represents the process where you simulate a hacker's actions to find vulnerabilities in a system?  

- Offensive Security
- Defensive Security

Answer:
```
Offensive Security
```

**Task 2**

We will use a command-line application called "GoBuster" to brute-force FakeBank's website to find hidden directories and pages. GoBuster will take a list of potential page or directory names and tries accessing a website with each of them; if the page exists, it tells you.

I'm just gonna use TryHackMe's virtual machine for this exercise

![Output](TryHackMe/Pre_Security_Path/Images/1.jpg)


We will be running GoBuster for this simple exercise , so just open the terminal and copy and paste the code in based on the instructions:
```
gobuster -u http://fakebank.com -w wordlist.txt dir
```
![Output](TryHackMe/Pre_Security_Path/Images/2.jpg)

**Gobuster** is a tool used for brute-forcing URLs, directories, DNS subdomains, and virtual host names on web servers. It helps identify hidden resources, directories, or files by testing various wordlists against the target, which is useful in penetration testing and vulnerability assessments. (Thought you might be wondering what it does so here's something by ChatGPT)

You should have found a secret bank transfer page that allows you to transfer money between accounts at the bank (/bank-transfer). Type the hidden page into the FakeBank website on the machine.
This page allows an attacker to steal money from any bank account, which is a critical risk for the bank. As an ethical hacker, you would (with permission) find vulnerabilities in their application and report them to the bank to fix before a hacker exploits them.  

Transfer $2000 from the bank account 2276, to your account (account number 8881).
![Output](TryHackMe/Pre_Security_Path/Images/3.jpg)
If your transfer was successful, you should now be able to see your new balance reflected on your account page. Go there now and confirm you got the money! (You may need to hit Refresh for the changes to appear)
![Output](TryHackMe/Pre_Security_Path/Images/4.jpg)
Above your account balance, you should now see a message indicating the answer to this question. Can you find the answer you need?
Answer:
```
BANK-HACKED
```

Feel like a hacker yet ? 