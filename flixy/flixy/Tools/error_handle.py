





def error_handling (function):
	def DoIt():
		try: function()
		except: pass
	
	return DoIt
