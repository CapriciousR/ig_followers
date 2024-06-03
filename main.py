from instaFollower import InstaFollower
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv())

SIMILIAR_ACCOUNT = os.getenv('similiar_acc')
USERNAME = os.getenv('ig_username')
PASSWORD = os.getenv('ig_password')

ig_bot = InstaFollower()
time.sleep(4)
ig_bot.login(username=USERNAME, password=PASSWORD)
time.sleep(2)
ig_bot.find_followers(SIMILIAR_ACCOUNT)

