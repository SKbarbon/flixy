from .VIEW import View
from .TAB_VIEW import TabView

import sys
import ui, appex
import inspect
import threading


sys.setrecursionlimit(999999)


class app (object):
	
	__mother = None
	__content_view = None
	__Tabview = None
	
	def __init__(self, target, view_mode="fullscreen", tabview=None, run_as_widget=False):
		self.__Tabview = tabview
		
		TheView = View()
		TheView.controls_padding = 0
		TheView.stack = "z"
		TheView.OverFill = "none"
		TheView.on_update = self.on_update_mother
		TheView.on_resize = self.on_update_mother
		TheView.show(view_mode)
		self.__mother = TheView
		
		
		if tabview != None:
			TheView.add(tabview)
			tabview.update()
		
		Content_View = View()
		Content_View.bgcolor = '#f4f4f4'
		Content_View.x = 0
		Content_View.OverFill = "scroll"
		Content_View.y = 0
		Content_View.width = TheView.width
		Content_View.height = TheView.height
		Content_View.update()
		TheView.add(Content_View)
		self.__content_view = Content_View
		
		
		TheView.update()
		TheView.on_close = Content_View.close
		self.on_update_mother()
		
		target(Content_View)
	
	
	def on_update_mother(self, *args):
		self.__mother.on_close = self.__content_view.close
		self.__mother.name = self.__content_view.name
		if self.__content_view.on_resize != None: threading.Thread(daemon=True, target=self.__content_view.on_resize).start()
		self.__content_view.update()
		if self.__Tabview == None:
			self.__content_view.width = self.__mother.width
			self.__content_view.height = self.__mother.height
			self.__content_view.x = 0
			self.__content_view.y = 0
			self.__content_view.update()
		else:
			self.__Tabview.update()
			if self.__mother.width < 675:
				# if iphone
				self.__content_view.width = self.__mother.width
				self.__content_view.height = self.__mother.height - 200 / 2
				self.__content_view.x = 0
				self.__content_view.y = 0
				self.__content_view.update()
			else:
				# if ipad, mac
				self.__content_view.width = self.__mother.width - 200
				self.__content_view.height = self.__mother.height
				self.__content_view.x = 200
				self.__content_view.y = 0
				self.__content_view.update()
