import os


# singletone pattern
class Connector:

    __instance = None
    __user = os.environ.get("POSTGRES_USER")
    __password = os.environ.get("POSTGRES_PASSWORD")
    __url = os.environ.get("POSTGRES_URL")
    __db = os.environ.get("POSTGRES_DB")

    def __new__(cls, *args, **kwargs):
        if not cls.__user or not cls.__password or not cls.__url or not cls.__db:
            raise Exception(
                "Please in environment check credentials (user, password, url, db)!"
            )
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Connector.__instance is None

    def __init__(self):
        self.POSTGRES_USER = self.__user
        self.POSTGRES_PASSWORD = self.__password
        self.POSTGRES_URL = self.__url
        self.POSTGRES_DB = self.__db

    def create_path(self):
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_URL}/{self.POSTGRES_DB}"


DB_path = Connector().create_path()
