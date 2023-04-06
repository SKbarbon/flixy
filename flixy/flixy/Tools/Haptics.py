import platform
import time
import ctypes #needed for workaround
import objc_util #used if workaround is unnecessary
from .sounds import Sound


workaround = True if platform.machine() == 'iPhone8,1' else False #iphone 6s is the first device with haptic engine and supports haptic feedback differently than newer models

#for workaround and vibration:
AudioServicesPlaySystemSound = ctypes.CDLL(None).AudioServicesPlaySystemSound
impactID, selectionID, notificationID, vibrateID = 1519, 1520, 1521, 4095

#if workaround is unnecessary:
objc_util.NSBundle.bundle(Path="/System/Library/Frameworks/UIKit.framework").load()
UIImpactFeedbackGenerator = objc_util.ObjCClass('UIImpactFeedbackGenerator').new()
UISelectionFeedbackGenerator = objc_util.ObjCClass('UISelectionFeedbackGenerator').new()
UINotificationFeedbackGenerator = objc_util.ObjCClass('UINotificationFeedbackGenerator').new()
	

def selectionChanged(workaround = workaround):
	if workaround:
		AudioServicesPlaySystemSound(selectionID)
	else: 
		#UISelectionFeedbackGenerator.prepare()
		UISelectionFeedbackGenerator.selectionChanged()
		
def impactOccured(workaround = workaround):
	if workaround:
		AudioServicesPlaySystemSound(impactID)
	else:
		#UIImpactFeedbackGenerator.prepare()
		UIImpactFeedbackGenerator.impactOccurred()
		
def notificationOccured(id = False, workaround = workaround): #3 different ids if workaround is not used
	if workaround or not id:
		AudioServicesPlaySystemSound(notificationID)
	else: 
		#UINotificationFeedbackGenerator.prepare()
		UINotificationFeedbackGenerator.notificationOccurred_(id)

def vibrate():
	AudioServicesPlaySystemSound(vibrateID)	
	


def single_haptic():
	Sound('ui:click5', volume=0.5).play()
	selectionChanged()



def impact_haptic():
	Sound('ui:switch11', volume=0.2).play()
	impactOccured()


def warning_haptic():
	for id in range(0, 3):
		Sound('ui:switch17', volume=0.3).play()
		notificationOccured(id)
		time.sleep(0.1)
