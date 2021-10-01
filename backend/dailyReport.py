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
    utils.send_message(utils.user, f"You had {n_cups} cups in total and slept for {n_hours} hours last night.")
    utils.send_message(utils.user, "Enjoy your evening and see you tomorrow :zzz:")
