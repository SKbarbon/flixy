import ui
import threading



class TextField (object):
	__MotherView = None
	__MotherClass = None
	__SelfView = None
	
	
	# propertys
	text = ""
	textcolor = "black"
	placeholder = ""
	width = 150
	height = 35
	border_radius = 0
	border_width = 0
	hide = False
	opacity = 1.0
	y = 0
	x = 0
	alignment = 1
	enabled = True
	parent = None
	# actions
	on_submit = None
	on_change = None
	on_start = None
	
	def __init__(self, placeholder="", text="", width=150, height=35, border_radius=0, y=0, x=0, hide=False, opacity=1.0, on_submit=None, on_change=None, on_start=None, textcolor = "black", enabled = True, alignment=1, border_width=0):
		TheTF_class = self
		class MyTextFieldDelegate (object):
			def textfield_should_begin_editing(self):
				if TheTF_class.on_start != None: threading.Thread(target=TheTF_class.on_start, args=[TheTF_class]).start()
				return True
			def textfield_did_begin_editing(self):
				pass
			def textfield_did_end_editing(self):
				pass
			def textfield_should_return(self):
				self.end_editing()
				if TheTF_class.on_submit != None: threading.Thread(target=TheTF_class.on_submit, args=[TheTF_class]).start()
				return True
			def textfield_should_change(self, range, replacement):
				return True
			def textfield_did_change(self):
				TheTF_class.text = self.text
				if TheTF_class.on_change != None: threading.Thread(target=TheTF_class.on_change, args=[TheTF_class]).start()
		
		self.__SelfView = ui.TextField()
		self.__SelfView.delegate = MyTextFieldDelegate
		self.__MotherClass = None
		self.__MotherView = None
		self.placeholder = placeholder
		self.text = text
		self.width = width
		self.textcolor = textcolor
		self.height = height
		self.border_radius = border_radius
		self.y = y
		self.x = x
		self.on_submit = on_submit
		self.on_change = on_change
		self.on_start = on_start
		self.enabled = enabled
		self.alignment = alignment
		self.border_width = border_width
		self.parent = None
		self.update()
		
		
	def update(self):
		tf = self.__SelfView
		tf.text = self.text
		tf.placeholder = self.placeholder
		tf.width = self.width
		tf.text_color = self.textcolor
		tf.height = self.height
		tf.hidden = self.hide
		tf.alpha = self.opacity
		tf.enabled = self.enabled
		tf.alignment = self.alignment
		tf.border_width = self.border_width
		self.parent = self.__MotherClass
		if tf.on_screen == False: return
		
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
