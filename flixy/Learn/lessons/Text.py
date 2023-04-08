from ...flixy import *



def text_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# Text", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("This is an example code of simple Text:", expand_width=True, text_align=0)
	v.add(t2)
	
	code1 = TextView("Text('Hello, world!')", expand_width=True, height=43)
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"value" : ["The value of the text.", "Text(value='Hi')"],
		"bgcolor" : ["The background color of the text.", "Text('Hi', bgcolor='black')"],
		"color" : ["The color of the text.", "Text('Hi', color='white')"],
		"font_family" : ["The font of the text. it will set automaticly as the page.font_family.", "Text('Hi', font_family='Avenir')"],
		"text_align" : ["The alignment of text. 0 as left, 1 as center, 2 as right.", "Text('Hi', text_align=1)"],
		"size" : ["The size of the text as a number.", "Text('Hi', size=18)"]
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
