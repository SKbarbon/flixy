from ...flixy import *



def page_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# Page", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("The main view that all sub-controls will be in.", expand_width=True, text_align=0)
	v.add(t2)
	
	code1 = TextView("""
from flixy import *
import flixy

def main(page:Page): # The page will be givin as an argument to the target.
	page.update() # After any changes to the page, you must update it to apple all changes

app(target=main)
	""", expand_width=True, height=250)
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"font_family" : ["The default font_family of all controls, Text or Button etc.", "page.font_family = 'Avenir'\npage.update()"],
		"bgcolor" : ["The background color of the page.", "page.bgcolor = 'white'"],
		"spacing" : ["The space padding number between sub-controls.", "page.spacing = 15\npage.update()"],
		"width" : ["Read-only property, the width of the page.", "width = page.width"],
		"height" : ["Read-only property, the height of the page", "height = page.height"],
		"touch_x" : ["Read-only property, the last finger touch position on X axis.", "touch_x = page.touch_x"],
		"touch_y" : ["Read-only property, the last finger touch position in Y axis.", "touch_y = page.touch_y"],
		"on_resize" : ["Set a function to be called when ever the page resized. best for iPad multi-task.", "page.on_resize = function"],
		"on_update" : ["Set a function to be called when ever the page is being updated", "page.on_update = function"],
		"on_hover" : ["Set a function to be called when ever the mouse cursor hovered the page. 'iPad only'", "page.on_hover = function"],
		"on_touch" : ["Set a function to be called when ever a finger touch the the page.", "page.on_touch = function"],
		"on_close" : ["Set a function to be called when the page is being closed.", "page.on_close = function"],
		"update()" : ["A function that will update and apply the page changes.", "page.update()"],
		"add(<control>)" : ["A function called to add a control to the page", "page.add(Text('Hi'))"],
		"clear()" : ["A function called to clear the page from all controls", "page.clear()"],
		"reposition_controls()" : ["A function called to reposition controls if there is any thing wrong", "page.reposition_controls()"],
		"remake_controls()" : ["A function called to remove then remake controls from scratch.", "page.remake_controls()"],
		"remove_control(<control>)" : ["A function called to remove a sub-control on the page directly.", "page.remove_control(myText)"],
		"close" : ["A function called to close the page.", "page.close()"]
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
