from .PAGE import Page
import ui


class app (object):
	
	def __init__ (self, target):
		ThePage = Page()
		ThePage.show()
		target(ThePage)
