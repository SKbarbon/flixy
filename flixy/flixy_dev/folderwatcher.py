from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class FolderWatcher:
    """
    A simple folder watcher using watchdog.
    
    Example:
        def on_change(event_type, path):
            print(event_type, path)
        
        watcher = FolderWatcher("my_folder", on_change)
        watcher.start()
    """
    
    def __init__(self, folder_path, callback, recursive=True):
        """
        :param folder_path: Path to watch
        :param callback: Function with signature callback(event_type, path)
        :param recursive: Whether to watch subfolders
        """
        self.folder_path = folder_path
        self.callback = callback
        self.recursive = recursive
        self.observer = Observer()

        # Custom handler that calls your callback
        class _Handler(FileSystemEventHandler):
            def on_created(_, event):
                callback("created", event.src_path, event.is_directory)

            def on_modified(_, event):
                if not event.is_directory:
                    callback("modified", event.src_path, event.is_directory)

            def on_deleted(_, event):
                    callback("deleted", event.src_path, event.is_directory)

        self.handler = _Handler()

    def start(self):
        self.observer.schedule(self.handler, self.folder_path, recursive=self.recursive)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

    def watch_forever(self, interval=1):
        """Blocking loop until Ctrl+C"""
        try:
            self.start()
            while True:
                time.sleep(interval)
        except KeyboardInterrupt:
            self.stop()
