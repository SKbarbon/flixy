from ..flixy import *




class start_demo:
	
	def __init__(self):
		app(target=self.App)
	
	def App(self, page:Page):
		self.page = page
		page.appbar = AppBar(
			title = "Demo",
			btn_icon =  'iob:close_round_32'
		)
		
		Split_View = Row(expand_width=True, expand_height=True, bgcolor=None, scroll=False)
		page.add(Split_View)
	
	def close (self, *args):
		self.page.close()
