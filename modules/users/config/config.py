import os


class Settings:
    def __init__(self):
        self.MYSQL_HOST = os.environ["MYSQL_HOST"]
        self.MYSQL_PORT = os.environ["MYSQL_PORT"]
        self.MYSQL_USER = os.environ["MYSQL_USER"]
        self.MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
        self.MYSQL_DATABASE = os.environ["MYSQL_DATABASE"]
        self.DATABASE_URL = f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
