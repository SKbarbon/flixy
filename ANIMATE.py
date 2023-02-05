import ui
import time
import threading



class animate (object):
	__a_copy = {}
	
	subview = None
	animate_func = None
	loop = False
	delay = 0.3
	
	def __init__(self, subview, animate_func, loop=False, delay=0.3):
		self.__a_copy = {}
		self.__a_copy.update(dict(subview.__dict__))
		self.subview = subview
		self.animate_func = animate_func
		self.loop = loop
		self.delay = delay
		
		TH = threading.Thread(target=self.__run)
		TH.daemon = True
		TH.start()
	
	def __run(self):
		def run_it():
			self.animate_func(self.subview)
			self.subview.update()
			self.subview.parent.ReBuildSubItems()
			self.subview.parent.update()
		
		def restore_it():
			self.subview.__dict__ = dict(self.__a_copy)
			self.subview.update()
			self.subview.parent.ReBuildSubItems()
			self.subview.parent.update()
		
		if self.loop == False:
			ui.animate(run_it, self.delay)
		
		elif self.loop == True:
			while self.loop == True:
				try: 
					if self.subview.is_on_screen() == False: break; return;
				except: raise NameError("Cannot use loop animation except with a View class."); break; return;
				ui.animate(run_it, self.delay)
				time.sleep(self.delay+0.1)
				ui.animate(restore_it, self.delay)
				time.sleep(self.delay+0.1)
	
	def stop(self):
		self.loop = False
	
	def __continue_the_loop(self):
		return self.loop
