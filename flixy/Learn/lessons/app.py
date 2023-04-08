from ...flixy import *



def app_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# app", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("The main class that will run the flixy UI.", expand_width=True, text_align=0)
	v.add(t2)
	
	code1 = TextView("""
from flixy import *
import flixy
	
def main(page:flixy.Page):
	pass
	
app(target=main) # The app class
	""", expand_width=True, height=250)
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"target" : ["The main function that will be called to serve.", "app(target=function)"],
		"develop" : ["Default is true, this will make actions on background like check for library updates.", "app(function, develop=True)"]
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
