import schedule
import jokesAndQuotes
import morningroutine
import stretchReminder
import dailyReport
import waterReminder

# # Morning Routine (Greeting, Sleep check, Challenge check, Daily challenge)
# schedule.every().day.at("09:00").do(morningroutine.morning_routine)
#
# # Morning Joke/Quotes
# schedule.every().day.at("10:00").do(jokesAndQuotes.JokesAndQuotes)
#
# # Hourly Reminders
# schedule.every().minute.at(":30").do(waterReminder.waterReminder)
# schedule.every().minute.at(":30").do(stretchReminder.streching)
#
# # Afternoon Joke/Quotes
# schedule.every().day.at("14:00").do(jokesAndQuotes.JokesAndQuotes)
#
# # Report
# schedule.every().day.at("17:00").do(dailyReport)


# schedule.every(1).seconds.do(morningroutine.morning_routine)
# schedule.every(1).seconds.do(jokesAndQuotes.JokesAndQuotes)
# schedule.every(1).seconds.do(stretchReminder.streching)
# schedule.every(1).seconds.do(waterReminder.waterReminder)
# schedule.every(1).seconds.do(dailyReport.dailyReport)

while True:
    schedule.run_pending()
