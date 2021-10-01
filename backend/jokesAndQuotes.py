import slack
import json
import random
import time
import emoji
import ssl
import utils


def JokesAndQuotes():
    def Jokes(username_routine):
        with open('../data/jokes.json') as f:
            jokes = json.load(f)

        joke = random.choice(jokes)
        question = joke['question']
        answer = joke['answer']

        utils.send_message(username=username_routine, text=f"Question: {question}")
        time.sleep(2)
        utils.send_message(username=username_routine, text=f"Answer: {answer}")
        utils.send_message(username=username_routine, text=":rolling_on_the_floor_laughing:")

    def Quotes(username_routine):

        with open("../data/quotes.json") as f:
            quotes = json.load(f)

        quote_slip = random.choice(quotes)
        quote = quote_slip['text']
        author = quote_slip['author']

        utils.send_message(
            username=username_routine,
            text=f"Quote to get you through the day: \"{quote}\" \n by: {author}"
        )

    def react_jokes_quotes(username, timestamp):
        channel = utils.resolve_user(username)
        allowed_reactions = utils.get_allowed_reactions('jokesQuotes')

        response = utils.client.reactions_get(channel=channel, timestamp=timestamp)
        reactions = utils.get_all_reactions(response)

        is_ok = utils.check_reaction(username, reactions, allowed_reactions)
        if not is_ok:
            return

        reaction = reactions.pop()
        if reaction == 'dart':
            Quotes(utils.user)
        elif reaction == 'rolling_on_the_floor_laughing':
            Jokes(utils.user)

    ts = utils.send_message(
        username=utils.user,
        text="Hello! What would help brighten up your day? a quote or a joke today? " \
             f"React :dart: or :rolling_on_the_floor_laughing:"
    )
    time.sleep(10)

    react_jokes_quotes(username=utils.user,
                       timestamp=ts)
