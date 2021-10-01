# reminding you to scratch every now and then
import json
import random
import time
import emoji
import slack
import ssl
from pathlib import Path
from time import sleep
ssl._create_default_https_context = ssl._create_unverified_context


def streching():
    with open('./data/exercise.json') as f:
        exercise = json.load(f)

    exercise = random.choice(exercise)
    text = exercise['text']
    times = exercise['time']

    client = slack.WebClient('xoxb-2535729735287-2574128624896-GL5JKsUH9q6u7exZSGrtJibT')

    users = {
        #"Martin Korytak": "U02GW2LF472",
        #"Tom Callaghan": "U02G6DM24KU",
        #"Pavel Ivanov": "U02FZM0QG3Y",
        "Dennis Dimov": "U02GW22S76U",
        #"Josef Svec": "U02G6DGQ0LA"
    }

    for i in users.values():
        response = client.conversations_open(users=[i])
        channel = response.data['channel']['id']

        client.chat_postMessage(channel=channel, text="Hey it's about time for your stretching session! \n *Your task is:* \n {} \n *Duration:* {} sec \n Have fun! :muscle:".format(text, times))