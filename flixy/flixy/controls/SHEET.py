from .COLUMN import Column
from ..Tools.action import do_action
import ui
import time


class Sheet (object):
	
	def __init__ (self, bgcolor="white", border_radius=12, show=True, on_hide=None):
		self.__self_ui = ui.View(alpha=0.0)
		self.__background_hider = ui.Button(bg_color="#474747", alpha=0.0, action=self.__custom_hide)
		
		self.page = None
		self.spacing = 10
		self.controls = []
		self.bgcolor = bgcolor
		self.border_radius = border_radius
		
		# actions
		self.on_hide = on_hide
		
		self.update()
		
		if show:
			self.show()
	
	def update (self):
		v = self.self_ui
		bg_btn = self.__background_hider
		
		v.background_color = self.bgcolor
		v.corner_radius = self.border_radius
		
		if self.page == None: return
		
		if v.superview != None:
			if bg_btn not in v.superview.subviews:
				v.superview.add_subview(bg_btn)
		bg_btn.width = self.page.width
		bg_btn.height = self.page.height
		bg_btn.bring_to_front()
		v.bring_to_front()
		
		
		if self.page.width < 675:
			# if iPhone
			v.width = self.page.width - 35
			v.height = self.page.height - 70
		elif self.page.height < 675:
			v.width = self.page.width / 2
			v.height = self.page.height - 35
		else:
			# if iPad & mac
			v.width = self.page.width / 2
			v.height = self.page.height / 2
		
		v.center = (self.page.width * 0.5, self.page.height * 0.5)
		
		for control in self.controls:
			control.update()
		
		self.reposition_controls()
	
	def add (self, *new_controls):
		if self.page == None:
			raise NameError("Cannot add sub-control while self is not on screen.")
		for control in new_controls:
			control.respown(self, self.page)
			flixy_control = control
			control = control.self_ui
			all_height = 0
			
			for i in self.controls:
				all_height = all_height + i.height + self.spacing
			
			self.controls.append(flixy_control)
			control_ui_class = control
			control_ui_class.y = all_height
			control_ui_class.x = self.width / 2 - control_ui_class.width / 2
			self.self_ui.add_subview(control_ui_class)
			self.update()
		
	
	def show (self, *args):
		self.self_ui.hidden = False
		def anim():
			self.__background_hider.alpha = 0.3
			self.self_ui.alpha = 1.0
		ui.animate(anim, 0.4)
	
	def hide (self, *args):
		def anim():
			self.__background_hider.alpha = 0.0
			self.self_ui.alpha = 0.0
		ui.animate(anim, 0.4)
		do_action(self.on_hide, [self])
		
		time.sleep(0.5)
		self.self_ui.hidden = True
	
	def __custom_hide (self, *args):
		do_action(self.hide, [])
	
	def respown(self, parent, page):
		self.page = page
		self.update()
	
	
	def remove_self (self):
		self.update()
		self.page.update()
		self.page.remove_control (self)
	
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
	
	@property
	def self_ui(self):
		return self.__self_ui
	
	@property
	def height (self):
		return self.self_ui.height
	
	@property
	def width (self):
		return self.self_ui.width
	
	@property
	def stack (self):
		return "v"
	

