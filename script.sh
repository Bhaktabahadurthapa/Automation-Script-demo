#!/bin/bash

# =============================
# Basic System Automation Script
# Author: Bhakta Thapa
# Date: 2025-06-29
# =============================

# Define variables
BACKUP_SOURCE="/home/yourusername/Documents"
BACKUP_DEST="/home/yourusername/backup"
LOG_FILE="/home/yourusername/automation_log.txt"

echo "===============================" >> "$LOG_FILE"
echo "Automation Script Run: $(date)" >> "$LOG_FILE"
echo "===============================" >> "$LOG_FILE"

# Step 1: Update the system
echo "[1] Updating system..." | tee -a "$LOG_FILE"
sudo apt update && sudo apt upgrade -y >> "$LOG_FILE" 2>&1
echo "System update completed." >> "$LOG_FILE"

# Step 2: Backup important files
echo "[2] Backing up files from $BACKUP_SOURCE to $BACKUP_DEST" | tee -a "$LOG_FILE"
mkdir -p "$BACKUP_DEST"
tar -czf "$BACKUP_DEST/backup_$(date +%F).tar.gz" "$BACKUP_SOURCE" >> "$LOG_FILE" 2>&1
echo "Backup completed." >> "$LOG_FILE"

# Step 3: Clean up temp files
echo "[3] Cleaning up temporary files..." | tee -a "$LOG_FILE"
sudo rm -rf /tmp/* >> "$LOG_FILE" 2>&1
echo "Temporary files cleaned." >> "$LOG_FILE"

# Step 4: Finish and log
echo "[✓] Automation complete on $(date)" | tee -a "$LOG_FILE"
echo "" >> "$LOG_FILE"
