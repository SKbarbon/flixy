import os, requests, shutil
from urllib.parse import urljoin



class ClientTools:
    def __init__(self, host_url:str, base_path:str, passcode:str, client_class):
        self.base_path = base_path
        self.host_url = host_url
        self.passcode = passcode
        self.client_class = client_class

    def process_stream_data (self, data):
        if data["ok"] == False: return
        
        updates = data["updates"]
        for u in updates:
            path = os.path.join(self.base_path, u["path"])
            # If path created.
            if u["event_type"] == "created":
                if u["is_dir"]:
                    os.mkdir(path)
                else:
                    self.download_file(
                        url=urljoin(self.host_url, "get_content"),
                        json={
                            "path": u["path"],
                            "passcode": self.passcode
                        },
                        dist_filename=path
                    )
            
            # if modified file, download it.
            elif u["event_type"] == "modified":
                if os.path.isfile(path):
                    os.remove(path)
                self.download_file(
                        url=urljoin(self.host_url, "get_content"),
                        json={
                            "path": u["path"],
                            "passcode": self.passcode
                        },
                        dist_filename=path
                    )
            elif u["event_type"] == "deleted":
                if u["is_dir"] and os.path.isdir(path):
                    shutil.rmtree(path)
                elif not u["is_dir"] and os.path.isfile(path):
                    os.remove(path)
        
            self.client_class.rerun_main_script()
    

    def download_file(self, url, json, dist_filename):
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter below
        with requests.post(url, json=json, stream=True) as r:
            r.raise_for_status()
            with open(dist_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    f.write(chunk)
        return local_filename