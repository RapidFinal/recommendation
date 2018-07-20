from firebase_data import firebase_fetch
from engine import learn


import threading

def printit():
  threading.Timer(7200.0, printit).start()
  firebase_fetch()
  learn()

printit()
