from .PAGE import Page
import ui
import dialogs
import threading
from .update import UpdateFlixy


class app (object):
	
	def __init__ (self, target, develop=True):
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
