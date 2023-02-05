import ui
import threading


class WebView (object):
	__MotherView = None
	__MotherClass = None
	__SelfView = None
	
	# propertys
	url = ""
	is_url_local = False
	__urls_history = []
	width = 100
	height = 100
	hide = False
	opacity = 1.0
	border_radius = 0
	x = 0
	y = 0
	
	# actions
	on_load_start = None
	on_load_finish = None
	on_load_fail = None
	
	def __init__(self, url="", width=100, height=100, hide=False, opacity=1.0, border_radius=0, x=0, y=0, on_load_start=None, on_load_finish=None, on_load_fail=None, is_url_local = False):
		class MyWebViewDelegate (object):
			wvs = self
			def webview_should_start_load(self, webview, url, nav_type):
				if wvs.on_load_start != None: threading.Thread(target=wvs.on_load_start, args=[wvs]).start()
				return True
			def webview_did_start_load(self, webview):
				pass
			def webview_did_finish_load(self, webview):
				if wvs.on_load_finish != None: threading.Thread(target=wvs.on_load_finish, args=[wvs]).start()
			def webview_did_fail_load(self, webview, error_code, error_msg):
				if wvs.on_load_fail != None: threading.Thread(target=wvs.on_load_fail, args=[wvs]).start()
		
		self.__SelfView = ui.WebView()
		self.__MotherClass = None
		self.__MotherView = None
		
		self.url = url
		self.width = width
		self.height = height
		self.hide = hide
		self.opacity = opacity
		self.border_radius = border_radius
		self.x = x
		self.y = y
		self.is_url_local = is_url_local
		
		self.on_load_start = on_load_start
		self.on_load_finish = on_load_finish
		self.on_load_fail = on_load_fail
		
		self.parent = None
		
		self.update()
	
	
	def update(self):
		wv = self.__SelfView
		if self.is_url_local: wv.load_html(self.url)
		elif self.is_url_local == False: wv.load_url(self.url)
		wv.width = self.width
		wv.height = self.height
		wv.hidden = self.hide
		wv.alpha = self.opacity
		wv.corner_radius = self.border_radius
		self.parent = self.__MotherClass
		if wv.on_screen == False: return 
		
		if self.__MotherClass.stack == "v":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.y = self.y
		elif self.__MotherClass.stack == "h":
			self.__SelfView.center = (self.__MotherView.width * 0.5, self.__MotherView.height * 0.5)
			self.__SelfView.x = self.x
		elif self.__MotherClass.stack == "z":
			self.__SelfView.x = self.x
			self.__SelfView.y = self.y
	
	
	def exec_js(self, javascript_code):
		return self.__SelfView.eval_js(javascript_code)
	
	
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
