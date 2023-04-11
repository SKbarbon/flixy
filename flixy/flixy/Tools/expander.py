



def expand_control (cls):
	# set the expand
	if cls.parent != None:
		if cls.expand_width:
			cls.self_ui.width = cls.parent.width
			cls.width = cls.self_ui.width
		if cls.expand_height:
			if cls.page.appbar == None or cls.page != cls.parent:
				cls.self_ui.height = cls.parent.height
				cls.height = cls.self_ui.height
			else:
				cls.self_ui.height = cls.parent.height - cls.page.appbar.self_ui.height
				cls.height = cls.self_ui.height
