from firebase_data import firebase_fetch
from engine import learn


import threading

def printit():
  firebase_fetch()
  learn()
  threading.Timer(7200.0, printit).start()

printit()
