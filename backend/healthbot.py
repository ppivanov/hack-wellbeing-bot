import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient('xoxb-2535729735287-2574128624896-GL5JKsUH9q6u7exZSGrtJibT')
client.chat_postMessage(channel='#botter', text='Hello!')

