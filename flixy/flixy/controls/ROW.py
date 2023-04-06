import ui
from ..Tools.action import do_action



class Row (object):
	
	def __init__ (self, controls=[], scroll=True, auto_end_following = False, width = 200, height = 75, bgcolor = None, expand_width = False, expand_height = False,
	border_radius = 8, spacing=5, on_scroll=None):
		
		
		class TheDelegate (object):
			def __init__(self, self_class_function):
				self.self_class_function = self_class_function
			def scrollview_did_scroll(self, scroll_view):
				self.self_class_function()
			
		
		self.parent = None
		self.page = None
		
		self.__self_ui = ui.ScrollView()
		self.__self_ui.directional_lock_enabled = True
		self.__self_ui.shows_vertical_scroll_indicator = False
		self.__self_ui.delegate = TheDelegate(self.__on_scroll)
		self.controls = controls
		self.scroll = scroll
		self.auto_end_following = auto_end_following
		self.width = width
		self.height = height
		self.bgcolor = bgcolor
		self.expand_width = expand_width
		self.expand_height = expand_height
		self.border_radius = border_radius
		self.spacing = spacing
		
		self.__offset_x = 0
		self.__offset_y = 0
		self.on_scroll = on_scroll
		
		self.update()
	
	def update(self):
		v = self.__self_ui
		
		v.scroll_enabled = self.scroll
		v.width = self.width
		v.height = self.height
		v.bg_color = self.bgcolor
		v.corner_radius = self.border_radius
		
		# to set the expand
		if self.parent != None:
			if self.expand_width:
				self.__self_ui.width = self.parent.width
				self.width = self.__self_ui.width
			if self.expand_height:
				self.__self_ui.height = self.parent.height
				self.height = self.__self_ui.height
		
		# update sub controls
		for i in self.controls:
			i.update()
		self.reposition_controls()
		# update the scroll
		max_width = 0
		for i in self.controls:
			max_width = max_width + i.width + self.spacing
		
		self.self_ui.content_size = max_width, 0
		self.self_ui.content_offset = self.self_ui.content_offset[0], 0
	
	def add (self, control):
		if self.page == None:
			raise NameError("Cannot add sub-control while self is not on screen.")
		control.respown(self, self.page)
		flixy_control = control
		control = control.self_ui
		all_widths = 0
		
		for i in self.controls:
			all_widths = all_widths + i.width + self.spacing
		
		self.controls.append(flixy_control)
		control_ui_class = control
		control_ui_class.y = self.height / 2 - control_ui_class.height / 2
		control_ui_class.x = all_widths
		self.self_ui.add_subview(control_ui_class)
		self.update()
		
		if self.auto_end_following:
			ui.animate(self.__follow_the_end, 0.3)
			self.update()
	
	def respown (self, parent, page):
		self.parent = parent
		self.page = page
	
	def remove_self (self):
		pass
	
	def clear (self):
		self.controls = []
		for i in self.self_ui.subviews:
			self.self_ui.remove_subview(i)
		self.update()
	
	def reposition_controls (self):
		for control in self.controls:
			control_ui_class = control.self_ui
			if self.stack == "v":
				control_ui_class.x = self.width / 2 - control_ui_class.width / 2
			elif self.stack == "h":
				control_ui_class.y = self.height / 2 - control_ui_class.height / 2
	
	def remake_controls (self):
		for i in self.self_ui.subviews:
			self.self_ui.remove_subview(i)
		new_controls = []
		for control in self.controls:
			instance = control
			new_controls.append(instance)
		self.controls = []
		for i in new_controls:
			self.add(i)
	
	def remove_control (self, control):
		if control not in self.controls:
			raise NameError("Cannot found this control to remove.")
		self.controls.remove(control)
		self.remake_controls()
	
	# actions
	def __on_scroll (self):
		self.self_ui.content_offset = self.self_ui.content_offset[0], 0
		self.__offset_x = self.self_ui.content_offset[0]
		self.__offset_y = self.self_ui.content_offset[1]
		do_action(self.on_scroll, [self])
	
	def __follow_the_end (self):
		self.self_ui.content_offset = self.self_ui.content_size[0], 0
	
	
	@property
	def self_ui (self):
		return self.__self_ui
	
	@property
	def stack (self):
		return "h"
	
	
	@property
	def on_screen (self):
		return self.self_ui.on_screen
	
	@property
	def offset (self):
		return [self.__offset_x, self.__offset_y]
	
	
	
	
	
	
	
	
	
	
