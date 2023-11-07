import os
import logging
import tkinter as tk
from file_information import folder_locations, file_extensions as extensions
from tkinter import filedialog
from shutil import move
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from time import sleep

root = tk.Tk()
root.withdraw()

print("Script starting...")
# check if the folders are already assigned
with open("file_locations.txt", "r") as f:
    folders = f.readlines()

while "\n" in folders:
    for i, folder in enumerate(folder_locations):
        if folder_locations[folder] == "":
            print(f"Choose the location for the {folder}")
            folders[i] = filedialog.askdirectory() + "\n"
            folder_locations[folder] = filedialog.askdirectory()

with open("file_locations.txt", "w") as f:
    f.writelines(folders)


source_directory = folder_locations["SourceFolder"] # The folder that is being checked from


def moveFile(dest, entry, name):
    fileExists = os.path.exists(dest + "/" + name)
    counter = 0
    while True:
        if fileExists: # checks if the file name already exists before sending to its folder
            os.rename(entry, name + f" ({counter})") # renames the file name to avoid errors
            counter += 1
        else:
            break
    move(entry, dest)


class MoveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_directory) as entries:
            for entry in entries: # goes through each file in the source_directory folder
                dest = source_directory
                name = entry.name
                suffix = os.path.splitext(name)[1].lower() # grabs the file extension
                if suffix in extensions["audio"]: # checks the file type and assigns it to a corresponding folder
                    dest = folder_locations["AudioFolder"]
                elif suffix in extensions["video"]:
                    dest = folder_locations["VideoFolder"]
                elif suffix in extensions["document"]:
                    dest = folder_locations["DocumentFolder"]
                elif suffix in extensions["image"]:
                    dest = folder_locations["ImageFolder"]
                else:
                    dest = folder_locations["MiscFolder"]
                
                moveFile(dest, entry, name) # moves file to the destination folder

                
        
if __name__ == "__main__": # checks if the folder is ever modified and runs the code
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_directory
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(1) # prevents excessive looping
    except KeyboardInterrupt:
        observer.stop() # ends code
        print("Script ending...")
    observer.join()