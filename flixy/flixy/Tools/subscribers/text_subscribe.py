



class textSubscribe (object):
	
	def __init__ (self, controls=[]):
		self.controls = controls
		self.subscribeStatus = {
			"value" : False,
			"color" : False,
			"bgcolor" : False,
			"text_align" : False
		}
		
		self.__value = ""
		self.__color = "white"
		self.__bgcolor = None
		self.__text_align = 0
	
	def __update_all (self):
		if self.subscribeStatus["value"]:
			for i in self.controls:
				i.value = self.__value
				i.update()
		
		if self.subscribeStatus["color"]:
			for i in self.controls:
				i.color = self.__color
				i.update()
		
		if self.subscribeStatus["bgcolor"]:
			for i in self.controls:
				i.bgcolor = self.__bgcolor
				i.update()
		
		if self.subscribeStatus["text_align"]:
			for i in self.controls:
				i.text_align = self.__text_align
				i.update()

	
	# setters
	@property
	def value(self): return self.__value
	@value.setter
	def value (self, arg):
		self.subscribeStatus["value"] = True
		self.__value = arg
		self.__update_all()
	
	
	@property
	def color (self): return self.__color
	@color.setter
	def color (self, arg):
		self.subscribeStatus["color"] = True
		self.__color = arg
		self.__update_all()
	
	@property
	def bgcolor (self): return self.__bgcolor
	@bgcolor.setter
	def bgcolor (self, arg):
		self.subscribeStatus["bgcolor"] = True
		self.__bgcolor = arg
		self.__update_all()
	
	@property
	def text_align(self): return self.__text_align
	@text_align.setter
	def text_align(self, arg):
		self.subscribeStatus["text_align"] = True
		self.__text_align = arg
		self.__update_all()
