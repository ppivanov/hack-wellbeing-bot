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

def JokesAndQuotes(username_indv):

    def Jokes(username_routine):
        with open('../data/jokes.json') as f:
            jokes = json.load(f)

        joke = random.choice(jokes)
        question = joke['question']
        answer = joke['answer']

        utils.send_message(username = username_routine, text = f"Question: {question}" )
        time.sleep(2)
        utils.send_message(username= username_routine, text = f"Answer: {answer}")
        utils.send_message(username= username_routine, text=":rolling_on_the_floor_laughing:")

    def Quotes(username_routine):

        with open("../data/quotes.json") as f:
            quotes = json.load(f)
        
        quote_slip = random.choice(quotes)
        quote = quote_slip['text']
        author = quote_slip['author']

        utils.send_message(
                username = username_routine,
                text=f"Quote to get you through the day: \"{quote}\" \n by: {author}"
                )

    def react_jokes_quotes(username, timestamp):
        channel = utils.resolve_user(username)
        allowed_reactions = utils.get_allowed_reactions('jokesQuotes')

        response = utils.client.reactions_get(channel=channel, timestamp=timestamp)
        reactions = utils.get_all_reactions(response)

        utils.check_reaction(username, reactions, allowed_reactions)

        reaction = reactions.pop()
        if reaction == 'dart':
            Quotes(username_indv)
        elif reaction == 'rolling_on_the_floor_laughing':
            Jokes(username_indv)
    
    ts = utils.send_message(
    username = username_indv,
    text = "Hello! What would help you to get through your day successfully? a quote or a joke today? " \
                f"React :dart: or :rolling_on_the_floor_laughing:"
        )
    time.sleep(10)
    
    react_jokes_quotes(username = username_indv,
                        timestamp = ts)
 

#Just change here the name of the user for the testing!
JokesAndQuotes(username_indv="Josef Svec")

# for user in utils.users:
#     JokesAndQuotes(username_routine= user,)
