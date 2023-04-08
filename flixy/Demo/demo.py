from ..flixy import *




class start_demo:
	
	def __init__(self):
		app(target=self.App)
	
	def App(self, page:Page):
		self.page = page
		page.on_update = self.on_update
		page.appbar = AppBar(
			title = "Demo",
			btn_icon =  'iob:close_circled_24',
			on_click_btn=self.close
		)
		
		describer = Text("Choose a page to view", expand_width=True, opacity=0.7)
		page.add(describer)
		
		for i in ["Text", "Button", "WebView", "Navigate", "TextField", "TextView"]:
			B = Button(i, bgcolor="#808080", height=50, width=320, bgcolor_after_hover="#cacaca", on_click=self.navigate_to_page)
			page.add(B)
		
		page.update()
	
	def close (self, *args):
		self.page.close()
	
	def on_update (self, page):
		pass
	
	def navigate_to_page (self, btn):
		if btn.title == "Text":
			Navigate(self.page, [
				Text("Text is the basic control.", expand_width=True),
				Text("Blue color :)", color="blue")
			]).show()
