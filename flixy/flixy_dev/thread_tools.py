import ctypes
import threading
import time

def _async_raise(tid, exctype):
    """Raise an exception in the threads with id tid"""
    if not isinstance(exctype, type):
        raise TypeError("Only exception types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("Invalid thread ID")
    elif res > 1:
        # If it returns >1, undo the call or it may corrupt the interpreter
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    if thread is None:
        return
    if not thread.is_alive() or thread.ident is None:
        return
    try:
        _async_raise(thread.ident, SystemExit)
    except ValueError:
        # Thread already dead or invalid
        pass
