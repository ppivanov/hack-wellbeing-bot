import schedule
import jokesAndQuotes
import morningroutine
import stretchReminder
import dailyReport
import waterReminder
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

# Morning Routine (Greeting, Sleep check, Challenge check, Daily challenge)
schedule.every().day.at("09:00").do(morningroutine.morning_routine)

# Morning Joke/Quotes
schedule.every().day.at("10:00").do(jokesAndQuotes.JokesAndQuotes)

# Hourly Reminders
schedule.every().minute.at(":30").do(waterReminder.waterReminder)
schedule.every().minute.at(":30").do(stretchReminder.streching)

# Afternoon Joke/Quotes
schedule.every().day.at("14:00").do(jokesAndQuotes.JokesAndQuotes)

# Report
schedule.every().day.at("17:00").do(dailyReport)

while True:
    schedule.run_pending()
    
