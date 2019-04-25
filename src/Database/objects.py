from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import json


Base = declarative_base()


class ApiKey(Base):

    __tablename__ = "apikeys"

    key = Column(String, unique=True)
    id = Column(Integer, autoincrement=True, primary_key=True)
    header = Column(String)
    retry_after = Column(Integer)
    x_rate_limit_type = Column(Integer)

    def __init__(self, key):
        self.key = key
        self.retry_after = 0
        self.x_rate_limit_type = 0
        self.header = json.dumps({"X-Riot-Token": self.key})

    def to_dict(self):
        return {'id': self.id, 'key': self.key}

    def get_header(self):
        return json.loads(self.header)

    def __repr__(self):
        return f'ApiKey: key:{self.key}, id: {self.id}'

