import slack
import time

client = slack.WebClient('xoxb-2535729735287-2574128624896-GL5JKsUH9q6u7exZSGrtJibT')

users = {
    "Martin Korytak": "U02GW2LF472",
    "Tom Callaghan": "U02G6DM24KU",
    "Pavel Ivanov": "U02FZM0QG3Y",
    "Dennis Dimov": "U02GW22S76U",
    "Josef Svec": "U02G6DGQ0LA"
}

allowed_emojis = {
    'waterReminder': {
        'non-potable_water', 'droplet', 'potable_water', 'ocean'
    },
    'jokesQuotes': {
        'dart', 'rolling_on_the_floor_laughing'
    },
    'hoursOfSleep': {'headstone', 'yawning_face', 'laughing', 'sloth'},
    'challengeCompletion': {'thumbsup', 'thumbsdown'}
}


def resolve_user(username):
    response = client.conversations_open(users=[users[username]])
    return response.data['channel']['id']


def send_message(username, text):
    channel = resolve_user(username)
    return client.chat_postMessage(channel=channel, text=text).data['ts']


def get_all_reactions(response):
    unique_reactions = set()
    try:
        for reaction in response.data['message']['reactions']:
            unique_reactions.add(reaction['name'])
    except KeyError:
        print('No reaction provided.')
    return unique_reactions


def get_allowed_reactions(discipline):
    return allowed_emojis[discipline]


def check_reaction(username, reactions, allowed_reactions):
    if not reactions:
        send_message(username, "HealthyBot is sad because you haven't responded yet. :cry:")
    elif len(reactions) > 1:
        send_message(username, 'Please react only with a single emoji!')
    elif any(reaction not in allowed_reactions for reaction in reactions):
        send_message(username,
                     f"Sorry :cry:, I don't understand this emoji! {', '.join(f':{reaction}:' for reaction in reactions if reaction not in allowed_reactions)}")


def react_water_challenge(username, timestamp):
    channel = resolve_user(username)
    allowed_reactions = get_allowed_reactions('waterReminder')

    response = client.reactions_get(channel=channel, timestamp=timestamp)
    reactions = get_all_reactions(response)

    check_reaction(username, reactions, allowed_reactions)

    reaction = reactions.pop()
    if reaction == 'ocean':
        send_message(username, "Please, don't get drowned! :pray:")
    elif any(reaction == 'non-potable_water' for reaction in reactions):
        send_message(username, "You should change it immediately! :eyes:")
    else:
        send_message(username, "Good job! :clap:")


def react_jokes_quotes(username, timestamp):
    channel = resolve_user(username)
    allowed_reactions = get_allowed_reactions('jokesQuotes')

    response = client.reactions_get(channel=channel, timestamp=timestamp)
    reactions = get_all_reactions(response)

    check_reaction(username, reactions, allowed_reactions)

    reaction = reactions.pop()
    if reaction == ':dart:':
        Quotes()
    elif reaction == ':rolling_on_the_floor_laughing:':
        Jokes()


if __name__ == '__main__':
    # timestamps = send_joke('Martin Korytak')
    while True:
        timestamp = send_message('Martin Korytak', 'did you drink anything in last hour?')
        time.sleep(5)
        react_water_challenge('Martin Korytak', timestamp)
