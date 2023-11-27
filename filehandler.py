import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Sayed/Downloads"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey!! A file was created in {event.src_path}!!")
    def on_deleted(self, event):
        print(f"Warning!! A file was deleted in {event.src_path}!!")
    def on_modified(self, event):
       print(f"Warning!! A file was modified in {event.src_path}!!")
    def on_moved(self, event):
        print(f"Warning!! A file was moved in {event.src_path}!!")
event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running!!")
except KeyboardInterrupt:
    observer.stop()
    print("Stoped!!")