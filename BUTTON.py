import ui
import threading





class Button (object):
	__MotherView = None
	__MotherClass = None
	__SelfView = None
	
	# propertys
	text = ""
	textcolor = "#9bbeff"
	bgcolor = None
	width = 150
	height = 50
	border_radius = 0
	font_family = 'Avenir Next'
	font_size = 24
	hide = False
	opacity = 1.0
	y = 0
	x = 0
	# actions
	on_click = None
	
	def __init__(self, text="", textcolor="#9bbeff", width=150, height=50, border_radius=0, font_family="Avenir Next", font_size = 24, hide=False, opacity=1.0, bgcolor=None, y=0, x=0, on_click=None):
		self.__SelfView = ui.Button()
		self.__MotherClass = None
		self.__MotherView = None
		self.text = text
		self.textcolor = textcolor
		self.width = width
		self.height = height
		self.border_radius = border_radius
		self.font_family = font_family
		self.font_size = font_size
		self.hide = hide
		self.opacity = opacity
		self.bgcolor = bgcolor
		self.y = y
		self.x = x
		self.on_click = on_click
		self.parent = None
		self.update()
	
	def update(self):
		bb = self
		def ACTION(self):
			if bb.on_click != None:
				threading.Thread(target=bb.on_click, args=[bb]).start()
		
		b = self.__SelfView
		b.action = ACTION
		b.title = self.text
		b.background_color = self.bgcolor
		b.tint_color = self.textcolor
		b.width = self.width
		b.height = self.height
		b.corner_radius = self.border_radius
		b.font = self.font_family, self.font_size
		b.hidden = self.hide
		b.alpha = self.opacity
		self.parent = self.__MotherClass
		
		if b.on_screen == False: return
		
		if self.__MotherClass.stack == "v":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.y = self.y
		elif self.__MotherClass.stack == "h":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.x = self.x
		elif self.__MotherClass.stack == "z":
			self.__SelfView.x = self.x
			self.__SelfView.y = self.y
	
	
	def Respown(self, ParentView, stack, ParentClass):
		self.__MotherView = ParentView
		self.__MotherClass = ParentClass
		
		if str(stack).lower() == "v":
			Last_y = 0
			LastHeight = 0
			for i in ParentView.subviews:
				if i.y > Last_y: Last_y = i.y
				LastHeight = i.height
			self.__SelfView.center = (ParentView.width * 0.5, ParentView.height * 0.5)
			if list(ParentView.subviews) == []: self.__SelfView.y = ParentClass.controls_padding
			else: self.__SelfView.y = Last_y + ParentClass.controls_padding + LastHeight
			self.__MotherView.add_subview(self.__SelfView)
			self.x = self.__SelfView.x; self.y = self.__SelfView.y
			
			if ParentClass.OverFill == "scroll":
				ParentView.content_size = ParentView.width, int(Last_y + LastHeight + self.height + ParentClass.controls_padding * 2)
			elif ParentClass.OverFill == "scale" and ParentView.height < int(Last_y + LastHeight + self.height + ParentClass.controls_padding * 2):
				def Animate():
					ParentView.height = int(Last_y + LastHeight + self.height + ParentClass.controls_padding * 2)
				ui.animate(Animate, 0.5)
				
		elif str(stack).lower() == "h":
			Last_x = 0
			LastWidth = 0
			for i in ParentView.subviews:
				if i.x > Last_x: Last_x = i.x
				LastWidth = i.width
			self.__SelfView.center = (ParentView.width * 0.5, ParentView.height * 0.5)
			if list(ParentView.subviews) == []: self.__SelfView.x = ParentClass.controls_padding
			else: self.__SelfView.x = Last_x + ParentClass.controls_padding + LastWidth
			self.__MotherView.add_subview(self.__SelfView)
			self.x = self.__SelfView.x; self.y = self.__SelfView.y
			
			if ParentClass.OverFill == "scroll":
				ParentView.content_size = int(Last_x + LastWidth + self.width + ParentClass.controls_padding * 2), ParentView.height
			elif ParentClass.OverFill == "scale" and ParentView.width < int(Last_x + LastWidth + self.width + ParentClass.controls_padding * 2):
				def Animate():
					ParentView.width = int(Last_x + LastWidth + self.width + ParentClass.controls_padding * 2)
					ParentClass.width = ParentView.width
				ui.animate(Animate, 0.5)




