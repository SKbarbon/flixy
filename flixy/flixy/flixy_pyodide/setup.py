import os
import shutil
import tarfile
import threading
import time
import zipfile
import webbrowser
import sys

class Setup (object):
	
	def __init__ (self, PORT, main_file):
		self.PORT = PORT
		self.main_file = main_file
		self.setup_files()
		try: self.run_server()
		except Exception as e: print(f"Host error:\n{e}\n--------\nTry changing the PORT on flixy.app(web_port=<new port>)")
	
	
	def setup_files (self):
		dist_template_path = str(__file__).replace("/setup.py", "")
		dist_template_path = f"{dist_template_path}/dist/"
		
		#! step1: Remove the last dist
		if os.path.isdir("dist"):
			#? if the folder does exist, remove it.
			shutil.rmtree("dist")
		
		#? Copy the template dist folder into the current user path.
		shutil.copytree(dist_template_path, "dist")
		
		#! step2: edit the tar.gz file to include the files.
		#! There is a folder called `app`
		#? Remove the Previous `app.tar.gz` file.
		os.remove("dist/app.tar.gz")
		
		#? unzip app.zip file
		with zipfile.ZipFile("dist/app.zip", "r") as zip_ref:
			zip_ref.extractall("dist/app")
		
		shutil.copytree("dist/app/app", "dist/_app")
		shutil.rmtree("dist/app")
		shutil.move("dist/_app", "dist/app")
		os.remove("dist/app.zip")
		
		#! step3: Bring all current files on current dir to "app" folder
		main_file_content = open(self.main_file, encoding="utf-8").read()
		open("dist/app/main.py", "w+", encoding="utf-8").write(main_file_content)
		self.get_all_dir_to_app()

		#! Pack the `app` folder into a new `app.tar.gz` file.
		out_put = "dist/app.tar.gz"
		source_put = "dist/app"
		import tarfile
		with tarfile.open(out_put, "w:gz") as tar:
			for fn in os.listdir(source_put):
				p = os.path.join(source_put, fn)
				tar.add(p, arcname=fn)
		
		#! Remove the `app` folder.
		shutil.rmtree("dist/app")
		
		
	def get_all_dir_to_app (self):
		"""
This must bring all development dir to app.tar.gz
		"""
		for file in os.listdir("."):
			if os.path.isfile(file):
				shutil.copyfile(file, f"dist/app/{file}")
			elif os.path.isdir(file):
				if file == "dist": pass
				elif file == "flixy": pass
				else: shutil.copytree(file, f"dist/app/{file}")
	
	def run_on_webview (self):
		time.sleep(1.5)
		webbrowser.open(f"safari-http://localhost:{self.PORT}/dist")
	
	def run_server (self):
		import http.server
		import socketserver
		import threading
		import webbrowser
		import time
		import random
		
		PORT = self.PORT # Change this to the desired port number
		
		class MyHandler(http.server.SimpleHTTPRequestHandler):
			def log_message(self, format, *args):
				pass
		
		with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
			threading.Thread(target=self.run_on_webview, daemon=True).start()
			httpd.serve_forever()
