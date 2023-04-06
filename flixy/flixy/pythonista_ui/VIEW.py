from .tools.gestures import *
from ..Tools.action import do_action
import ui

class pythonista_ui_View (ui.View):
	
	def __init__ (self, self_class=None):
		ui.View.__init__(self)
		UIHoverGestureRecognizer = ObjCClass('UIHoverGestureRecognizer')
		handler = UIGestureRecognizerDelegate(UIHoverGestureRecognizer, self, self.hover)
		
		self.self_class = self_class
		
		self.on_touch = None
		
		self.on_mouse_hover = None
	
	def touch_began(self, touch):
		if hasattr(self.self_class, "touch_x"): self.self_class.touch_x = touch.location[0]
		if hasattr(self.self_class, "touch_y"): self.self_class.touch_y = touch.location[1]
		do_action(self.on_touch, ["start", self.self_class])
	
	def touch_moved(self, touch):
		if hasattr(self.self_class, "touch_x"): self.self_class.touch_x = touch.location[0]
		if hasattr(self.self_class, "touch_y"): self.self_class.touch_y = touch.location[1]
		do_action(self.on_touch, ["move", self.self_class])
	
	def touch_ended(self, touch):
		if hasattr(self.self_class, "touch_x"): self.self_class.touch_x = touch.location[0]
		if hasattr(self.self_class, "touch_y"): self.self_class.touch_y = touch.location[1]
		do_action(self.on_touch, ["end", self.self_class])
	
	
	def hover(self, data):
		if data.state == 1: # began
			do_action(self.on_mouse_hover, ["start", self.self_class])
		elif data.state == 2: # changed
			do_action(self.on_mouse_hover, ["change", self.self_class])
		elif data.state == 3: # ended
			do_action(self.on_mouse_hover, ["end", self.self_class])
