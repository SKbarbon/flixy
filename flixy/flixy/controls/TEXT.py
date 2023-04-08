import ui


class Text (object):
	
	def __init__(self, value="", color="white", bgcolor=None, text_align=1, size=18, font_family="default", width=100, height=40, expand_width=False, expand_height=False
	, opacity=1.0):
		self.__self_ui = ui.Label()
		
		self.parent = None
		self.page = None
		
		self.value = value
		self.color = color
		self.bgcolor = bgcolor
		self.text_align = text_align
		self.size = size
		self.font_family = font_family
		self.x = 0
		self.width = width
		self.height = height
		self.y = 0
		self.expand_width = expand_width
		self.expand_height = expand_height
		self.opacity = opacity
		
		self.update()
	
	
	def update(self):
		l = self.__self_ui
		l.text = self.value
		l.alpha = self.opacity
		l.text_color = self.color
		l.background_color = self.bgcolor
		l.bg_color = self.bgcolor
		l.alignment = self.text_align
		
		if self.font_family == "default":
			if self.page != None:
				l.font = self.page.font_family, self.size
		else:
			l.font = self.font_family, self.size
		l.width = self.width
		l.height = self.height
		
		# set the expand
		if self.parent != None:
			if self.expand_width:
				self.__self_ui.width = self.parent.width
				self.width = self.__self_ui.width
			if self.expand_height:
				if self.page.appbar == None or self.page != self.parent:
					self.__self_ui.height = self.parent.height
					self.height = self.__self_ui.height
				else:
					self.__self_ui.height = self.parent.height - self.page.appbar.self_ui.height
					self.height = self.__self_ui.height
		
		
	
	def respown(self, parent, page):
		self.parent = parent
		self.page = page
		self.update()
	
	
	def remove_self (self):
		self.update()
		self.parent.update()
		self.parent.remove_control (self)
	
	
	
	
	@property
	def self_ui(self):
		return self.__self_ui
	
	
	
	
	
	
