# 🛡️ My Cybersecurity Engineering Journey: 30 Security Labs

Welcome to my personal hands-on cybersecurity challenge!

The goal of this repository is to move beyond simply using existing security tools and start understanding the engineering principles behind them by building them from scratch.

Over the next three months, I will develop **30 Python-based cybersecurity laboratories**, exploring topics such as Linux internals, digital forensics, process monitoring, filesystem integrity, networking, threat detection, and security automation.

Each lab is designed to introduce a practical cybersecurity concept while helping me improve my Python programming skills.

---

# 🔬 Lab 1/30 — Ghost Process Monitor

## 📌 Objective

Build a Python-based process inspection tool for Linux systems that demonstrates basic process monitoring using simple heuristic checks.

Additionally, the tool detects processes executing from world-writable temporary directories such as `/tmp`, `/var/tmp`, and `/dev/shm`, locations that are commonly abused during malware execution and defense evasion techniques.

> **Note:** This project is intended for educational purposes to understand basic Linux process monitoring and introductory memory forensics concepts.

---

## 🛠️ Concepts Learned

During this lab I learned how to work with:

- `psutil.process_iter()` for enumerating active Linux processes.
- `os.path.exists()` for validating executable paths.
- Linux process metadata (`PID`, process name, executable path).
- Temporary directories commonly abused by malware.
- Basic process integrity verification.
- Exception handling while inspecting running processes.
- Introductory Digital Forensics & Incident Response (DFIR) concepts.

---

## 💻 How It Works

The script enumerates every active process running on the system.

For each process, it retrieves:

- Process ID (PID)
- Process name
- Executable path

The tool then performs two simple security checks:

### 🚨 Rule 1 — Deleted Executable Detection

If the executable path is no longer present on disk, the process is flagged as potentially suspicious.

### ⚠️ Rule 2 — Temporary Directory Detection

If the executable is running from one of the following directories:

- `/tmp`
- `/var/tmp`
- `/dev/shm`

the script generates a warning because these world-writable locations are frequently used during malware execution.

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/juanciberseg/Cybersecurity-Engineering-Labs.git
```

Install the required dependency:

```bash
pip3 install psutil
```

Run the script:

```bash
python3 ghost_process_monitor.py
```

---

## 📸 Proof of Concept (PoC)

The following demonstration simulates a common defense evasion scenario.

A copy of the Linux `sleep` binary is executed from the `/tmp` directory and kept running in the background. The executable file is then deleted while the process continues executing in memory.

The Ghost Process Monitor successfully detects:

- Suspicious behavior related to missing executable paths is detected using basic process inspection.
- A process executing from a temporary directory.

<img width="944" height="348" alt="Lab1" src="https://github.com/user-attachments/assets/6f71b72d-2b1b-4adf-9364-463483e4128c" />

---

## 🎯 Skills Practiced

- Python Automation
- Linux Process Monitoring
- Linux Filesystem
- Process Enumeration
- Digital Forensics (DFIR)
- Memory Forensics Fundamentals
- Defensive Security
- Threat Hunting Fundamentals

---

## 📚 Future Improvements

As I progress through future labs, I plan to improve this tool by adding features such as:

- JSON report generation
- CSV export
- Continuous monitoring mode
- Risk scoring
- Colorized terminal output
- Detection of additional suspicious execution patterns

---

## ⚠️ Disclaimer

This project was created exclusively for educational purposes as part of my Cybersecurity Engineering learning journey.

This project demonstrates simplified heuristic-based process monitoring techniques for educational purposes and is not intended to be used as a production-grade security solution.
