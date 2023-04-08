def Get_parent(cls):
	return cls.parent

def Get_first_parent (cls):
	last_parent = get_parent(cls)
	while last_parent != cls.page:
		if get_parent(last_parent) == cls.page: break
		last_parent = get_parent(last_parent)
	
	return last_parent
