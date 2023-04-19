from .PAGE import Page
import ui
import dialogs
import threading
from .flixy_pyodide.setup import Setup
import os
from .update import UpdateFlixy

class app (object):
	
	def __init__ (self, target, develop=True, web_port=8000, based_file="", view="normal"):
		
		if str(view).lower() == "normal":
			ThePage = Page()
			ThePage.show()
			uf = UpdateFlixy()
			if develop:
				dialogs.hud_alert("Swipe down with two fingers to close.")
				def check():
					if uf.is_there_new_update():
						uf.run()
				threading.Thread(target=check).start()
		
			target(ThePage)
		elif str(view).lower() == "web_browser":
			if os.path.isfile(based_file) == False:
				raise FileNotFoundError("The 'based_file' argument must be a file, you can just put '__file__' with it")
			s = Setup(PORT=web_port, main_file=based_file)
			if develop:
				print("Your dist folder has been created!, Read this document for more: 'https://github.com/SKbarbon/flixy/wiki/flixy-app#web_browser-view' ..")
