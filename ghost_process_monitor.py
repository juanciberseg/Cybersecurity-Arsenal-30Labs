import psutil
import os
import datetime 

def scan_processes():
 print(f"[*] Audit Started: {datetime.datetime.now()}")
 print("-" * 65)
 print(f"{'PID':<7} | {'NAME':<20} | {'STATUS'}")
 print("-" * 65)

# SECURITY RULE 1:Stream and inspect all active processes running in volatile memory (RAM)
 for proc in psutil.process_iter(['pid', 'name', 'exe']):
    try:
        pid = proc.info['pid']
        name = proc.info['name']
        path = proc.info['exe']
        # SECURITY RULE 2: Detect "ghost processes" (payloads unlinked/deleted from disk but active in RAM)
        if path and(not os.path.exists(path) or "(deleted)" in path):
            print(f"[ALERT] GHOST PROCESS: {name} (PID: {pid})")
            print(f"    Path: {path} (Deleted from disk)")
        # SECURITY RULE 3: Identify binaries executing from world-writable temporary directories
        temp_paths = ["/tmp", "/var/tmp", "/dev/shm"]
        if path and any(tp in path for tp in temp_paths):
            print(f"[WARNING] TEMP FOLDER EXECUTION: {name} (PID: {pid})")
            print(f"    Path: {path}")
    # Exception Handling: Prevent script crash if a process terminates or denies access during inspection
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        continue

if __name__ == "__main__":
    scan_processes()
    print("-" * 65)
    print("[*]Scan finished.")
