import ui
import os
import sys
import shutil
import sys
import random
import sound
import time
import threading
import requests
import json


version = "1.4"

class update_flixy (object):
	def __init__ (self, auto_run=True):
		v = ui.View(bg_color="white")
		v.bring_to_front()
		self.v = v
		
	
	def background_animation (self):
		v = self.v
		def random_moves (ball):
			ball.alpha = 0.7
			random_size = random.choice(range(80))
			random_pos = [random.choice(range(-1, int(v.width))), random.choice(range(-1, int(v.height)))]
			ball.width = random_size
			ball.height = random_size
			ball.corner_radius = random_size / 2
			ball.x, ball.y = random_pos
			
		all_balls = []
		for i in range(80):
			colors = ["#ff8989", '#ffddb9', '#ffeca7', '#e2ff9e', '#afff9e', '#c1c7ff', '#ffb9cb']
			color = random.choice(colors)
			ball = ui.View(bg_color=color, width=30, height=30, corner_radius=15, alpha=0.0)
			ball.send_to_back()
			ball.center = (v.width * 0.5, v.height * 0.5)
			all_balls.append(ball)
			v.add_subview(ball)
			
		
		for i in all_balls:
			i.send_to_back()
		
		while v.on_screen:
			sounds = ['piano:D4#', 'piano:F4#', 'piano:F4', 'piano:G3#', 'piano:C4#', 'piano:A3', 'piano:C4', 'piano:B3', 'piano:E3', 'piano:F3#']
			sound.set_volume(0.1)
			sound.play_effect(random.choice(sounds))
			sound.play_effect(random.choice(sounds))
			for i in all_balls:
				def do():
					random_moves(i)
				ui.animate(do, 4.0)
			time.sleep(2.5)
		sys.exit()
	
	def update_site_packages (self, btn):
		btn.enabled = False
		url = 'https://raw.githubusercontent.com/SKbarbon/flixy/main/flixy.zip'
		
		# Send a request to the URL to download the file
		response = requests.get(url, stream=True)
		
		# Get the total size of the file from the Content-Length header
		total_size = int(response.headers.get('content-length', 0))
		
		# Save the downloaded file to a local file
		with open('flixy.zip', 'wb') as file:
			downloaded_size = 0
			for chunk in response.iter_content(1024):
				file.write(chunk)
				downloaded_size += len(chunk)
		
		import zipfile
		import os
		
		# Specify the path to the downloaded ZIP file
		zip_file_path = 'flixy.zip'
		
		# Specify the path where the extracted folder should be saved
		extracted_folder_path = '__folder'
		
		# Open the ZIP file
		with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
			# Extract all files to the specified folder path
			zip_ref.extractall(extracted_folder_path)
		
		# Get the home directory
		home_dir = os.path.expanduser("~")
		
		# Create the path to the Documents folder
		documents_folder = os.path.join(home_dir, "Documents")
		
		# Get the path of site-packages
		site_packages = os.path.join(documents_folder, "site-packages", "flixy")
		
		# Remove the destination folder if it exists
		if os.path.exists(site_packages):
		    shutil.rmtree(site_packages)
		
		# Move the source folder to the destination folder
		shutil.move(f"{extracted_folder_path}/flixy", site_packages)
		
		# to clear every thing
		os.remove(zip_file_path)
		shutil.rmtree("__folder")
		
		self.v.close()
		print(f"Flixy library is updated!\nWhats new?:\n{self.library_news()}")
	
	def update_context (self, view):
		v = self.v
		view.alpha = 0.0
		v.add_subview(view)
		view.bring_to_front()
		time.sleep(0.1)
		def anim():
			view.alpha = 1.0
		ui.animate(anim, 0.4)
	
	def run(self):
		v = self.v
		v.bring_to_front()
		if ui.get_window_size()[0] > 770:
			v.width = 790
			v.height = 590
			v.present("sheet", hide_title_bar=True)
		else:
			v.present("fullscreen", hide_title_bar=True)
		
		threading.Thread(target=self.background_animation, daemon=True).start()
		
		vv = ui.View(width=self.v.width, height=self.v.height)
		vv.bounds = v.bounds
		if self.is_there_new_update():
			title = ui.Label(text="There is a new update!", text_color="black", alignment=1, font=('Avenir', 30), width=vv.width)
			install_button = ui.Button(title="Download now", width=290, height=60, corner_radius=10, bg_color="black", tint_color="white", font=('Avenir', 17))
			install_button.width = 290
			install_button.action = self.update_site_packages
			news = ui.TextView(text=f"Whats new ?:\n{self.library_news()}", width=install_button.width, height=150, font=('Avenir', 18), bg_color=None)
			news.editable = False
			news.selectable = False
			vv.add_subview(title)
			vv.add_subview(install_button)
			vv.add_subview(news)
			title.center = (vv.width * 0.5, vv.height * 0.45)
			install_button.center = (vv.width * 0.5, vv.height * 0.53)
			news.height = vv.height-(install_button.y+install_button.height)
			news.y = vv.height - news.height
			news.x = vv.width / 2 - news.width / 2
			self.update_context(vv)
		else:
			no_update = ui.Label(text="flixy is up to date!", font=('Avenir', 30), text_color="black", alignment=1)
			version_label = ui.Label(text=f"{version}", font=('Avenir', 18), alignment=1)
			no_update.width = vv.width
			version_label.width = vv.width
			vv.add_subview(no_update)
			vv.add_subview(version_label)
			
			no_update.center = (vv.width * 0.5, vv.height * 0.45)
			version_label.center = (vv.width * 0.5, vv.height * 0.55)
			
			self.update_context(vv)
	
	def library_news (self):
		url = "https://raw.githubusercontent.com/SKbarbon/flixy/main/info.json"
		data = requests.get(url).text
		return str(json.loads(data)["news"])
	
	def is_there_new_update (self):
		url = "https://raw.githubusercontent.com/SKbarbon/flixy/main/info.json"
		data = requests.get(url).text
		if json.loads(data)["version"] == version:
			return False
		else:
			return True


if __name__ == "__main__":
	a = update_flixy().run()
