import ui
import threading
import random
import sys
import time
import sound
import shutil
import os



v = ui.View()
v.bg_color = "white"
if ui.get_window_size()[0] > 770:
	v.width = 790
	v.height = 590
	v.present("sheet", hide_title_bar=True)
else:
	v.present("fullscreen", hide_title_bar=True)


def loop_animations (view):
	def random_moves (ball):
		ball.alpha = 1.0
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

threading.Thread(target=loop_animations, args=[v], daemon=True).start()
up_coverv = ui.View(bg_color=v.bg_color, alpha=1.0)
up_coverv.width = v.width
up_coverv.height = v.height
v.add_subview(up_coverv)
up_coverv.bring_to_front()



def set_cover():
	up_coverv.alpha = 0.5
ui.animate(set_cover, 0.2)



Title = ui.Label(text="", text_color="black", font=('Avenir', 50), width=v.width)
if v.width < 400:
	# if iPhone
	Title.font = 'Avenir', 30
	Title.width = v.width
	Title.alignment = 1
	Title.center = (v.width * 0.5, v.height * 0.3)
else:
	Title.x = v.width / 12
	Title.y = v.height / 5
v.add_subview(Title)

Describe = ui.TextView(text="", text_color="#9f9f9f")
Describe.font = 'Avenir', 17
Describe.editable = False
Describe.background_color = None
Describe.selectable = False
Describe.width = v.width - 28
if v.width < 400:
	# if iPhone
	Describe.height = 120
	Describe.width = v.width - 60
	Describe.center = (v.width * 0.5, v.height * 0.43)
else:
	Describe.x = v.width / 12
	Describe.y = v.height / 3
v.add_subview(Describe)


context_view = ui.View() # the place which every actions will be in.
context_view.width = v.width / 2
context_view.height = v.height - (Describe.y + Describe.height)
context_view.bg_color = None
v.add_subview(context_view)
if v.width < 400:
	context_view.width = v.width
	context_view.height = v.height - (Describe.y + Describe.height + 15)
	context_view.center = (v.width * 0.5, v.height * 0.8)
else:
	context_view.center = (v.width * 0.5, v.height * 0.7)

def set_context (view):
	def anim():
		for i in context_view.subviews:
			context_view.remove_subview(i)
		
		view.alpha = 0.0
		context_view.add_subview(view)
		time.sleep(0.2)
		view.alpha = 1.0
	ui.animate(anim, 0.4)


def set_title_and_describe (t, d):
	def anim():
		Title.alpha = 0.0
		Describe.alpha = 0.0
	def anim2():
		Title.text = t
		Describe.text = d
		Title.alpha = 1.0
		Describe.alpha = 1.0
	threading.Thread(target=ui.animate, args=[anim, 0.3], daemon=True).start()
	time.sleep(1)
	threading.Thread(target=ui.animate, args=[anim2, 0.5], daemon=True).start()


time.sleep(1)
set_title_and_describe("Let's imagine a new UI.", "flixy is a pythonista UI library that allow\nyou to create powerful UI that support new cases.")




Download_btn = ui.Button(title="Download flixy", width=250, height=70)
Download_btn.bg_color = 'black'
Download_btn.width = 250; Download_btn.height = 45
Download_btn.corner_radius = 10
Download_btn.tint_color = "white"
Download_btn.font = 'Avenir', 18
set_context(Download_btn)
Download_btn.center = (context_view.width * 0.5, context_view.height * 0.5)


def SetTemplates():
	import requests
	import os
	# Get the home directory
	home_dir = os.path.expanduser("~")
	
	# Create the path to the Documents folder
	documents_folder = os.path.join(home_dir, "Documents")
	
	# Get the path of site-packages
	Templates_folder = os.path.join(documents_folder, "Templates")
	
	script = """
from flixy import *
import flixy
import random

def main (page:flixy.Page):
	def on_name_edit (textfield):
		name = textfield.value
		random_emoji = ["🤠", "🙂", "😃", "😄", "😇"]
		greeting_text.value = f"Hello {name} {random.choice(random_emoji)}"
		greeting_text.update()
	greeting_text = flixy.Text("Type your name.", expand_width=True, height=50, size=30)
	page.add(Text(""))
	page.add(greeting_text)
	name_input = flixy.TextField(placeholder="Your name..", bgcolor="#ffffff")
	name_input.on_edit = on_name_edit
	page.add(name_input)

flixy.app(target=main)

# To read the docs and learn about flixy, type: `flixy.learn_flixy()`
# To hide the `swipe down with two fingers` alert, and to stop checking for library updates on background, type: `flixy.app(target=main, develop=False)`.
	"""
	open(f"{Templates_folder}/flixy ui.py", "w+", encoding="utf-8").write(script)


def save_into_site_package():
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


def start_install (cls):
	cls.enabled = False
	# this function is for install the .zip file
	def do_in_thread():
		set_title_and_describe("Getting data..", "We are getting library data to start install..")
		import requests
		# Define the URL to send the HEAD request to
		url = 'https://raw.githubusercontent.com/SKbarbon/flixy/main/flixy.zip'
		
		# Send an HTTP HEAD request and get the response
		response = requests.head(url)
		
		# Check the status code of the response
		if response.status_code == 200:
			set_title_and_describe("Data collected!", "The data of the library has been found!, installing will be started soon.")
			full_size = int(int(response.headers['Content-Length'])/1000)
		else:
			set_title_and_describe("Cannot found 😵!", "Cannot found the zip file of the library!!")
			return 
		
		time.sleep(1)
		set_title_and_describe("Downloading..", "The file is being Downloading.")
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
		
		set_title_and_describe("Saving..", "Saving the file into the site-package.")
		save_into_site_package()
		SetTemplates()
		set_title_and_describe("Done 🤠!", "The library has been downloaded and saved!, now lets restart the app!")
		
		def restart(cls):
			os._exit(0)
		
		restart_btn = ui.Button(title="Restart pythonista")
		restart_btn.bg_color = 'black'
		restart.action = restart
		restart_btn.width = 280; restart_btn.height = 40
		restart_btn.corner_radius = 10
		restart_btn.tint_color = "white"
		restart_btn.font = 'Avenir', 18
		restart_btn.action = restart
		set_context(restart_btn)
		restart_btn.center = (context_view.width * 0.5, context_view.height * 0.5)
		
		
		
		
	threading.Thread(target=do_in_thread, daemon=True).start()
	


Download_btn.action = start_install









