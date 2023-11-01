import os
import logging
from shutil import move
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from time import sleep

audioSuffix = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]

videoSuffix = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", 
               ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".m2ts"]

docSuffix = [".pdf", ".ppt", ".pptx", ".xls", ".xlsx", ".odt", ".doc", ".docx", ".zip"]

imgSuffix = [".jpg", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw",
             ".cr2", ".nrw", ".k25",".bmp", ".dib", ".heif", ".heic", ".indd", ".ind", ".indt",
             ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".jfif",
             ".gif", ".jif", ".jfi", ".jpe"]


source_directory = "/Users/aaron/Downloads"


def moveFile(dest, entry, name):
    fileExists = os.path.exists(dest + "/" + name)
    if fileExists:
        os.rename(entry, name + " (dupe name)")
    move(entry, dest)


class MoveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_directory) as entries:
            for entry in entries:
                dest = source_directory
                name = entry.name
                suffix = os.path.splitext(name)[1].lower()
                print(suffix)
                if suffix in audioSuffix:
                    dest = "/Users/aaron/Documents/Downloaded Audio"
                elif suffix in videoSuffix:
                    dest = "/Users/aaron/Documents/Downloaded VIDs"
                elif suffix in docSuffix:
                    dest = "/Users/aaron/Documents/Downloaded DOCs"
                elif suffix in imgSuffix:
                    dest = "/Users/aaron/Documents/Downloaded IMGs"
                else:
                    dest = "/Users/aaron/Documents/Downloaded MISC"
                
                moveFile(dest, entry, name)

                
        
if __name__ == "__main__":
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
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()