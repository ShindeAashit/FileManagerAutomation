import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# === CONFIGURATION ===
SOURCE_DIR = r"C:\Users\Aditi\Downloads"
DEST_DIRS = {
    "audio": r"E:\Projects\DownloadedAudio",
    "video": r"E:\Projects\DownloadedVideo",
    "image": r"E:\Projects\DownloadedImage"
}
FILE_TYPES = {
    "audio": [".mp3", ".wav"],
    "video": [".mp4", ".mov"],
    "image": [".jpeg", ".jpg", ".png"]
}

# === UTILITY FUNCTIONS ===
def make_unique_name(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1
    new_name = name
    while os.path.exists(os.path.join(dest, new_name)):
        new_name = f"{filename}_{counter}{extension}"
        counter += 1
    return new_name

def move_file(dest, entry):
    try:
        name = entry.name
        src_path = entry.path
        dest_path = os.path.join(dest, name)

        if os.path.exists(dest_path):
            name = make_unique_name(dest, name)
            dest_path = os.path.join(dest, name)

        shutil.move(src_path, dest_path)
        logging.info(f"Moved: {src_path} → {dest_path}")
    except Exception as e:
        logging.error(f"Error moving file {entry.name}: {e}")

# === EVENT HANDLER ===
class FileMoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(SOURCE_DIR) as entries:
            for entry in entries:
                if entry.is_file():
                    for category, extensions in FILE_TYPES.items():
                        if entry.name.lower().endswith(tuple(extensions)):
                            move_file(DEST_DIRS[category], entry)
                            break

# === MAIN EXECUTION ===
def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    observer = Observer()
    event_handler = FileMoverHandler()
    observer.schedule(event_handler, SOURCE_DIR, recursive=False)
    observer.start()
    logging.info("File Management Automation started...")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("File Management Automation stopped.")
    observer.join()

if __name__ == "__main__":
    main()