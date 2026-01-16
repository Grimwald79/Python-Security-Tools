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

    python port_scanner.py
    # Follow prompts to enter target IP (e.g., 192.168.1.1)

### 2. File Integrity Checker
Calculates the SHA-256 checksum of any file. This is useful for verifying that downloaded files or system binaries have not been altered.

    python integrity_checker.py
    # Enter the path to the file you wish to verify

### 3. Password Policy Auditor
Checks strings against a mock corporate security policy (Length > 8, requires Uppercase, Lowercase, Number, and Special Character).

    python password_auditor.py
    # Input a password to receive a complexity score

---

## 🧠 Technical Highlights

### **Socket Programming & Networking**
The `port_scanner.py` script demonstrates an understanding of the TCP 3-way handshake. It utilizes the `socket` library to attempt connections, handling timeouts and connection refusals gracefully.

### **Cryptography & Hashing**
The `integrity_checker.py` script utilizes the **SHA-256** algorithm. It implements **chunk-based reading** (reading 4KB at a time) to ensure that large files (ISOs, logs) can be hashed without causing memory overflow errors, a critical consideration for system resources.

### **Regular Expressions (Regex)**
The `password_auditor.py` script moves beyond simple string matching. It uses specific regex patterns to validate input, a fundamental skill for sanitizing user data and preventing injection attacks.

---

## ⚠️ Disclaimer
These tools are intended for **educational purposes** and **authorized security testing** only. Always ensure you have permission before scanning networks you do not own.

---

**Author:** Joseph Vincent
**Focus:** Security Engineering & DevSecOps
