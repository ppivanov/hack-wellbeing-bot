import schedule
import jokesAndQuotes
import morningRoutine
import time

schedule.every(10).seconds.do(morningRoutine.morningRoutine)  

# Morning Routine (Greeting, Sleep check, Challenge check, Daily challenge)
# schedule.every().day.at("09:00").do(morningRoutine.morningRoutine)  

# Morning Joke/Quotes
# schedule.every().day.at("10:00").do(jokesAndQuotes)

# Hourly Reminders
# schedule.every().minute.at(":30").do(waterReminder)
# schedule.every().minute.at(":30").do(stretchReminder)

# Afternoon Joke/Quotes
# schedule.every().day.at("14:00").do(jokesAndQuotes)

# Report
# schedule.every().day.at("10:00").do(dailyReport)
 
while True:
    schedule.run_pending()
    time.sleep(10)