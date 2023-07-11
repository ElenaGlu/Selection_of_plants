import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DJANGO_KEY_USER = os.getenv('DJANGO_KEY_USER')

KEY_NAME = os.getenv('KEY_NAME')
KEY_USER = os.getenv('KEY_USER')
KEY_PASSWORD = os.getenv('KEY_PASSWORD')
KEY_HOST = os.getenv('KEY_HOST')
KEY_PORT = os.getenv('KEY_PORT')
