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

