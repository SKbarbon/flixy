import ui
from ..pythonista_ui.VIEW import pythonista_ui_View
from ..Tools.action import do_action


class Button (object):
	
	def __init__ (self, title="", bgcolor="#4082ff", title_color="white", bgcolor_after_hover="#80acff", on_click=None, width=250, height=50, border_radius=15
	, font_size=16, font_family='default', opacity=1.0, expand_width=False, expand_height=False):
		self.__self_ui = pythonista_ui_View()
		self.__self_ui.self_class = self
		self.__self_ui.on_mouse_hover = self.__on_hover
		self.__self_ui.on_touch = self.__on_click
		
		self.__title_view = ui.Label(text=title, alignment=1)
		self.__self_ui.add_subview(self.__title_view)
		self.__title_view.center = (self.__self_ui.width * 0.5, self.__self_ui.height * 0.5)
		
		self.page = None
		self.parent = None
		
		self.title = title
		self.bgcolor = bgcolor
		self.title_color = title_color
		self.bgcolor_after_hover = bgcolor_after_hover
		self.width = width
		self.height = height
		self.on_click = on_click
		self.border_radius = border_radius
		self.font_size = font_size
		self.font_family = font_family
		self.opacity = opacity
		self.expand_width = expand_width
		self.expand_height = expand_height
		self.update()
	
	def update(self):
		v = self.self_ui
		t = self.__title_view
		
		v.background_color = self.bgcolor
		v.corner_radius = self.border_radius
		v.width = self.width
		v.height = self.height
		v.alpha = self.opacity
		
		t.text = self.title
		t.text_color = self.title_color
		if self.font_family == "default":
			if self.page != None:
				t.font = self.page.font_family, self.font_size
		else:
			t.font = self.font_family, self.font_size
		t.width = v.width
		t.height = v.height
		
		if self.parent != None:
			if self.expand_width:
				self.__self_ui.width = self.parent.width
				self.width = self.__self_ui.width
			if self.expand_height:
				self.__self_ui.height = self.parent.height
				self.height = self.__self_ui.height
		
		self.__title_view.center = (self.__self_ui.width * 0.5, self.__self_ui.height * 0.5)
	
	def respown (self, parent, page):
		self.parent = parent
		self.page = page
	
	def remove_self (self):
		self.update()
		self.parent.update()
		self.parent.remove_control (self)
		
	
	
	def __on_hover(self, state, cls):
		def change():
			if state == "start" or state == "change":
				self.self_ui.background_color = self.bgcolor_after_hover
			else:
				self.self_ui.background_color = self.bgcolor
		ui.animate(change, duration=0.3)
	
	
	def __on_click(self, state, cls):
		def change():
			if state == "start" or state == "move":
				self.self_ui.alpha = 0.65
			else:
				self.self_ui.alpha = self.opacity
				do_action(self.on_click, [self])
		ui.animate(change, duration=0.15)
	
	@property
	def self_ui(self):
		return self.__self_ui














