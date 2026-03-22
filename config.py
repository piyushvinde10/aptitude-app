import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///aptitude.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False