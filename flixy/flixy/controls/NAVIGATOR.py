from ..Tools.action import do_action
import ui
import time


class Navigate (object):
	def __init__ (self, page, controls, show=False, on_back=None, back_btn_color="#6da0ff"):
		if hasattr(page, "page"):
			raise NameError("The navigator accept only pages.")
		self.__page_controls = []
		for i in page.controls:
			self.__page_controls.append({"class":i, "props":dict(i.__dict__)})
		self.controls = controls
		self.__page = page
		self.__is_presented_ones = False
		self.swipe_back_started = False
		
		self.on_back = on_back
		
		self.__back_animator = ui.View(width=0, height=2, x=0, y=0, bg_color='#649aff')
		self.__page.self_ui.add_subview(self.__back_animator)
		
		self.backbtn = ui.Button(title="< Back", tint_color=back_btn_color, font=('Avenir', 18), x=25, y=75, action=self.__custom_go_back)
		if page.appbar != None:
			self.backbtn.y = page.appbar.self_ui.height
		
		if show:
			self.show()
	
	def show (self, *args):
		# reset
		self.__last_on_touch = self.__page.on_touch
		self.__page.on_touch = self.__on_swipe
		if self.__is_presented_ones == False:
			self.__page_controls = []
			for i in self.__page.controls:
				self.__page_controls.append({"class":i, "props":dict(i.__dict__)})
			self.__is_presented_ones = True
		# start showing	
		for i in self.__page_controls:
			i["class"].opacity = 0.0
			ui.animate(i["class"].update, 0.4)
		
		time.sleep(0.5)
		self.__page.clear()
		
		for i in self.controls:
			self.__page.add(i)
		
		
		self.__page.self_ui.add_subview(self.__back_animator)
		self.__page.self_ui.add_subview(self.backbtn)
		
		self.backbtn.bring_to_front()
	
	def back (self, *args):
		self.__page.on_touch = self.__last_on_touch
		for i in self.controls:
			orgin = i.opacity
			i.opacity = 0.0
			ui.animate(i.update, 0.4)
			i.opacity = orgin
		time.sleep(0.5)
		self.__page.clear()
		for i in self.__page_controls:
			self.__page.add(i["class"])
			i["class"].__dict__ = dict(i["props"])
			ui.animate(i["class"].update, 0.4)
		
		# do action
		do_action(self.on_back, [self])
		
		self.__is_presented_ones = True
	
	def __on_swipe (self, state, cls):
		if state == "start" and int(cls.touch_x) < 35:
			self.swipe_back_started = True
		elif state == "move" and self.swipe_back_started:
			the_half_half_number_of_width = cls.width / 10
			if cls.touch_x >= the_half_half_number_of_width:
				self.swipe_back_started = False
				self.back()
				self.__back_animator.width = 0
			else:
				self.__back_animator.width = cls.touch_x / float(cls.width / 10) * cls.width
		else:
			self.swipe_back_started = False
			self.__back_animator.width = 0
			
	
	def __custom_go_back (self, cls):
		do_action(self.back, [])
