# reminding you to scratch every now and then
import json
import random
import utils
import slack


def streching():
    with open('../data/exercise.json') as f:
        exercise = json.load(f)

    exercise = random.choice(exercise)
    text = exercise['text']
    times = exercise['time']

    utils.send_message(utils.user,
                       "Hey it's about time for your stretching session! \n *Your task is:* \n {} \n *Duration:* {} sec \n Have fun! :muscle:".format(
                           text, times))
