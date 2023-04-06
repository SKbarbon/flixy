import sound
import threading
import time



class Sound (object):
	__player = None
	
	# actions
	on_finish = None
	on_click_play = None
	on_click_stop = None
	on_click_pause = None
	
	def __init__(self, name, volume=1.0, on_finish=None, on_click_play = None, on_click_stop = None, on_click_pause = None):
		def run_at_end():
			if self.on_finish == None: return
			threading.Thread(target=self.on_finish, args=[self]).start()
		
		self.__player = sound.Player(name)
		self.__player.stop()
		self.__player.finished_handler = run_at_end
		self.__player.volume = volume
		
		self.name = name
		self.on_finish = on_finish
		self.on_click_pause = on_click_pause
		self.on_click_play = on_click_play
		self.on_click_stop = on_click_stop
	
	
	def play(self):
		self.__player.play()
		if self.on_click_play != None:
			threading.Thread(target=self.on_click_play, daemon=True).start()
	
	def pause(self):
		self.__player.pause()
		if self.on_click_pause != None:
			threading.Thread(target=self.on_click_pause, daemon=True).start()
	
	def current_time(self, new=None):
		if new == None:
			return float(self.__player.current_time)
		else:
			self.__player.current_time = new
			return float(self.__player.current_time)
	
	def get_full_time(self):
		return float(self.__player.duration)
	
	def is_still_playing(self):
		return self.__player.playing
