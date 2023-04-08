from ...flixy import *



def navigate_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# Navigate", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("A router that allow you to navigate to a second sub-page.", expand_width=True, text_align=0)
	v.add(t2)
	
	nv_ex = Navigate(v.page, controls=[
		Text("I am on the second page!", expand_width=True)
	])
	
	show_sheet_btn = Button("Navigate example", bgcolor=None, title_color="#80acff", on_click=nv_ex.show, bgcolor_after_hover='#3d3d3d')
	v.add(show_sheet_btn)
	
	code1 = TextView("""
from flixy import *
import flixy

def main(page:Page):
	n = Navigate(page, controls=[
		Text("I am on the new page.")	
	])

flixy.app(target=main)
# swip to right to go back or click '< Back' to go back.
	""", expand_width=True, height=330)
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"page" : ["Give it the main page class.", "Navigate(page=page)"],
		"controls" : ["The sub-controls that will be added to the new page.", "Navigate.add(myText)"],
		"show" : ["A function called to show the sheet", "Navigate.show()"],
		"hide" : ["A function called to hide the sheet.", "Navigate.hide()"],
		"on_back" : ["Set a function to be called when the user back to the original page.", "Navigate.on_back = function"]
	}
	
	for i in props:
		describe = props[i][0]
		code_ex = props[i][1]
		n = Text(i, size=23, expand_width=Text, text_align=0)
		de = Text(describe, text_align=0, expand_width=True)
		cx = TextView(code_ex, expand_width=True, height=50)
		cx.editable = False
		cx.selectable = True
		v.add(n)
		v.add(de)
		v.add(cx)
		v.add(Text(""))
