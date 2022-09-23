import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or hash("cant touch this")
