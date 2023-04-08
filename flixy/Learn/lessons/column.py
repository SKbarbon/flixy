from ...flixy import *



def column_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# Column", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("A control that accept sub-controls to show them vertically.", expand_width=True, text_align=0)
	v.add(t2)
	
	code1 = TextView("Column(expand_width=True, bgcolor='white')", expand_width=True, height=43)
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"scroll" : ["A bool value for scroll, if False the Column will not scroll if overFlow.", "Column(scroll=True)"],
		"auto_end_following" : ["A bool value, if True the Column will be animated to the last element.", "Column(auto_end_following=True)"],
		"width" : ["A number of the Column width.", "Column(width=200)"],
		"height" : ["The number of the Column's' height.'", "Column(height=50)"],
		"add(<control>)" : ["Add a sub-control to the Column.", "Column.add(myText)"],
		"clear()" : ["To clear the the Column from all controls", "Column.clear()"],
		"remove_control(<control>)" : ["Remove a control from the Column", "Column.remove_control(myText)"],
		"on_scroll" : ["Set a function to be called when the user scroll on the Column.", "Column.on_scroll = function"],
		"on_update" : ["Set a function to be called when the Column is updated.", "Column.on_update = function"],
		"offset" : ["A read-only propert returns a list that contain the scroll offset_x and offset_y", "offset = Column.offset"]
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
