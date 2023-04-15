from ..Tools.sounds import Sound




class Audio (object):
	def __init__ (self, src="8ve:8ve-beep-bop"):
		self.__self = Sound(src)
		self.__src = src
		self.page = None
		
		# actions
		self.on_duration_changed = None
		
	def play(self):
		if self.page == None:
			raise OSError("There must be a page.")
		self.__self.play()
	
	def pause (self):
		self.__self.pause()
	
	def current_time(self):
		return self.__self.current_time()
		
	def respown (self, page):
		self.page = page
	
	def get_full_time (self):
		return self.__self.get_full_time()
