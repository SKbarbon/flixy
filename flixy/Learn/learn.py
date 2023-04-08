from ..flixy import *
from .lessons.Text import text_lesson
from .lessons.app import app_lesson
from .lessons.page import page_lesson
from .lessons.button import button_lesson
from .lessons.row import row_lesson
from .lessons.column import column_lesson
from .lessons.textfield import textfield_lesson
from .lessons.webview import webview_lesson
from .lessons.sheet import sheet_lesson
from .lessons.navigate import navigate_lesson


class learn_flixy:
	def __init__ (self):
		app(target=self.App)
	
	def App(self, page):
		page.on_resize = self.__on_resize
		page.appbar = AppBar(
			title = "Learn flixy",
			btn_icon="iob:close_circled_32",
			on_click_btn = self.close
		)
		self.page = page
		
		spliter = Row(expand_width=True, expand_height=True, scroll=False, spacing=0)
		page.add(spliter)
		self.spliter = spliter
		
		selections_place = Column(width=spliter.width/4, expand_height=True)
		spliter.add(selections_place)
		self.selections_place = selections_place
		
		preview_section = Column(width=spliter.width-(spliter.width/4), expand_height=True)
		spliter.add(preview_section)
		self.preview_section = preview_section
		
		title = Text("	Controls", size=28, expand_width=True, text_align=0)
		selections_place.add(title)
		
		all_lessons = ["app", "Page", "Text", "Button", "Row", "Column", "TextField", "WebView", "Sheet", "Navigate"]
		self.all_button_navigators = []
		for i in all_lessons:
			b = Button(i, width=selections_place.width-70, height=37, border_radius=10, bgcolor="white", title_color="black", bgcolor_after_hover='#d7d7d7')
			b.on_click = self.__on_choose_page
			self.all_button_navigators.append(b)
			selections_place.add(b)
		
		for i in ["TextView", "AppBar", "Haptics", "Sound"]:
			b = Button(i, width=selections_place.width-70, height=37, border_radius=10, bgcolor="#d7d7d7", title_color="black", bgcolor_after_hover='#d7d7d7')
			#b.on_click = self.__on_choose_page
			self.all_button_navigators.append(b)
			selections_place.add(b)
		
	
	def __on_resize(self, page):
		if hasattr(self, "spliter") == False: return 
		sp = self.spliter
		self.selections_place.width = self.page.width / 4
		self.preview_section.width = self.page.width-(self.page.width/4)
		
		for i in self.all_button_navigators:
			i.width = self.selections_place.width-70
		
		self.page.remake_controls()
		self.page.update()
	
	def __on_choose_page (self, btn):
		func = self.get_page_function(btn.title)
		func(self.preview_section)
	
	def close (self):
		self.page.close()
	
	def get_page_function (self, name):
		al = {
			"Text" : text_lesson,
			"app" : app_lesson,
			"Page" : page_lesson,
			"Button" : button_lesson,
			"Row" : row_lesson,
			"Column" : column_lesson,
			"TextField" : textfield_lesson,
			"WebView" : webview_lesson,
			"Sheet" : sheet_lesson,
			"Navigate" : navigate_lesson
		}
		return al[name]
