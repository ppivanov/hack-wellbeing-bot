import schedule
import jokesAndQuotes
# import morningRoutine
import stretchReminder
import time
import dailyReport
import waterReminder

# schedule.every(10).seconds.do(stretchReminder.streching)

# Morning Routine (Greeting, Sleep check, Challenge check, Daily challenge)
# schedule.every().day.at("09:00").do(morningRoutine.morningRoutine)  

# Morning Joke/Quotes
# schedule.every().day.at("10:00").do(jokesAndQuotes.JokesAndQuotes)

# Hourly Reminders
# schedule.every(3).seconds.do(waterReminder.waterReminder)  
# schedule.every().minute.at(":30").do(waterReminder)
# schedule.every().minute.at(":30").do(stretchReminder)

# Afternoon Joke/Quotes
# schedule.every().day.at("14:00").do(jokesAndQuotes)

# Report
# schedule.every().day.at("10:00").do(dailyReport)

# schedule.every(1).seconds.do(jokesAndQuotes.JokesAndQuotes)
# schedule.every(1).seconds.do(waterReminder.waterReminder)
schedule.every(1).seconds.do(dailyReport.dailyReport)

while True:
    schedule.run_pending()
    # time.sleep(10)
