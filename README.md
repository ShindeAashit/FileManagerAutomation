# File Management Automation Tool

Automates the sorting of downloaded files in real time using Python and Watchdog. Designed to streamline file organization by detecting new files and moving them to categorized folders based on type.

---

## 🚀 Overview

This tool monitors a specified download directory and automatically moves audio, video, and image files to their respective destination folders. It handles duplicate filenames gracefully and logs all actions for traceability.

Built with:
- 🐍 Python
- 👀 Watchdog (real-time file system monitoring)
- 📦 Shutil & OS (file operations)
- 🧠 Logging (status and error tracking)

---

## ✨ Features

- Real-time monitoring of download folder
- Automatic sorting into audio, video, and image folders
- Duplicate file handling with unique renaming
- Configurable file types and destination paths
- Lightweight and easy to run on any Windows system
- Clean logging for debugging and audit

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup
```bash
pip install watchdog
Clone the Repository
git clone https://github.com/ShindeAashit/file-management-automation.git
cd file-management-automation
▶️ Usage
Open file_management.py and update the following paths:

SOURCE_DIR = r"C:\Users\YourName\Downloads"
DEST_DIRS = {
    "audio": r"E:\Projects\DownloadedAudio",
    "video": r"E:\Projects\DownloadedVideo",
    "image": r"E:\Projects\DownloadedImage"
}
Run the script:

python file_management.py
Watch your files get sorted automatically!



