from .VIEW import View
from .BOARD import Board
from .BUTTON import IconButton
from .TEXT import Text
import ui


"""
{
	"name" : "TabViewItem",
	"icon" : "icon_image",
	"on_click" : func
}
"""



class TabView (object):
	__MotherView = None
	__SelfClass = None
	
	# propertys
	bgcolor = None
	
	title = "Home"
	title_color = "black"
	controls = []
	controls_bgcolor = None
	controls_font_family = 'Avenir'
	controls_icon_color = "black"
	controls_title_color = "black"
	controls_border_radius = 8
	hide_controls_icon_on_desktop = False
	
	def __init__(self, controls=[], controls_width = 100, controls_height = 100, controls_bgcolor = None, controls_border_radius = 8, bgcolor = None, controls_icon_color = "black", title="Home", title_color = "black", controls_title_color = "black", hide_controls_icon_on_desktop = False):
		self.__MotherView = None
		self.__SelfClass = View()
		
		self.bgcolor = bgcolor
		
		self.controls = controls
		self.controls_width = controls_width
		self.controls_height = controls_height
		self.controls_bgcolor = controls_bgcolor
		self.controls_border_radius = controls_border_radius
		self.controls_icon_color = controls_icon_color
		self.title = title
		self.title_color = title_color
		self.controls_title_color = controls_title_color
		self.hide_controls_icon_on_desktop = hide_controls_icon_on_desktop
		self.update()
		
	
	
	def update(self):
		tb = self.__SelfClass
		mother = self.__MotherView
		thick = 200
		
		tb.bgcolor = self.bgcolor
		tb.auto_fit_childs = True
		tb.fit_padding = 8
		tb.OverFill = "none"
		tb.update()
		
		if mother == None: return 
		
		tb.clear()
		if mother.width < 675:
			# if phone
			tb.controls_padding = 0
			tb.stack = "h"
			tb.width = mother.width
			tb.height = thick / 2
			tb.x = 0
			tb.y = mother.height - tb.height
			
			contr = []
			for i in self.controls:
				if "section" in i: pass
				else: contr.append(i)
			
			if int(len(contr)*100) < tb.width: tb.add(View(bgcolor=None, width=tb.width/2-len(contr)*100/2))
			for I in self.controls:
				if "section" in I: pass
				else:
					tab_btn = self.Phone_TabView_Button(I["name"], I["icon"], I["on_click"])
					tb.add(tab_btn)
			tb.update()
		else:
			# if ipad, mac
			tb.controls_padding = 12
			tb.stack = "v"
			tb.width = thick
			tb.height = mother.height
			tb.x = 0
			tb.y = 0
			tb.add(View(bgcolor=None, height=10))
			T = Text(self.title, height=30, textcolor=self.title_color)
			tb.add(T)
			tb.add(View(bgcolor=None, height=7))
			for I in self.controls:
				if "section" in I: tb.add(self.section_view(I["section"]))
				else:
					tab_btn = self.Desktop_TabView_Button(I["name"], I["icon"], I["on_click"])
					tb.add(tab_btn)
			tb.update()
		
		tb.update()
	
	
	def respown(self, motherView=None):
		self.__MotherView = motherView
		
		sl = self.__SelfClass
		self.__MotherView.add(sl)
		self.update()
	
	def Respown(self, p, s, ParentClass):
		self.respown(ParentClass)

	
	def Desktop_TabView_Button(self, tab_name, tab_icon, tab_click):
		
		b = Board()
		b.width = 100
		b.height = 40
		b.stack = "h"
		b.drawable = False
		b.on_touch_end = tab_click
		b.border_radius = self.controls_border_radius
		b.controls_padding = 10
		b.OverFill = "none"
		b.bgcolor =  self.controls_bgcolor
		b.update()
		
		tab_icon_img = IconButton(icon=tab_icon)
		tab_icon_img.on_click = tab_click
		tab_icon_img.width = 25
		tab_icon_img.height = 25
		tab_icon_img.iconcolor = self.controls_icon_color
		tab_icon_img.update()
		
		
		tab_title = Text(tab_name)
		tab_title.font_family = self.controls_font_family
		tab_title.textcolor = self.controls_title_color
		tab_title.alignment = 0
		tab_title.font_size = 17
		tab_title.width = b.width - 20
		tab_title.height = b.height
		tab_title.update()
		
		if self.hide_controls_icon_on_desktop:
			tab_title.font_size = 15
			tab_title.width = b.width
			tab_title.update()
			b.auto_fit_childs = True
			b.padding_fit = 0
			b.add(tab_title)
		else:
			b.add(tab_icon_img)
			b.add(tab_title)
		b.update()
		return b

	
	def Phone_TabView_Button(self, tab_name, tab_icon, tab_click):
		
		b = Board()
		b.width = 100
		b.height = 50
		b.stack = "v"
		b.drawable = False
		b.on_touch_end = tab_click
		b.border_radius = self.controls_border_radius
		b.controls_padding = 10
		b.OverFill = "none"
		b.bgcolor = None
		b.update()
		
		tab_icon_img = IconButton(icon=tab_icon)
		tab_icon_img.on_click = tab_click
		tab_icon_img.width = 25
		tab_icon_img.height = 25
		tab_icon_img.iconcolor = self.controls_icon_color
		tab_icon_img.update()
		b.add(tab_icon_img)
		
		
		tab_title = Text(tab_name)
		tab_title.font_family = self.controls_font_family
		tab_title.textcolor = self.controls_title_color
		tab_title.alignment = 1
		tab_title.font_size = 15
		tab_title.width = b.width
		tab_title.height = 30
		tab_title.update()
		b.add(tab_title)
		
		return b
	
	def section_view(self, title):
		T = Text(f"    {title}")
		T.textcolor = "#a0a0a0"
		T.font_size = 15
		T.height = 25
		T.alignment = 0
		T.update()
		return T



