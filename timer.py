import time
import threading
import settings

#a class to store data for and run individual timers within a pomodoro session.
class Timer:
   #init with important data
   def __init__(self, type="break", duration = 5*60):
      self.duration = duration
      self.remaining = duration
      self.running = False
      self.timer_thread = None
      self.type = type
      self.focus = "average"
      self.score = 0
   
   #starts running and creates a thread to output time left repeatedly
   def start(self):
      self.running = True
      self.timer_thread = threading.Thread(target=self._run)
      self.timer_thread.start()

   #private thread method for outputing time left
   def _run(self):
      start_time = time.time()
      while self.running:
         self.remaining = self.duration - (time.time()-start_time)
         time.sleep(1)
   
   #stops running and deletes the thread
   def stop(self):
      self.running = False
      self.timer_thread.join()
   
   #calculates the score for itself based on type, time remaining, focus level, and scaling constants
   def calculate_score(self):
      self.remaining = round(self.remaining)
      if self.type == "focus":
         self.score += self.duration*settings.TIME_SCORE_MULTIPLIER
      
      if self.type == "break" and self.remaining < -settings.TIME_ALLOWANCE:
         self.score += self.remaining*settings.LONG_BREAK_MULTIPLIER*settings.TIME_SCORE_MULTIPLIER
      elif self.type == "focus" and self.remaining > settings.TIME_ALLOWANCE:
         self.score -= self.remaining*settings.SHORT_SESSION_MULTIPLIER*settings.TIME_SCORE_MULTIPLIER
      
      if self.score > 0:
         self.score*=settings.FOCUS_DICT[self.focus]

      return self.score
   
   def get_remaining_time(self):
      return round(self.remaining)

   def set_focus(self, focus):
      self.focus=focus