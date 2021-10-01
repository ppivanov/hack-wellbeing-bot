import time

import slack
import emoji
import utils
from datetime import datetime


def waterReminder():
    now = datetime.now()
    currTime = '10:30'#str(now.hour) + ":" + str(now.minute)

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

    if currTime in waterDic:
        waterAmount = waterDic.get(currTime)
    else:
        waterAmount = 0

    utils.send_message(utils.user, "{} Gentle Reminder {}\n Don't forget to drink water!{} At this point of the day, you should have drank approx {}L."
            .format(emoji.emojize(':bell:'), emoji.emojize(':bell:'), emoji.emojize(':potable_water:'),
                    waterAmount))

    ts = utils.send_message(utils.user, "How much water have you drank in the last hour? \n\n {} 0-0.5 Cup\n\n {} 0.5-1 Cup(s)\n\n {} 1.0-1.5 Cup(s)\n\n {} 1.5+ Cup(s)"
            .format(':non-potable_water:', ':droplet:', ':potable_water:', ':ocean:'))

    time.sleep(10)
    utils.react_water_challenge(utils.user, ts)
