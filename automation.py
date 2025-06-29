#!/usr/bin/env python3

import os
import tarfile
import shutil
import datetime
import subprocess

# Define paths and filenames
backup_source = "/home/yourusername/Documents"
backup_dest = "/home/yourusername/backup"
log_file = "/home/yourusername/automation_log.txt"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log(message):
    with open(log_file, "a") as logf:
        logf.write(f"[{timestamp}] {message}\n")
    print(message)

def update_system():
    log("Updating system...")
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        log("System update completed successfully.")
    except subprocess.CalledProcessError as e:
        log(f"System update failed: {e}")

def backup_files():
    log(f"Backing up files from {backup_source} to {backup_dest}")
    try:
        os.makedirs(backup_dest, exist_ok=True)
        backup_filename = f"backup_{datetime.datetime.now().strftime('%Y-%m-%d')}.tar.gz"
        backup_path = os.path.join(backup_dest, backup_filename)
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(backup_source, arcname=os.path.basename(backup_source))
        log(f"Backup completed: {backup_path}")
    except Exception as e:
        log(f"Backup failed: {e}")

def clean_temp_files():
    log("Cleaning up /tmp files...")
    try:
        tmp_dir = "/tmp"
        for filename in os.listdir(tmp_dir):
            file_path = os.path.join(tmp_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                log(f"Failed to delete {file_path}: {e}")
        log("Temporary files cleaned.")
    except Exception as e:
        log(f"Error during cleanup: {e}")

def main():
    log("========= Automation Script Started =========")
    update_system()
    backup_files()
    clean_temp_files()
    log("========= Automation Script Finished =========\n")

if __name__ == "__main__":
    main()
