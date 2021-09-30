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
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero'
    }
}


def resolve_user(username):
    response = client.conversations_open(users=[users[username]])
    return response.data['channel']['id']


# def send_joke(username):
#     channel = resolve_user(username)
#
#     ts1 = client.chat_postMessage(channel=channel, text=question).data['ts']
#     time.sleep(5)
#     ts2 = client.chat_postMessage(channel=channel, text=answer).data['ts']
#     ts3 = client.chat_postMessage(channel=channel, text=emoji.emojize(':rolling_on_the_floor_laughing:')).data['ts']
#     return ts1, ts2, ts3


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


def get_reactions(username, timestamps, discipline):
    channel = resolve_user(username)
    allowed_reactions = get_allowed_reactions(discipline)

    for ts in timestamps:
        response = client.reactions_get(channel=channel, timestamp=ts)
        reactions = get_all_reactions(response)

        if any(reaction not in allowed_reactions for reaction in reactions):
            send_message(username,
                         f"Sorry :cry:, I don't understand this emoji! {', '.join(f':{reaction}:' for reaction in reactions if reaction not in allowed_reactions)}")
        elif any(reaction in {'five', 'six', 'seven', 'eight', 'nine'} for reaction in reactions):
            send_message(username, "Haha, very funny :angry:. Why don't I believe you? :thinking_face:")
        elif any(reaction == 'zero' for reaction in reactions):
            send_message(username, "You should change it immediately! :eyes:")
        else:
            send_message(username, "Good job! :clap:")


if __name__ == '__main__':
    # timestamps = send_joke('Martin Korytak')
    timestamp = send_message('Martin Korytak', 'did you drink anything in last hour?')
    time.sleep(20)
    get_reactions('Martin Korytak', [timestamp], 'waterReminder')
