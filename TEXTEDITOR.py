import ui
import threading



class TextEditor (object):
	__MotherView = None
	__MotherClass = None
	__SelfView = None
	
	
	# propertys
	text = ""
	bgcolor = "white"
	textcolor = "black"
	width = 100
	height = 100
	border_radius = 0
	hide = False
	opacity = 1.0
	y = 0
	x = 0
	editable = True
	selectable = True
	font_size = 20
	font_family = 'Avenir'
	alignment = 0
	parent = None
	# actions
	on_change = None
	on_start = None
	def __init__(self, text="", width=150, height=100, textcolor = "black", bgcolor = "white", border_radius = 0, hide = False, opacity = 1.0, y=0, x=0, on_change=None, editable = True, selectable = True, on_start = None, font_size = 20, font_family = 'Avenir', alignment = 0):
		TEC = self
		class MyTextFieldDelegate (object):
			def textview_should_begin_editing(self):
				if TEC.on_start != None: threading.Thread(target=TEC.on_start).start()
				return True
			
			def textview_did_change(self):
				TEC.text = self.text
				if TEC.on_change != None: threading.Thread(target=TEC.on_change).start()
		
		self.__SelfView = ui.TextView()
		self.__SelfView.delegate = MyTextFieldDelegate
		self.__MotherClass = None
		self.__MotherView = None
		self.text = text
		self.width = width
		self.height = height
		self.textcolor = textcolor
		self.bgcolor = bgcolor
		self.border_radius = border_radius
		self.hide = hide
		self.opacity = opacity
		self.y = y
		self.x = x
		self.on_change = on_change
		self.editable = editable
		self.selectable = selectable
		self.on_start = on_start
		self.font_size = font_size
		self.font_family = 'Avenir'
		self.alignment = alignment
		self.parent = None
		self.update()
	
	def update(self):
		tv = self.__SelfView
		tv.text = self.text
		tv.text_color = self.textcolor
		tv.background_color = self.bgcolor
		tv.width = self.width
		tv.height = self.height
		tv.corner_radius = self.border_radius
		tv.hidden = self.hide
		tv.alpha = self.opacity
		tv.editable = self.editable
		tv.selectable = self.selectable
		tv.font = self.font_family, self.font_size
		tv.alignment = self.alignment
		self.parent = self.__MotherClass
		if tv.on_screen == False: return 
		
		if self.__MotherClass.stack == "v":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.y = self.y
		elif self.__MotherClass.stack == "h":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.x = self.x
		elif self.__MotherClass.stack == "z":
			self.__SelfView.x = self.x
			self.__SelfView.y = self.y
	
	def stop_type(self):
		self.__SelfView.end_editing()
	
	def start_type(self):
		self.__SelfView.begin_editing()
	
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
