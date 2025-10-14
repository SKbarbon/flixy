from urllib.parse import urljoin
import requests, json, traceback, time
from .client_tools import ClientTools
from .thread_tools import stop_thread
import os, threading, importlib
import importlib.util, sys, traceback, os



class FlixyClient:
    def __init__(self, flixy_host_url, base_path:str):
        self.flixy_host_url = flixy_host_url
        self.base_path = base_path

        self.host_passcode = False
        
        self._stay_connected = False

        self.current_script_thread = None
    

    def connect (self):
        self.rerun_main_script()
        try:
            obtain_url = urljoin(self.flixy_host_url, "obtain")
            respone = json.loads(requests.get(obtain_url).text)
            if respone["ok"] == False: return
        except:
            traceback.print_exc()
            return
        
        self.host_passcode = respone['passcode']
        self.join_host_stream()
    
    def join_host_stream(self):
        stream_url = urljoin(self.flixy_host_url, "get_updates")
        
        self._stay_connected = True
        while self._stay_connected:
            resp = requests.post(
                url=stream_url,
                json={
                    "passcode": self.host_passcode
                }
            )
            try:
                ClientTools(
                    host_url=self.flixy_host_url,
                    base_path=self.base_path,
                    passcode=self.host_passcode,
                    client_class=self
                ).process_stream_data(json.loads(resp.text))
            except:
                traceback.print_exc()
            time.sleep(1)
    

    def close (self):
        self._stay_connected = False
    


    def rerun_main_script(self):
        """If main.py exists, it will rerun it freshly in a new thread."""
        def try_run():
            main_script = os.path.join(self.base_path, "main.py")
            if not os.path.isfile(main_script):
                print(f"main.py not found at {main_script}.")
                return

            base_name = os.path.basename(self.base_path)
            module_prefix = f"{base_name}."

            # Remove cached modules inside this package so edits are reflected
            for name in list(sys.modules.keys()):
                if name.startswith(module_prefix):
                    del sys.modules[name]

            parent_dir = os.path.dirname(self.base_path)
            if parent_dir not in sys.path:
                sys.path.insert(0, parent_dir)

            try:
                module_name = f"{base_name}.main"
                spec = importlib.util.spec_from_file_location(module_name, main_script)
                mod = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = mod
                spec.loader.exec_module(mod)

            except SystemExit:
                # Thread killed intentionally — ignore
                pass
            except Exception:
                print("Error while running main.py in a new thread:")
                traceback.print_exc()
            finally:
                if parent_dir in sys.path:
                    sys.path.remove(parent_dir)

        # stop previous thread if it exists
        if self.current_script_thread is not None:
            stop_thread(self.current_script_thread)

        self.current_script_thread = threading.Thread(target=try_run)
        self.current_script_thread.start()