from ..pythonista_ui.WKWEBVIEW import WKWebView
from ..Tools.action import do_action
from ..Tools.convert_rgb_to_hex import rgb2hex
import ui




class WebView (object):
	
	def __init__ (self, url="", width=250, height=250, border_radius=8, opacity=1.0, expand_width=False, expand_height=False, bgcolor=None, use_wkwebview=False):
		# actions
		self.on_load_start = None
		self.on_load_finish = None
		self.on_load_error = None
		# set
		try:
			if use_wkwebview:
				self.__self_ui = WKWebView(swipe_navigation=True)
				self.self_ui.delegate = WebViewDelegate(self)
				self.self_ui.load_url(url)
			else:
				self.__self_ui = ui.WebView(swipe_navigation=True)
				self.self_ui.delegate = WebViewDelegate(self)
				self.self_ui.load_url(url)
		except:
			self.__self_ui = ui.WebView(swipe_navigation=True)
			self.self_ui.delegate = WebViewDelegate(self)
			self.self_ui.load_url(url)
		
		self.parent = None
		self.page = None
		
		self.url = url
		self.width = width
		self.height = height
		self.border_radius = border_radius
		self.opacity = opacity
		self.expand_width = expand_width
		self.expand_height = expand_height
		self.bgcolor = bgcolor
		
		self.load_is_ended = False
		
		self.url = str(self.self_ui.evaluate_javascript("window.location.href"))
		self.update()
	
	
	def update (self):
		wv = self.self_ui
		
		
		try: current_url = str(wv.evaluate_javascript("window.location.href"))
		except: return False
		if self.url != str(wv.evaluate_javascript("window.location.href")):
			try: wv.load_url(self.url)
			except: pass
		
		wv.width = self.width
		wv.corner_radius = self.border_radius
		wv.height = self.height
		wv.alpha = self.opacity
		wv.bg_color = self.bgcolor
		
		if self.parent != None:
			if self.expand_width:
				self.__self_ui.width = self.parent.width
				self.width = self.__self_ui.width
			if self.expand_height:
				if self.page.appbar == None or self.page != self.parent:
					self.__self_ui.height = self.parent.height
					self.height = self.__self_ui.height
				else:
					self.__self_ui.height = self.parent.height - self.page.appbar.self_ui.height
					self.height = self.__self_ui.height
	
	def respown(self, parent, page):
		self.parent = parent
		self.page = page
		self.update()
	
	def remove_self (self):
		self.update()
		self.parent.update()
		self.parent.remove_control (self)
	
	def go_back (self):
		self.self_ui.go_back()
	
	def go_forward (self):
		self.self_ui.go_forward()
	
	def reload (self):
		self.self_ui.reload()
	
	def stop_load (self):
		self.self_ui.stop()
	
	def evaluate_javascript (self, js_code):
		return self.self_ui.evaluate_javascript(js_code)
	
	def load_url (self, url):
		self.self_ui.load_url(url)
		self.url = url
	
	@property
	def self_ui(self):
		return self.__self_ui


# delegate
class WebViewDelegate (object):
	def __init__ (self, self_class):
		self.self_class = self_class
	def webview_should_start_load(self, webview, url, nav_type):
		self.self_class.url = url
		self.self_class.load_is_ended = False
		return True
	def webview_did_start_load(self, webview):
		self.self_class.url = str(webview.evaluate_javascript("window.location.href"))
		do_action(self.self_class.on_load_start, [self.self_class])
		self.self_class.load_is_ended = False
	def webview_did_finish_load(self, webview):
		self.self_class.url = str(webview.evaluate_javascript("window.location.href"))
		self.self_class.load_is_ended = True
		do_action(self.self_class.on_load_finish, [self.self_class])
	def webview_did_fail_load(self, webview, error_code, error_msg):
		do_action(self.self_class.on_load_error, [self.self_class, error_code, error_msg])