class IconButton (object):
	__MotherView = None
	__MotherClass = None
	__SelfView = None
	
	# propertys
	icon = "typb:Heart"
	iconcolor = "#9bbeff"
	bgcolor = None
	width = 80
	height = 80
	border_radius = 0
	hide = False
	opacity = 1.0
	its_image = False
	# actions
	on_click = None
	
	def __init__(self, icon='typb:Heart', iconcolor="#9bbeff", width=150, height=50, border_radius=0, hide=False, opacity=1.0, bgcolor=None, on_click=None, its_image=False):
		self.__SelfView = ui.Button()
		self.__MotherClass = None
		self.__MotherView = None
		self.icon = icon
		self.iconcolor = iconcolor
		self.width = width
		self.height = height
		self.border_radius = border_radius
		self.hide = hide
		self.opacity = opacity
		self.bgcolor = bgcolor
		self.on_click = on_click
		self.its_image = its_image
		self.update()
	
	def update(self):
		bb = self
		def ACTION(self):
			if bb.on_click != None:
				threading.Thread(target=bb.on_click, args=[bb]).start()
			
		b = self.__SelfView
		b.action = ACTION
		if self.its_image: b.image = ui.Image.named(self.icon).with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		else: b.image = ui.Image(self.icon)
		b.background_color = self.bgcolor
		b.tint_color = self.iconcolor
		b.width = self.width
		b.height = self.height
		b.corner_radius = self.border_radius
		b.hidden = self.hide
		b.alpha = self.opacity
		
		if b.on_screen == False: return
		
		if self.__MotherClass.stack == "v":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.y = self.y
		elif self.__MotherClass.stack == "h":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.x = self.x
	
	
	def Respown(self, ParentView, stack, ParentClass):
		self.__MotherView = ParentView
		self.__MotherClass = ParentClass
		
		if str(stack).lower() == "v":
			Last_y = 0
			LastHeight = 0
			for i in ParentView.subviews:
				if i.y > Last_y: Last_y = i.y
				LastHeight = i.height
			self.__SelfView.center = (ParentView.width * 0.5, ParentView.height * 0.5)
			if list(ParentView.subviews) == []: self.__SelfView.y = ParentClass.controls_padding
			else: self.__SelfView.y = Last_y + ParentClass.controls_padding + LastHeight
			
			if self.__SelfView in list(self.__MotherView.subviews): pass
			else: self.__MotherView.add_subview(self.__SelfView)
			
			self.x = self.__SelfView.x; self.y = self.__SelfView.y
			
			if ParentClass.OverFill == "scroll":
				ParentView.content_size = ParentView.width, int(Last_y + LastHeight + self.height + ParentClass.controls_padding * 2)
			elif ParentClass.OverFill == "scale" and ParentView.height < int(Last_y + LastHeight + self.height + ParentClass.controls_padding * 2):
				def Animate():
					ParentView.height = int(Last_y + LastHeight + self.height + ParentClass.controls_padding * 2)
				ui.animate(Animate, 0.5)
				
		elif str(stack).lower() == "h":
			Last_x = 0
			LastWidth = 0
			for i in ParentView.subviews:
				if i.x > Last_x: Last_x = i.x
				LastWidth = i.width
			self.__SelfView.center = (ParentView.width * 0.5, ParentView.height * 0.5)
			if list(ParentView.subviews) == []: self.__SelfView.x = ParentClass.controls_padding
			else: self.__SelfView.x = Last_x + ParentClass.controls_padding + LastWidth
			self.__MotherView.add_subview(self.__SelfView)
			self.x = self.__SelfView.x; self.y = self.__SelfView.y
			
			if ParentClass.OverFill == "scroll":
				ParentView.content_size = int(Last_x + LastWidth + self.width + ParentClass.controls_padding * 2), ParentView.height
			elif ParentClass.OverFill == "scale" and ParentView.width < int(Last_x + LastWidth + self.width + ParentClass.controls_padding * 2):
				def Animate():
					ParentView.width = int(Last_x + LastWidth + self.width + ParentClass.controls_padding * 2)
					ParentClass.width = ParentView.width
				ui.animate(Animate, 0.5)
		
		
		elif str(stack).lower() == "z":
			self.__SelfView.x = self.x
			self.__SelfView.y = self.y
			if self.__SelfView in list(self.__MotherView.subviews): pass
			else: self.__MotherView.add_subview(self.__SelfView)
