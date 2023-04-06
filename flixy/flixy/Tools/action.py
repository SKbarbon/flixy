import threading


def do_action(function, args=[]):
	if function == None: return
	threading.Thread(target=function, args=args, daemon=True).start()
