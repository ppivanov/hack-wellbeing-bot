import slack
import json
import random
import time
import emoji
from pathlib import Path
from dotenv import load_dotenv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

def jokesAndQuotes():
    with open('../data/jokes.json') as f:
        jokes = json.load(f)

    joke = random.choice(jokes)
    question = joke['question']
    answer = joke['answer']

    client = slack.WebClient('xoxb-2535729735287-2574128624896-GL5JKsUH9q6u7exZSGrtJibT')

    users = {
        "Martin Korytak": "U02GW2LF472",
        "Tom Callaghan": "U02G6DM24KU",
        "Pavel Ivanov": "U02FZM0QG3Y",
        "Dennis Dimov": "U02GW22S76U",
        "Josef Svec": "U02G6DGQ0LA"
    }

    for i in users.values():
        response = client.conversations_open(users=[i])
        channel = response.data['channel']['id']

        client.chat_postMessage(channel=channel, text="Question: {}".format(question))
        time.sleep(2)
        client.chat_postMessage(channel=channel, text="Answer: {}".format(answer))
        client.chat_postMessage(channel=channel, text=emoji.emojize(':rolling_on_the_floor_laughing:'))
