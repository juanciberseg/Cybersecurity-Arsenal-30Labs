# 🛡️ My Cybersecurity Engineering Journey: 30 Labs Arsenal

Welcome to my personal hands-on cybersecurity challenge! In this repository, I am moving away from just using pre-made security tools to understanding the engineering and computer science mechanisms behind them. 

Over this learning journey, I am building **30 automated python security scripts** interacting with the Linux Kernel, volatile memory (RAM), filesystems, and network sockets.

---

## 🔬 Lab 1/30: Ghost Process Monitor (RAM Forensics)

### 📌 Objective
Automate the detection of evasive malware that executes payload binary files from temporary directories and immediately deletes the binary from the disk to evade traditional antivirus software while remaining running as a "ghost process" inside the **volatile memory (RAM)**.

### 🛠️ Core Concepts Learned
* **`psutil.process_iter()`**: Interrogating the Linux operating system sub-systems to dynamically stream active processes.
* **`os.path.exists()`**: Cross-referencing running binary absolute paths with physical disk states.
* **Defense Evasion (MITRE ATT&CK T1070.004)**: Understanding how threat actors utilize `/tmp` spaces and unlinked descriptors for fileless execution.

### 💻 How It Works
The script maps every PID's execution path. If a process link exists in RAM but `os.path.exists(path)` evaluates to `False` or contains a `(deleted)` label, it flags a high-priority **[ALERT]**. Additionally, it triggers a **[WARNING]** for any process executing inside world-writable directories (`/tmp`, `/var/tmp`, `/dev/shm`).

### 🔧 How to Run
```bash
python3 ghost_process_monitor.py

### 📸 Proof of Concept (PoC)

Here is the script in action, successfully detecting the simulated defense evasion technique in real-time:<img width="944" height="348" alt="Lab1" src="https://github.com/user-attachments/assets/9f8d6978-efc5-4fdb-a72c-f3cfbcda0a57" />
