import slack
import json
import random
import time
import emoji
import ssl
import utils
ssl._create_default_https_context = ssl._create_unverified_context



# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)
def JokesAndQuotes(username_routine):

    # client = slack.WebClient('xoxb-2535729735287-2574128624896-GL5JKsUH9q6u7exZSGrtJibT')
    # response = client.conversations_open(users= "U02G6DGQ0LA") #Do not forgot to authomate this
    # channel = response.data['channel']['id']
    ts = utils.send_message(
        username = username_routine,
        text = "Hello!"
    )
    def Choosing():
        utils.send_message(
            username=username_routine, 
            text="Do you fell like a quote or a joke today? " \
                f"React :dart: or :rolling_on_the_floor_laughing:"
            )
        emoji = utils.get_reactions(username = username_routine, 
                                    timestamps=[ts],
                                    discipline="")

        #this is a temporary solution
        # if emoji == ':dart:':
        #     Quotes()
        # elif emoji == ':rolling_on_the_floor_laughing:':
        #     Jokes()
        # else:
        #     send("Sorry, you did not indicate your choice clearly." \
        #         "\n Let me ask you again.")
    def react_jokes_quotes(username, timestamp):
    channel = utils.resolve_user(username)
    allowed_reactions = utils.get_allowed_reactions('jokesQuotes')

    response = client.reactions_get(channel=channel, timestamp=timestamp)
    reactions = utils.get_all_reactions(response)

    utils.check_reaction(username, reactions, allowed_reactions)

    reaction = reactions.pop()
    if reaction == ':dart:':
        Quotes()
    elif reaction == ':rolling_on_the_floor_laughing:':
        Jokes()         


    def Jokes():
        with open('../data/jokes.json') as f:
            jokes = json.load(f)

        joke = random.choice(jokes)
        question = joke['question']
        answer = joke['answer']

        for i in users.values():
            response = client.conversations_open(users=[i])
            channel = response.data['channel']['id']

            client.chat_postMessage(channel=channel, text="Question: {}".format(question))
            time.sleep(2)
            client.chat_postMessage(channel=channel, text="Answer: {}".format(answer))
            client.chat_postMessage(channel=channel, text=emoji.emojize(':rolling_on_the_floor_laughing:'))

    def Quotes(username_routine):

        with open("../data/quotes.json") as f:
            quotes = json.load(f)
        
        quote_slip = random.choice(quotes)
        quote = quote_slip['text']
        author = quote_slip['author']

        # client = slack.WebClient('xoxb-2535729735287-2574128624896-GL5JKsUH9q6u7exZSGrtJibT')
        response = client.conversations_open(users= "U02G6DGQ0LA") #Do not forgot to authomate this
        channel = response.data['channel']['id']

        utils.send_message(
            username = username_routine,
            text=f"Quote to get you through the day: \"{quote}\" \n by: {author}"
            )



# JokesAndQuotes()

for k in utils.users:
    print(k)