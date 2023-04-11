from ..Tools.action import do_action
from ..Tools.expander import expand_control
import ui


class Slider (object):
	"""
	"""
	def __init__ (self, value=0.3, active_color="white", on_change=None, max_value=1.0, min_value=0.0, expand_width=False, expand_height=False, opacity=1.0, width=150, height=50):
		self.__self_ui = ui.Slider()
		self.self_ui.action = self.__on_change_value
		self.self_ui.continuous = True
		
		self.page = None
		self.parent = None
		
		self.value = value
		self.active_color = active_color
		self.max_value = max_value
		self.min_value = min_value
		self.expand_width = expand_width
		self.expand_height = expand_height
		self.opacity = opacity
		self.width = 150
		self.height = 50
		
		# actions
		self.on_change = on_change
		
		self.update()
	
	
	def update(self):
		s = self.self_ui
		s.value = self.value
		s.alpha = self.opacity
		
		# expand set
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
		if self.self_ui.value > self.max_value:
			self.self_ui.value = self.max_value
		if self.self_ui.value < self.min_value:
			self.self_ui.value = self.min_value
		
		self.value = cls.value
		do_action(self.on_change, [self])
		
	
	
	@property
	def self_ui(self):
		return self.__self_ui
