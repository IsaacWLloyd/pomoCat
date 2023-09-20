from timer import Timer
import datetime
import time

#a class that represents a pomodoro session which consists of various break and focus timers of different types
class Pomodoro:
   #init with important data
   def __init__(self):
      self.timers = []
      self.timer = None
      self.score = 0
      self.datetime = datetime.datetime.now()
      self.datetime_dict = {"year" : self.datetime.year, 
                       "month" : self.datetime.month, 
                       "day" : self.datetime.day, 
                       "hour" : self.datetime.hour,
                       "minute" : self.datetime.minute,
                       "second" : self.datetime.second}

   #only one timer can be running at a time within a Pomodoro object
   
   #starts a new timer of a set duration in focus mode
   def start_focus(self, duration = 20*60):
      self.timer = Timer("focus", duration)
      self.timer.start()
   #starts a new timer of set duration in break mode
   def start_break(self, duration = 5*60):
      self.timer = Timer("break", duration)
      self.timer.start()
   #stops the current timer
   def stop(self):
      self.timer.stop()


   def get_remaining_time(self):
      return self.timer.get_remaining_time()

   #calculates the score of the current timer and adds it to the pomodoro score.
   def calculate_score(self, focus="average"):
      self.timer.set_focus(focus)
      self.score += self.timer.calculate_score()
      self.timers.append(self.timer)

      self.score = round(self.score)
      return self.score

