import ui
import threading



class slider (object):
	__MotherView = None
	__MotherClass = None
	__SelfView = None
	
	# Propertys
	value = 0
	width = 150
	height = 50
	hide = False
	opacity = 1.0
	x = 0
	y = 0
	parent = None
	color = "white"
	# actions
	on_edit = None
	
	def __init__(self, value=0, width=150, height=50,  x=0, y=0, hide=False, opacity=1.0, on_edit=None, color="white"):
		self.__SelfView = ui.Slider()
		self.__MotherClass = None
		self.__MotherView = None
		
		self.width = width
		self.height = height
		self.hide = hide
		self.opacity = opacity
		self.x = x
		self.y = y
		self.value = value
		self.on_edit = on_edit
		self.parent = None
		self.color = color
		self.update()
	
	def update(self):
		ss = self
		def on_edit_action(self):
			ss.value = s.value
			if ss.on_edit != None:
				th = threading.Thread(target=ss.on_edit, args=[ss])
				th.daemon = True
				th.start()
		
		s = self.__SelfView
		s.width = self.width
		s.height = self.height
		s.hidden = self.hide
		s.alpha = self.opacity
		s.x = self.x
		s.y = self.y
		s.tint_color = self.color
		s.value = self.value
		s.action = on_edit_action
		self.parent = self.__MotherClass
		
		if s.on_screen == False: return
		
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
