from .VIEW import View
from .BOARD import Board
from .BUTTON import IconButton
import ui
import time
import threading


class Sheet (object):
	__SelfClass = None
	__MotherClass = None
	__BackCoverClass = None
	__close_btn_bar = None
	
	# propertys
	__on_show = False
	__cloased = False
	subview = None
	fullscreen = False
	bgcolor = "white"
	close_btn = True
	
	# actions
	on_close = None
	on_unpush = None
	
	def __init__(self, subview, fullscreen=False, bgcolor="white", on_close=None, close_btn=True, on_unpush = None):
		self.__SelfClass = View(OverFill="none")
		self.__MotherClass = None
		self.__BackCoverClass = None
		self.__close_btn_bar = None
		
		self.subview = subview
		self.fullscreen = fullscreen
		self.bgcolor = bgcolor
		self.on_close = on_close
		self.on_unpush = on_unpush
		self.__on_show = False
		self.close_btn = close_btn
	
	
	def update(self):
		sh = self.__SelfClass
		sh.OverFill = "none"
		sh.controls_padding = 0
		sh.auto_fit_childs = True
		sh.padding_fit = 0
		sh.bgcolor = self.bgcolor
		sh.border_radius = 10
		bg_cv = self.__BackCoverClass
		mother = self.__MotherClass
		sh.update()
		
		if mother == None: return
		if mother.stack != "z": self.close()
		
		if self.fullscreen:
			bg_cv.width = mother.width
			bg_cv.height = mother.height
			sh.width = mother.width
			sh.height = mother.height
			sh.x = 0
			sh.y = 0
		else:
			if mother.width < 675:
				# if phone
				bg_cv.width = mother.width
				bg_cv.height = mother.height
				sh.width = mother.width 
				sh.height = mother.height - 100
				sh.x = 0
				sh.y = 100
			else:
				# if ipad, mac
				bg_cv.width = mother.width
				bg_cv.height = mother.height
				sh.width = mother.width / 1.5
				sh.height = mother.height / 1.5
				sh.x = mother.width / 2 - sh.width / 2
				sh.y = mother.height / 2 - sh.height / 2
		
		self.subview.width = sh.width
		self.subview.height = sh.height - 45
		self.subview.x = 0
		self.subview.y = 45
		self.subview.update()
		
		bg_cv.update()
		sh.update()
		
	
	def Respown(self, p, s, ParentClass):
		if self.__MotherClass != None: return
		
		p = ParentClass.parent
		lp = p
		lpp = lp
		while lp != None:
			lpp = lp
			lp = lp.parent
		
		if lpp.is_on_screen() == False: return
		if lpp.stack != "z": return 
		
		self.__MotherClass = lpp
		
		sh = self.__SelfClass
		sh.opacity = 0.0
		sh.update()
		
		if self.close_btn:
			v = View(OverFill="none")
			v.width = sh.width
			v.height = 40
			v.bgcolor = None
			v.stack = "h"
			v.update()
			
			cls_btn = IconButton()
			cls_btn.iconcolor = "#808080"
			cls_btn.icon = 'iob:close_circled_256'
			cls_btn.width = 30; cls_btn.height = 30;
			cls_btn.on_click = self.unpush
			cls_btn.update()
			v.add(cls_btn)
			sh.add(v)
			v.bring_to_top()
			self.__close_btn_bar = v
		
		sh.add(self.subview)
		self.subview.width = sh.width
		self.subview.height = sh.height - 45
		self.subview.x = 0
		self.subview.y = 45
		self.subview.update()
		
		
		back_cover = Board()
		back_cover.on_touch_end = self.unpush
		back_cover.width = lpp.width
		back_cover.drawable = False
		back_cover.height = lpp.height
		back_cover.x = 0; back_cover.y = 0;
		back_cover.bgcolor = "black"
		back_cover.opacity = 0.0
		back_cover.update()
		lpp.add(back_cover)
		self.__BackCoverClass = back_cover
		
		lpp.add(self.__SelfClass)
		lpp.add(self)
		self.update()
		
	
	def push(self, *args):
		sh = self.__SelfClass
		if sh.is_on_screen() == False: return 
		self.update()
		back_cover = self.__BackCoverClass
		back_cover.opacity = 0.7
		ui.animate(back_cover.update, 0.3)
		sh.opacity = 1.0
		ui.animate(sh.update, 0.5)
		return self
	
	def unpush(self, *args):
		sh = self.__SelfClass
		if sh.is_on_screen() == False: return
		self.update()
		back_cover = self.__BackCoverClass
		back_cover.opacity = 0.0
		sh.opacity = 0.0
		ui.animate(back_cover.update, 0.3)
		ui.animate(sh.update, 0.3)
		
		if self.on_unpush != None:
			th = threading.Thread(target=self.on_unpush, args=[self])
			th.daemon = True
			th.start()
	
	def close(self, *args):
		sh = self.__SelfClass
		if sh.is_on_screen() == False: return
		back_cover = self.__BackCoverClass
		self.unpush()
		
		time.sleep(0.4)
		sh.remove_self()
		back_cover.remove_self()
		if self.on_close != None:
			th = threading.Thread(target=self.on_close, args=[self])
			th.daemon = True
			th.start()
		return
	
	def change_subview(self, subview):
		self.__SelfClass.clear()
		self.subview = subview
		self.__SelfClass.add(self.__close_btn_bar)
		self.__SelfClass.add(subview)
		self.__SelfClass.ReBuildSubItems()
		self.update()
