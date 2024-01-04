from config.config import Settings
from sqlalchemy import create_engine
import sqlalchemy


class Database:
    def __init__(self):
        self.engine = create_engine(Settings().DATABASE_URL)
        self.metadata = sqlalchemy.MetaData()
        self.connection = self.engine.connect()
        self.users = sqlalchemy.Table(
            "users", self.metadata, autoload=True, autoload_with=self.engine
        )

    def get_user(self):
        query = sqlalchemy.select([self.users])
        result = self.connection.execute(query)
        print(result)
        return result.fetchall()

    def post_user(self, user=dict):
        query = self.users.insert().values(user)
        result = self.connection.execute(query)
        return result.inserted_primary_key
