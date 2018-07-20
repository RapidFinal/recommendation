from firebase_data import firebase_fetch
from engine import learn
import time

print("Starting...")

while True:
  print("trainings...")
  firebase_fetch()
  learn()
  time.sleep(7200)
