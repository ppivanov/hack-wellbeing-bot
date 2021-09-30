import slack
import json
import random
import time
import emoji
from pathlib import Path
from dotenv import load_dotenv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def morningRoutine():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    with open('../data/challenges.json') as file:
        challenges = json.load(file)
    with open('../data/greetings.json') as file:
        greetings = json.load(file)

    morningGreeting = random.choice(greetings)
    challenge = random.choice(challenges)

    client = slack.WebClient('xoxb-2535729735287-2574128624896-GL5JKsUH9q6u7exZSGrtJibT')

    users = {
        "Martin Korytak": "U02GW2LF472",
        "Tom Callaghan": "U02G6DM24KU",
        "Pavel Ivanov": "U02FZM0QG3Y",
        "Dennis Dimov": "U02GW22S76U",
        "Josef Svec": "U02G6DGQ0LA"
    }

    sleepPrompt = 'How many hours of sleep did you get last night?\n0-4 (:headstone:)\n5-6 (:yawning_face:)\n7-8 (:laughing:)\n9+ (:sloth:)'
    challengePrompt = 'Did you complete yesterday\'s daily challenge? :thumbsup:/:thumbsdown:\n_Use reactions below to respond..._'

    for i in users.values():
        response = client.conversations_open(users=[i])
        channel = response.data['channel']['id']
        client.chat_postMessage(channel=channel, text=emoji.emojize(morningGreeting["text"]))

        client.chat_postMessage(channel=channel, text=emoji.emojize(sleepPrompt))
        client.chat_postMessage(channel=channel, text=emoji.emojize(challengePrompt))
        
        client.chat_postMessage(channel=channel, text=emoji.emojize(f'Daily challenge: {challenge["text"]}'))

