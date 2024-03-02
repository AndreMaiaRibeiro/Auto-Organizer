import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog
from collections import defaultdict
import ctypes

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def create_folder(path, name):
    """Create a folder if it does not exist."""
    path = os.path.join(path, name) 
    os.makedirs(path, exist_ok=True) 
    return path

def move_files(disk, downloads_path, folder_name, files):
    """Move files to the specified folder."""
    directory_path = create_folder(disk, folder_name)
    for file_name in files:
        source_file = os.path.join(downloads_path, file_name)
        destination_file = os.path.join(directory_path, file_name)
        if os.path.exists(destination_file):
            print(f"File '{file_name}' already exists in {directory_path}")
        else:
            shutil.move(source_file, destination_file)

def get_destination_disk():
    """Get the destination disk location from user."""
    config_file = "config.json"
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            config = json.load(file)
            destination_disk = config.get("destination_disk", "")
    else:
        destination_disk = ""

    if not destination_disk or not os.path.exists(destination_disk):
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        destination_disk = filedialog.askdirectory(title="Select Destination Disk")
        
        # Save selected location to config file
        with open(config_file, "w") as file:
            json.dump({"destination_disk": destination_disk}, file)

    return destination_disk

downloads_path = os.path.join(os.environ['USERPROFILE'], "Downloads")

extensions_mapping = {
    "Photos": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".doc", ".docx"],
    "PDF": [".pdf"],
    "Zip": [".zip", ".rar"],
    "Videos": [".webm", ".mkv", ".mov", ".mp4", ".m4p", ".m4v", ".m4a"],
    "Audio": [".mp3"],
    "Excel": [".xlsx"],
    "Text": [".txt"],
    "Extra": []
}

files_list = defaultdict(list)

for file_name in os.listdir(downloads_path):
    for category, extensions in extensions_mapping.items():
        if any(file_name.lower().endswith(ext) for ext in extensions):
            files_list[category].append(file_name)
            break
    else:
        files_list["Extra"].append(file_name)

destination_disk = get_destination_disk()

for category, files in files_list.items():
    move_files(destination_disk, downloads_path, category, files)

Mbox('Organizer Folder', f"Your Download Folder as been organized to the folder {destination_disk}", 0)
