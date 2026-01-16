# 🛡️ Python Security Automation Tools

A collection of Python scripts designed to demonstrate core concepts in **offensive security**, **data integrity**, and **compliance automation**. 

These tools were built to explore low-level network interactions, cryptographic hashing, and input validation without relying on pre-built enterprise tools.

## 📂 Project Overview

| Tool | File Name | Key Libraries | Description |
| :--- | :--- | :--- | :--- |
| **Network Port Scanner** | `port_scanner.py` | `socket`, `datetime` | Scans a target IP for open ports to identify potential entry points. |
| **File Integrity Monitor** | `integrity_checker.py` | `hashlib`, `os` | Generates SHA-256 hashes to detect unauthorized file tampering. |
| **Password Policy Auditor** | `password_auditor.py` | `re` (Regex) | Validates password complexity against strict security policies. |

---

## 🚀 Usage Guide

### Prerequisites
* Python 3.x installed
* No external dependencies required (uses standard library only)

### 1. Network Port Scanner
Performs a TCP connect scan on a specified range of ports.
```bash
python port_scanner.py
# Follow prompts to enter target IP (e.g., 192.168.1.1)
