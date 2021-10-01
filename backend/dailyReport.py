import utils
import json


def select_user_data(data):
    for item in data:
        if item['user'] == utils.user:
            return item


def dailyReport():
    with open("../data/database.json") as f:
        data = json.load(f)['data']

    user_data = select_user_data(data)
    n_cups = user_data['n_cups']
    n_hours = user_data['n_hours']

    utils.send_message(utils.user, f"Your Health Report :droplet:\n"
                                   f"----------------------------------------------------\n"
                                   f"Water Intake: {n_cups} cups\nSleep: {n_hours} hours\n"
                                   f"Great work on improving your wellbeing! :battery:\n"
                                   f"----------------------------------------------------")

