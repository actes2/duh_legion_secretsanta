import sys
import logging
from dotenv import load_dotenv

load_dotenv(dotenv_path="/mnt/ActDrive/duhchristmas/.env")

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/mnt/ActDrive/duhchristmas/app')

from main import app as application
