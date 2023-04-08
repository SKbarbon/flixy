from ...flixy import *



def button_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# Button", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("A clickable control for doing actions per click.", expand_width=True, text_align=0)
	v.add(t2)
	
	code1 = TextView("Button('click me!')", expand_width=True, height=50)
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"title" : ["The text of that the button will show.", "Button(title='click me!')"],
		"bgcolor" : ["The background color of the button.", "Button('click me', bgcolor='white')"],
		"title_color" : ["The color of the button's text.", "Button('click me', title_color='black')"],
		"bgcolor_after_hover" : ["The bgcolor after the mouse cursor hover the button. iPad only", "Button(bgcolor_after_hover='gray')"],
		"width" : ["The width of the button", "Button('click', width=250)"],
		"height" : ["The height of the button", "Button('click', height=50)"],
		"border_radius" : ["The border radius of the button", "Button('click', border_radius=10)"],
		"font_size" : ["The size of the button's text'", "Button('click', font_size=18)"],
		"font_family" : ["The font of the button", "Button('click', font_family='')"],
		"opacity" : ["The opacity of the button from 0.0 to 1.0", "Button('click', opacity=1.0)"],
		"expand_width" : ["A bool value, if True the button will expand the parent width.", "Button(expand_width=True)"],
		"expand_height" : ["A bool value, if True the button will expand the parent height.", "Button(expand_height=True)"],
		"on_click" : ["Set a function to be called when ever the button clicked", "Button.on_click = function"],
		"on_hover" : ["Set a function to be called when ever mouse cursor hoverd the button.", "Button.on_hover = function"]
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
