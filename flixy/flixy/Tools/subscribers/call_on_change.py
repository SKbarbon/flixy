
from ...Tools.action import do_action

class callOnChange (object):
	
	def __init__ (self, value, function, event_name=""):
		self.__value = value
		self.function = function
		self.event_name=event_name
	
	@property
	def value (self):
		return self.__value
	
	@value.setter
	def value (self, arg):
		do_action(self.function, [self])
		self.__value = arg
