from .Tools.action import do_action
from .pythonista_ui.VIEW import pythonista_ui_View
from .controls.SHEET import Sheet
import ui
import threading
import time

class Page (object):
	def __init__ (self, run_as="app"):
		self.__ui_view = pythonista_ui_View()
		self.__ui_view.self_class = self
		
		self.controls = []
		self.bgcolor = "black"
		self.title = ""
		self.__appbar = None
		self.font_family = "Avenir"
		self.width = 0
		self.height = 0
		self.spacing = 15
		
		self.touch_x = 0
		self.touch_y = 0
		
		self.on_resize = None
		self.on_touch = None
		self.on_hover = None
		self.on_update = None
		self.on_close = None
		
		self.update()
	
	def update(self):
		v = self.__ui_view
		v.background_color = self.bgcolor
		v.name = self.title
		
		v.on_touch = self.on_touch
		v.on_mouse_hover = self.on_hover
		
		self.width = v.width
		self.height = v.height
		
		if self.__appbar != None: self.__appbar.update()
		for control in self.controls:
			control.update()
		
		self.reposition_controls()
		do_action(self.on_update, [self])
		
	
	def add (self, control):
		# start add
		control.respown(self, self)
		flixy_control = control
		control = control.self_ui
		all_heights = 0
		
		if self.appbar != None:
			all_heights = all_heights + self.appbar.self_ui.height + 25
		
		for i in self.controls:
			if isinstance(i, Sheet): pass
			else:
				all_heights = all_heights + i.height + self.spacing
		
		self.controls.append(flixy_control)
		
		control_ui_class = control
		control_ui_class.y = all_heights
		control_ui_class.x = self.width / 2 - control_ui_class.width / 2
		self.__ui_view.add_subview(control_ui_class)
		self.update()
	
	def clear (self):
		self.controls = []
		for i in self.__ui_view.subviews:
			if self.__appbar.self_ui == i: pass
			else: self.__ui_view.remove_subview(i)
	
	def show(self):
		if self.self_ui.on_screen:
			raise NameError("The page is already on screen.")
		self.__ui_view.present("fullscreen", hide_title_bar=True)
		threading.Thread(target=self.__background_thread, daemon=True).start()
	
	def close (self):
		self.__ui_view.close()
		do_action(self.on_close, [self])
		
	
	def reposition_controls(self):
		for control in self.controls:
			control_ui_class = control.self_ui
			if self.stack == "v":
				control_ui_class.x = self.width / 2 - control_ui_class.width / 2
			elif self.stack == "h":
				control_ui_class.y = self.height / 2 - control_ui_class.height / 2
	
	def remake_controls (self):
		for i in self.__ui_view.subviews:
			self.__ui_view.remove_subview(i)
		new_controls = []
		for control in self.controls:
			instance = control
			new_controls.append(instance)
		self.controls = []
		for i in new_controls:
			self.add(i)
		
		self.appbar = self.__appbar
		if self.__appbar != None: self.__appbar.update()
			
	def remove_control (self, control):
		if control not in self.controls:
			raise NameError("Cannot found this control to remove.")
		self.controls.remove(control)
		self.remake_controls()
	
	
	
	@property
	def appbar (self):
		return self.__appbar
	
	@appbar.setter
	def appbar(self, new_appbar):
		if new_appbar == None:
			self.__appbar = None
			return
		self.__appbar = new_appbar
		new_appbar.page = self
		self.self_ui.add_subview(new_appbar.self_ui)
	
	
	# propertys
	@property
	def stack(self):
		return "v"
	
	@property
	def self_ui (self):
		return self.__ui_view
	
	def on_screen (self):
		self.__ui_view.on_screen
	
	def __background_thread(self):
		last_size = [self.width, self.height]
		v = self.__ui_view
		while v.on_screen:
			if [v.width, v.height] != last_size:
				self.width = v.width
				self.height = v.height
				last_size = [self.width, self.height]
				do_action(self.on_resize, [self])
				self.update()
		do_action(self.on_close, [self])
		
		
		
		
		
		
	
	
	
	
	
	
	
	
