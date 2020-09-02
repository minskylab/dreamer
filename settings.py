import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
