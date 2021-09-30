import slack
import emoji
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from datetime import datetime

def waterReminder():
    client = slack.WebClient('xoxb-2535729735287-2574128624896-GL5JKsUH9q6u7exZSGrtJibT')
    now = datetime.now()
    currTime = str(now.hour) + ":" + str(now.minute)

    users = {
        # "Martin Korytak": "U02GW2LF472",
        "Tom Callaghan": "U02G6DM24KU",
        # "Pavel Ivanov": "U02FZM0QG3Y",
        # "Dennis Dimov": "U02GW22S76U",
        # "Josef Svec": "U02G6DGQ0LA"
    }

    waterDic = {
        "10:30": "0.25",
        "11:30": "0.50",
        "12:30": "0.75",
        "13:30": "1.00",
        "14:30": "1.25",
        "15:30": "1.50",
        "16:30": "1.75",
        "17:30": "2.00",
    }

    print(currTime)
    if currTime in waterDic:
        waterAmount = waterDic.get(currTime)
    else: 
        waterAmount = 0

    for i in users.values():
        response = client.conversations_open(users=[i])
        channel = response.data['channel']['id']

        ts = client.chat_postMessage(
            channel=channel, 
            text="{} Gentle Reminder {}\n Don't forget to drink water!{} At this point of the day, you should have drank approx {}L."
            .format(emoji.emojize(':bell:'), emoji.emojize(':bell:'), emoji.emojize(':potable_water:'), waterAmount)).data['ts']

        ts1 = client.chat_postMessage(
            channel=channel, 
            text="How much water have you drank in the last hour? \n\n {} 0-0.5 Cup\n\n {} 0.5-1 Cup(s)\n\n {} 1.0-1.5 Cup(s)\n\n {} 1.5+ Cup(s)"
            .format(':non-potable_water:',':droplet:',':potable_water:',':ocean:'))