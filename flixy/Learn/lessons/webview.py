from ...flixy import *



def webview_lesson (v):
	v.clear()
	v.update()
	
	title = Text("# WebView", size=29, expand_width=True, height=50, text_align=0, bgcolor=None)
	v.add(title)
	
	t2 = Text("A control that show an external webpage.", expand_width=True, text_align=0)
	v.add(t2)
	
	code1 = TextView("WebView('https://example.com')", expand_width=True, height=43)
	code1.editable = False
	code1.selectable = True
	v.add(code1)
	
	t3 = Text("## Properties", expand_width=True, text_align=0, size=27, height=90)
	v.add(t3)
	
	props = {
		"url" : ["A string value of the url that will be loaded.", "WebView.url = 'https://example.com'; WebView.update()"],
		"width" : ["A number of the width.", "WebView.width = 200"],
		"height" : ["A number of the height", "WebView.height = 200"],
		"use_wkwebview" : ["Bool, if True it will use wkwebview. you can edit this onec", "WebView(use_wkwebview=True)"],
		"border_radius" : ["A number of the border radius.", "WebView.border_radius = 10"],
		"load_is_ended" : ["A read-only bool value, true if the current state of the current url if loaded.", "state = WebView.load_is_ended"],
		"go_back()" : ["A function called to go to previous url.", "WebView.go_back()"],
		"go_forward()" : ["A function called to go to recent url.", "WebView.go_forward()"],
		"reload()" : ["A function called to reload the current url.", "WebView.reload()"],
		"on_load_start" : ["Set a function to call when WebView is load a url.", "WebView.on_load_start = function"],
		"on_load_finish" : ["Set a function to call when WebView is finish loading a url.", "WebView.on_load_finish = function"],
		"on_load_error" : ["Set a function to call when WebView having error while downloading.", "WebView.on_load_error = function"]
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
