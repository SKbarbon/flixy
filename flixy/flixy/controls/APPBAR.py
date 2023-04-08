from ..Tools.action import do_action
import ui

class AppBar ():
	
	def __init__ (self, title="", title_size=23, title_color="white", bgcolor=None, center_title=False, on_click_btn=None, btn_icon='typb:Feed', icon_color="white"):
		self.page = None
		self.__self_ui = ui.View()
		self.__title_label = ui.Label()
		self.__bar_btn = ui.Button()
		
		self.__self_ui.add_subview(self.__title_label)
		self.__self_ui.add_subview(self.__bar_btn)
		
		self.title = title
		self.title_size = title_size
		self.bgcolor = bgcolor
		self.title_color = title_color
		self.icon_color = icon_color
		self.center_title = center_title
		self.on_click_btn = on_click_btn
		self.btn_icon = btn_icon
		
		self.update()
	
	def update (self):
		v = self.__self_ui
		l = self.__title_label
		b = self.__bar_btn
		
		if self.page == None: return 
		
		v.width = self.page.width
		v.height = 130
		v.bg_color = self.bgcolor
		
		l.text = self.title
		l.text_color = self.title_color
		if self.page != None: l.font = self.page.font_family, self.title_size
		l.height = v.height
		if self.center_title:
			l.width = v.width
			l.alignment = 1
		else:
			l.x = 20
			l.y = 0
			l.width = v.width - 20
			l.alignment = 0
		
		
		b.width = 35
		b.action = self.__custom_bar_action
		b.tint_color = self.icon_color
		b.height = 35
		b.x = v.width - 80
		b.y = v.height / 2 - b.height / 2
		b.image = ui.Image(self.btn_icon)
	
	
	def __custom_bar_action (self, *args):
		do_action(self.on_click_btn, [])
	
	
	@property
	def self_ui (self):
		return self.__self_ui
