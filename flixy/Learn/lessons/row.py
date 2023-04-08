from ...flixy import *



def row_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# Row", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("A control that accept sub-controls to show them horizontally.", expand_width=True, text_align=0)
	v.add(t2)
	
	code1 = TextView("Row(expand_width=True, bgcolor='white')", expand_width=True, height=43)
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"scroll" : ["A bool value for scroll, if False the Row will not scroll if overFlow.", "Row(scroll=True)"],
		"auto_end_following" : ["A bool value, if True the Row will be animated to the last element.", "Row(auto_end_following=True)"],
		"width" : ["A number of the Row width.", "Row(width=200)"],
		"height" : ["The number of the row's height.'", "Row(height=50)"],
		"add(<control>)" : ["Add a sub-control to the row.", "Row.add(myText)"],
		"clear()" : ["To clear the the Row from all controls", "Row.clear()"],
		"remove_control(<control>)" : ["Remove a control from the row", "Row.remove_control(myText)"],
		"on_scroll" : ["Set a function to be called when the user scroll on the row.", "Row.on_scroll = function"],
		"on_update" : ["Set a function to be called when the Row is updated.", "Row.on_update = function"],
		"offset" : ["A read-only propert returns a list that contain the scroll offset_x and offset_y", "offset = Row.offset"]
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
