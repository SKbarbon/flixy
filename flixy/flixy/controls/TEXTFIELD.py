from ..Tools.action import do_action
from ..Tools.convert_rgb_to_hex import hex_to_rgb
import ui
from objc_util import *


class TextField (object):
	
	def __init__ (self, value="", placeholder="Type..", width=300, height=50, text_color="black", bgcolor=None, border_radius=15, font_size=18, font_family="default",
	expand_width=False, expand_height=False, opacity=1.0, selectable=True, editable=True, text_align=0, autocorrection=False):
		
		self.__self_ui = ui.TextField()
		self.__tfo = ObjCInstance(self.self_ui).textField()
		self.__tfo.backgroundColor = ObjCClass('UIColor').colorWithRed_green_blue_alpha_(1.0, 1.0, 1.0, 1)
		
		self.__self_ui.delegate = textViewDelegate(self)
		
		self.parent = None
		self.page = None
		
	
		self.value = value
		self.placeholder = placeholder
		self.width = width
		self.height = height
		self.text_color = text_color
		self.bgcolor = bgcolor
		self.border_radius = border_radius
		self.font_size = font_size
		self.font_family = font_family
		self.expand_width = expand_width
		self.expand_height = expand_height
		self.opacity = 1.0
		self.selectable = selectable
		self.editable = editable
		self.text_align = text_align
		self.autocorrection = autocorrection
		
		self.last_char = ""
		
		self.x = 0
		self.y = 0
		
		# actions
		self.on_edit = None
		self.on_start_edit = None
		self.on_done_edit = None
		
		self.update()
	
	def update (self):
		tv = self.self_ui
		tv.autocorrection_type = self.autocorrection
		tv.text = self.value
		tv.placeholder = self.placeholder
		tv.width = self.width
		tv.height = self.height
		tv.text_color = self.text_color
		
		if self.bgcolor == None:
			self.__tfo.backgroundColor = ObjCClass('UIColor').colorWithRed_green_blue_alpha_(1.0, 1.0, 1.0, 0)
		elif str(self.bgcolor).startswith("#"):
			convert_to_RGB = hex_to_rgb(str(self.bgcolor))
			self.__tfo.backgroundColor = ObjCClass('UIColor').colorWithRed_green_blue_alpha_(*convert_to_RGB, 1)
		elif type(self.bgcolor) == type(list()) and len(self.bgcolor) == 3:
			self.__tfo.backgroundColor = ObjCClass('UIColor').colorWithRed_green_blue_alpha_(*self.bgcolor, 1)
		
		tv.corner_radius = self.border_radius
		if self.font_family == "default":
			if self.page != None:
				tv.font = self.page.font_family, self.font_size
		else:
			tv.font = self.font_family, self.font_size
		
		tv.alpha = self.opacity
		tv.selectable = self.selectable
		tv.editable = self.editable
		tv.alignment = self.text_align
		
		
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
	
	
	def focus (self):
		self.self_ui.begin_editing()
	
	def stop (self):
		self.self_ui.end_editing()
	
	
	@property
	def self_ui(self):
		return self.__self_ui






# delegate
class textViewDelegate (object):
	def __init__ (self, self_class):
		self.self_class = self_class
	def textfield_should_begin_editing(self, textfield):
		return True
	def textfield_did_begin_editing(self, textfield):
		do_action(self.self_class.on_start_edit, [self.self_class])
	def textfield_did_end_editing(self, textfield):
		return True
	def textfield_should_return(self, textfield):
		textfield.end_editing()
		do_action(self.self_class.on_done_edit, [self.self_class])
		return True
	def textfield_should_change(self, textfield, range, replacement):
		self.self_class.last_char = replacement
		return True
	def textfield_did_change(self, textfield):
		self.self_class.value = textfield.text
		do_action(self.self_class.on_edit, [self.self_class])
		return True


















