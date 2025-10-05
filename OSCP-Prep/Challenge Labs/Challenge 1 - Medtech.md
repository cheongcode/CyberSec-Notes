About this lab

This advanced lab challenges participants to navigate a realistic, multi-machine enterprise network, beginning with the exploitation of a SQL injection vulnerability on a public-facing web server. The vulnerability is used to achieve remote code execution and escalate privileges locally. From there, you'll harvest credentials, perform lateral movement, and pivot into internal systems like FILES02 and CLIENT02. Continue compromising additional hosts such as DEV04 using misconfigurations and token impersonation techniques, ultimately targeting the domain controller (DC01) and PROD01 to achieve full domain compromise.
## After completing this lab, learners will be able to:

- Identify and exploit a SQL injection vulnerability on WEB02 to gain initial access and execute commands.
- Escalate privileges on the WEB02 machine and extract credentials for lateral movement.
- Use pivoting techniques to access internal machines such as FILES02 and CLIENT02, leveraging stolen credentials.
- Escalate privileges on DEV04 and utilize compromised accounts to attack DC01 for domain admin access.
- Compromise PROD01 and finalize the domain takeover, securing all proof flags.

