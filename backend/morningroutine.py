from types import resolve_bases
import slack
import json
import random
import time
import utils


def random_object_from_file(filepath):
    with open(filepath) as file:
        obj = json.load(file)
    return random.choice(obj)


def send_sleep_promt(username):
    sleep_prompt = 'How many hours of sleep did you get last night?\n0-4 (:headstone:)\n5-6 (:yawning_face:)\n7-8 (:laughing:)\n9+ (:sloth:)'
    sleep_ts = utils.send_message(username, text=sleep_prompt)
    time.sleep(15)
    utils.react_sleep_routine(username, timestamp=sleep_ts)


def send_challenge_prompt(username):
    challenge_prompt = 'Did you complete yesterday\'s daily challenge? :thumbsup:/:thumbsdown:'
    challenge_ts = utils.send_message(username, text=challenge_prompt)
    time.sleep(15)
    utils.react_daily_challenge(username, timestamp=challenge_ts)


def send_morning_prompts(username):
    send_sleep_promt(username)
    send_challenge_prompt(username)


def morning_routine():
    morning_greeting = random_object_from_file('../data/greetings.json')['text']
    challenge = random_object_from_file('../data/challenges.json')['text']

    utils.send_message(utils.user, text=morning_greeting)
    send_morning_prompts(utils.user)
    utils.send_message(utils.user, text=f'Daily challenge: {challenge}')
