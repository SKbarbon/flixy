from ...flixy import *
import random

def on_typeing(cls):
	col = ['#ffffff', '#84afff', '#ff9595', '#bc23ff']
	cls.bgcolor = random.choice(col)
	cls.update()

def textfield_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# TextField", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("A control that accept user text input.", expand_width=True, text_align=0)
	v.add(t2)
	
	code1 = TextView("""
def on_typing(cls):
	col = ['#ffffff', '#84afff', '#ff9595', '#bc23ff']
	cls.bgcolor = random.choice(col)
	cls.update()
tf = TextField(expand_width=True, bgcolor='white')
tf.on_edit = on_typing
tf.update()
	""", expand_width=True, height=250)
	
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	
	tf_ex = TextField(placeholder="Type..", bgcolor="#ffffff")
	tf_ex.on_edit = on_typeing
	v.add(tf_ex)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"value" : ["A bool value for scroll, if False the Column will not scroll if overFlow.", "TextField(value='')"],
		"placeholder" : ["A string that will be shown if the TextField empty..", "TextField(placeholder='type..')"],
		"width" : ["A number of the TextField width.", "TextField(width=200)"],
		"height" : ["The number of the TextField height.'", "TextField(height=50)"],
		"text_color" : ["The text color of the textField", "TextField(text_color='black')"],
		"bgcolor" : ["The bgcolor of the TextField. it must be only #hex.", "TextField(bgcolr='#ffffff')"],
		"font_size" : ["The size of the font", "TextField.font_size = ''"],
		"opacity" : ["The opacity of the TextField from 0.0 to 1.0", "TextField.opacity = 1.0\nTextField.update()"],
		"selectable" : ["Bool value, if False the user will cant select the value.", "TextField.selectable = True"],
		"editable" : ["Bool value, if False the user will cant edit the TextField.", "TextField.editable = True"],
		"on_edit" : ["set a function to be called when ever the TextField being edited.", "TextField.on_edit = function"],
		"on_start_edit" : ["Set a function to be called when ever the the user start edit the TextField.", "TextField.on_edit_start = function"],
		"on_done_edit" : ["Set a function to be called when the user click enter and finish typing.", "TextField.on_done_edit = function"],
		"focus()" : ["A function that being called to focus on the TextField ans start typing", "TextField.focus()"],
		"stop()" : ["A function called to unfocus and stop typeing on the TextField.", "TextField.stop()"]
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
