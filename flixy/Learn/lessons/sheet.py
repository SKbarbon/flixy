from ...flixy import *



def sheet_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# Sheet", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("A on-top control can show a small page on top of the main page.", expand_width=True, text_align=0)
	v.add(t2)
	
	sh_ex = Sheet(show=False)
	v.page.add(sh_ex)
	sh_ex.add(Text("I am on the sheet!", bgcolor="white", expand_width=True, color="black"))
	
	show_sheet_btn = Button("show example sheet", bgcolor=None, title_color="#80acff", on_click=sh_ex.show, bgcolor_after_hover='#3d3d3d')
	v.add(show_sheet_btn)
	
	code1 = TextView("Sheet(bgcolor='white', border_radius=10)", expand_width=True, height=43)
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"bgcolor" : ["The background color of the sheet", "Sheet.bgcolor = 'white'"],
		"add(<control>)" : ["A function called to a sub-control on the Sheet.", "Sheet.add(myText)"],
		"show" : ["A function called to show the sheet", "Sheet.show()"],
		"hide" : ["A function called to hide the sheet.", "Sheet.hide()"],
		"remove_self" : ["A function called to delete the sheet.", "Sheet.remove_self()"]
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
