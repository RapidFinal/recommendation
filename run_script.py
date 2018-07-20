from firebase_data import firebase_fetch
from engine import learn


import threading

def printit():
  print("trainings...")
  firebase_fetch()
  learn()
  threading.Timer(7200.0, printit).start()

print("Starting...")
printit()
