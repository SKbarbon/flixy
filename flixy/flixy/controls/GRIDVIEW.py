import ui



class GridView (object):
	
	def __init__ (self):
		self.__self_ui = ui.View()
		
		
		self.width = 250
		self.height = 250
		self.max_extent = 150
		self.controls = []
	
	
	def update (self):
		pass
	
	def reposition (self):
		mwidth = 0
		for control in self.controls:
			if mwidth >= self.width:
				pass
	
	
	@property
	def self_ui (self):
		return self.__self_ui
