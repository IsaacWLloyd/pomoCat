from pomodoro import Pomodoro
import csv
import datetime
import settings
import os

#writes the data from all timers within a pomodoro object to the current day file
# will create file if does not exist and initiliaze with a top row that describes data
# if the file does not exist it will also call the function to write yesterdays data to the month file
def write_pom_to_day(pom):

   data = []
   #first line to describe data
   format = ["type", "duration", "time remaining", "score", "focus level"]
   #loops through the pomodoros list of timers that have run and adds a list of their data to data[]
   for timer in pom.timers:
      data.append([timer.type, timer.duration, timer.remaining, 
                   timer.score, timer.focus])
   #string format for todays date using the datetime module
   today = str(datetime.datetime.now().month) + "_" + str(datetime.datetime.now().day) + "_" + str(datetime.datetime.now().year)
   # if this is the first time using today add yesterdays data to the monthly file
   # and then create todays file with the data format at the top
   if not os.path.exists(settings.DAILY_FOLDER_PATH+today+".csv"):
      write_yesterday_to_month()
      with open(settings.DAILY_FOLDER_PATH+today+".csv","a",newline="") as file:
         writer =csv.writer(file)
         writer.writerow(format)
   #adds the pomodoros data to the daily file
   with open(settings.DAILY_FOLDER_PATH+today+".csv","a",newline="") as file:
      writer = csv.writer(file)
      writer.writerows(data)

#takes yesterdays data and calculates relevent data to add to the month
def write_yesterday_to_month():
   # string formats for yesterdays date
   yesterday_datetime = datetime.datetime.now() - datetime.timedelta(days=1)
   yesterday = str(yesterday_datetime.month) + "_" + str(yesterday_datetime.day) + "_" + str(yesterday_datetime.year)
   yesterday_month = str(yesterday_datetime.month) + "_" + str(yesterday_datetime.year)
   yesterday_data = []
   #top line for month file
   format = ["date", "score", "seconds focused"]
   #if yesterday's file exists read its data tp yesterday_data[]
   if os.path.exists(settings.DAILY_FOLDER_PATH+yesterday+".csv"):     
      with open(settings.DAILY_FOLDER_PATH+yesterday+".csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
               yesterday_data.append(row)
   #loops through yesterdays data and calculates the total score and time focused
   yesterday_score = 0
   yesterday_focus_time = 0
   for list in yesterday_data:
      yesterday_score+=round(float(list[3]))
      if list[0] == "focus":
         yesterday_focus_time+=round(float(list[1])-float(list[2]))
   #if the month file doesnt exist, put the format line up top
   if not os.path.exists(settings.MONTHS_FOLDER_PATH+yesterday_month+".csv"):
      with open(settings.MONTHS_FOLDER_PATH+yesterday_month+".csv","a",newline="") as file:
         writer = csv.writer(file)
         writer.writerow(format)
   #write yesterdays data to the monthly file
   with open(settings.MONTHS_FOLDER_PATH+yesterday_month+".csv","a",newline="") as file:
      writer = csv.writer(file)
      writer.writerow([yesterday, yesterday_score, yesterday_focus_time])

#prints out yesterdays data using the relevant CLI command    
def view_day():
   filepath = settings.DAILY_FOLDER_PATH+str(datetime.datetime.now().month) + "_" + str(datetime.datetime.now().day) + "_" + str(datetime.datetime.now().year)+".csv"
   if os.name == 'nt':  # Windows
      os.system('type ' + filepath)
   else:  # Unix
      os.system('cat ' + filepath)





  

