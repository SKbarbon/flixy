from .PAGE import Page
import ui
import threading
from .update import update_flixy


class app (object):
	
	def __init__ (self, target, develop=True):
		ThePage = Page()
		ThePage.show()
		
		uf = update_flixy()
		if develop:
			def check():
				if uf.is_there_new_update():
					uf.run()
		threading.Thread(target=check).start()
		
		target(ThePage)
