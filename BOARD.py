import ui
import threading
import time



class Board (object):
	__MotherView = None
	__MotherClass = None
	__SelfView = None
	__isSelfMain = False
	
	# propertys
	__items = []
	parent = None
	stack = "v"
	name = ""
	bgcolor = "white"
	border_color = "black"
	border_width = 0.0
	border_radius = 0
	width = 100
	height = 85
	x = 0
	y = 0
	hide = False
	controls_padding = 10
	OverFill = "scale"
	opacity = 1.0
	
	drawable = True
	Touch_x = 0
	Touch_y = 0
	# actions
	on_resize = None
	on_close = None
	on_update = None
	on_touch_start = None
	on_touch_moved = None
	on_touch_end = None
	
	def __init__(self, stack="v", bgcolor="white", border_color="black", border_width=0.0, border_radius=0, width=100, height=85, on_resize=None, on_close=None, on_update=None, name="", OverFill="scale", controls_padding=10, hide=False, opacity=1.0, drawable = True, on_touch_start = None, on_touch_moved = None, on_touch_end = None, auto_fit_childs=False, fit_padding=10):
		class BoardView (ui.View):
			bvs = self
			def __init__(self):
				self.path = None
				self.action = None
				
				self.bvs.width = self.width
				self.bvs.height = self.height
				self.bvs.x = self.x
				self.bvs.y = self.y
			
			
			def touch_began(self, touch):
				x, y = touch.location
				self.bvs.Touch_x = x
				self.bvs.Touch_y = y
				if self.bvs.on_touch_start != None: threading.Thread(target=self.bvs.on_touch_start, args=[self.bvs]).start()
				if self.bvs.drawable:
					self.path = ui.Path()
					self.path.line_width = 8.0
					self.path.line_join_style = ui.LINE_JOIN_ROUND
					self.path.line_cap_style = ui.LINE_CAP_ROUND
					self.path.move_to(x, y)
			
			def touch_moved(self, touch):
				x, y = touch.location
				self.bvs.Touch_x = x
				self.bvs.Touch_y = y
				if self.bvs.on_touch_moved != None: threading.Thread(target=self.bvs.on_touch_moved, args=[self.bvs]).start()
				if self.bvs.drawable:
					self.path.line_to(x, y)
					self.set_needs_display()
			
			def touch_ended(self, touch):
				x, y = touch.location
				self.bvs.Touch_x = x
				self.bvs.Touch_y = y
				if self.bvs.on_touch_end != None: threading.Thread(target=self.bvs.on_touch_end, args=[self.bvs]).start()
				if self.bvs.drawable:
					if callable(self.action):
						self.action(self)
					self.path = None
					self.set_needs_display()
			
			def draw(self):
				if self.path:
					self.path.stroke()
		
		self.__SelfView = BoardView()
		self.__isSelfMain = False
		self.stack = stack
		self.bgcolor = bgcolor
		self.border_color = border_color
		self.border_width = border_width
		self.border_radius = border_radius
		self.width = width
		self.height = height
		self.on_resize = on_resize
		self.on_close = on_close
		self.on_update = on_update
		self.name = name
		self.__items = []
		self.OverFill = OverFill
		self.__MotherView = None
		self.__MotherClass = None
		self.controls_padding = controls_padding
		self.hide = hide
		self.opacity = opacity
		self.drawable = drawable
		self.Touch_x = 0
		self.Touch_y = 0
		self.on_touch_start = on_touch_start
		self.on_touch_moved = on_touch_moved
		self.on_touch_end = on_touch_end
		self.parent = None
		self.auto_fit_childs = auto_fit_childs
		self.fit_padding = fit_padding
		self.update()
	
	def update(self):
		def update_childs():
			for i in self.__items:
				if self.auto_fit_childs:
					if self.stack == "v": i.width = self.width - int(self.fit_padding * 2)
					elif self.stack == "h": i.height = self.height - int(self.fit_padding * 2)
				i.update()
		
		v = self.__SelfView
		v.background_color = self.bgcolor
		v.border_color = self.border_color
		v.border_width = self.border_width
		v.corner_radius = self.border_radius
		v.hidden = self.hide
		v.name = self.name
		v.alpha = self.opacity
		self.parent = self.__MotherClass
		
		# Update all subviews
		if self.__isSelfMain:
			self.width = v.width
			self.height = v.height
			update_childs()
		else:
			v.width = self.width
			v.height = self.height
		
		if self.__isSelfMain == True: return
		if self.__SelfView.on_screen == False: return
		
		
		if self.__MotherClass.stack == "v":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.y = self.y
		elif self.__MotherClass.stack == "h":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.x = self.x
		elif self.__MotherClass.stack == "z":
			self.__SelfView.x = self.x
			self.__SelfView.y = self.y
		
		update_childs()
		
		# The on_update function
		if self.on_update != None:
			try: threading.Thread(target=self.on_update).start()
			except Exception as e: print(f"on_update Error passed:\n{e}")
	
	def add(self, item):
		item.Respown(self.__SelfView, self.stack, self)
		self.__items.append(item)
	
	def show(self, mode="fullscreen"):
		v = self.__SelfView
		if mode == "fullscreen":
			self.OverFill = "none"
		if v.superview != None: raise NameError("cannot use function 'show()' on sub view"); return 
		self.__SelfView.present(str(mode).lower())
		self.__isSelfMain = True
		Th1 = threading.Thread(target=self.__BackgroundThread)
		Th1.start()
		self.width = self.__SelfView.width
		self.height = self.__SelfView.height
		self.update()
	
	def __BackgroundThread(self):
		Last_width = self.__SelfView.width
		Last_Height = self.__SelfView.height
		self.width = self.__SelfView.width
		self.height = self.__SelfView.height
		while self.__SelfView.on_screen:
			if Last_width != self.__SelfView.width or Last_Height != self.__SelfView.height:
				Last_width = self.__SelfView.width
				Last_Height = self.__SelfView.height
				self.width = self.__SelfView.width
				self.height = self.__SelfView.height
				self.update()
				threading.Thread(target=self.on_resize, args=[self]).start()
	
	def ReBuildSubItems(self):
		for i in self.__SelfView.subviews:
			self.__SelfView.remove_subview(i)
		for i in self.__items:
			i.Respown(self.__SelfView, self.stack, self)
	
	def Respown(self, ParentView, stack, ParentClass):
		self.__MotherView = ParentView
		self.__MotherClass = ParentClass
		
		if self.__isSelfMain: raise NameError("cannot add the main view inside a sub view")
		
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
			
			if ParentClass.OverFill == "scale" and ParentView.height < int(Last_y + LastHeight + self.height + ParentClass.controls_padding * 2):
				def Animate():
					ParentView.height = int(Last_y + LastHeight + self.height + ParentClass.controls_padding * 2)
					ParentClass.height = ParentView.height
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
			
			if ParentClass.OverFill == "scale" and ParentView.width < int(Last_x + LastWidth + self.width + ParentClass.controls_padding * 2):
				def Animate():
					ParentView.width = int(Last_x + LastWidth + self.width + ParentClass.controls_padding * 2)
				ui.animate(Animate, 0.5)
		
		elif str(stack).lower() == "z":
			self.__SelfView.x = self.x
			self.__SelfView.y = self.y
			if self.__SelfView in list(self.__MotherView.subviews): pass
			else: self.__MotherView.add_subview(self.__SelfView)
	
	def clear(self):
		for i in self.__SelfView.subviews:
			self.__SelfView.remove_subview(i)
		self.__items = []
	
	
	def is_on_screen(self):
		return self.__SelfView.on_screen
		
	
	def Remove_SubView(self, SubView_class):
		SubView_class.remove_self(just_remove_view=True)
		self.__items.remove(SubView_class)
		del SubView_class
	
	def remove_self(self, just_remove_view=False):
		self.__MotherView.remove_subview(self.__SelfView)
		if just_remove_view == False: self.__MotherClass.Remove_SubView(self)
	
	
	def close(self):
		if self.__SelfView.on_screen and self.__isSelfMain:
			self.__SelfView.close()
			self.on_close()
	
	def bring_to_top(self):
		self.__SelfView.bring_to_front()
