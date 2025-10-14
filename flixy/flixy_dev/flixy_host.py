from flask import Flask, Response, request, send_file
from .folderwatcher import FolderWatcher
import socket, random, secrets, threading
import time, os

class FlixyHost:
    def __init__(self, for_folder=None):
        self.for_folder = for_folder

        self.__obtained_with_client = False
        self.__passcode = str(secrets.token_urlsafe())

        self.stored_updates = []

        self.folder_watcher = FolderWatcher(folder_path=for_folder, callback=self.on_folder_content_change)
        threading.Thread(target=self.folder_watcher.start, daemon=True).start()
        self.app = Flask(__name__)
        self.port = self.get_random_available_port()


    def host(self):
        app = self.app
        @app.route("/get_updates", methods=["POST"])
        def get_updates():
            r = request.json
            if "passcode" in r and r["passcode"] == self.__passcode:
                updates = list(self.stored_updates)
                self.stored_updates.clear()
                return {"ok": True, "updates": updates}
            else:
                return {"ok": False}
        
        @app.route("/obtain")
        def obtain():
            if self.__obtained_with_client: return {"ok": False}
            else:
                return {
                    "ok": True,
                    "passcode": str(self.__passcode)
                }
        

        @app.route("/get_content", methods=["POST"])
        def get_content ():
            r = request.json
            if "passcode" in r and r["passcode"] == self.__passcode:
                requested_path = r['path']
                full_path = os.path.join(self.for_folder, requested_path)
                print(full_path)
                if os.path.isfile(full_path):
                    return send_file(full_path)
                else: return {"ok": False}
            else:
                return {"ok": False}

        app.run(debug=False, port=self.port, host="0.0.0.0",use_reloader=False)

    def get_random_available_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))  # Bind to port 0 to let the OS choose an available port
            return s.getsockname()[1] # Get the assigned port number

    def on_folder_content_change (self, event_type, path, is_dir):
        path = os.path.relpath(path, self.for_folder)
        update = {
            "ok": True,
            "event_type": event_type,
            "path": path,
            "is_dir": is_dir
        }
        
        self.stored_updates.append(update)