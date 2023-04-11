import ui
from ..Tools.expander import expand_control
from ..Tools.action import do_action



class Switch (object):
	
	def __init__ (self, value=False, active_color="#76a6ff", disabled=False, on_change=None, expand_width=False, expand_height=False, opacity=1.0, width=100, height=100):
		self.__self_ui = ui.Switch()
		self.__self_ui.action = self.__on_change_value
		
		self.page = None
		self.parent = None
		
		self.value = value
		self.active_color = active_color
		self.disabled = disabled
		self.expand_width = expand_width
		self.expand_height = expand_height
		self.opacity = opacity
		self.width = width
		self.height = height
		# actions
		self.on_change = on_change
		
		self.update()
	
	def update(self):
		s = self.self_ui
		
		s.value = self.value
		s.tint_color = self.active_color
		s.enabled = self.disabled == False
		s.alpha = self.opacity
		s.width = self.width
		self.height = self.height
		
		expand_control(self)
		
		
	def respown(self, parent, page):
		self.parent = parent
		self.page = page
		self.update()
	
	
	def remove_self (self):
		self.update()
		self.parent.update()
		self.parent.remove_control (self)
	
	def get_percentage (self):
		return float(self.value) / 1.0 * 100
	
	def __on_change_value (self, cls):
		self.value = cls.value
		do_action(self.on_change, [self])
		
	
	
	@property
	def self_ui(self):
		return self.__self_ui
