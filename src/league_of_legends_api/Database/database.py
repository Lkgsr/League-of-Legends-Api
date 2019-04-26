from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from league_of_legends_api.Database.objects import Base, ApiKey


class Database:

    def __init__(self):
        self.engine = create_engine(f'sqlite:///data.db', echo=False)
        self.session = scoped_session(sessionmaker())
        self.setup()

    def setup(self):
        self.session.remove()
        self.session.configure(bind=self.engine, autoflush=False, expire_on_commit=False)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def save_keys_to_database(self, keys):
        for key in keys:
            try:
                self.session.add(ApiKey(key))
                self.session.commit()
            except Exception as e:
                print(f'Error by Committing key {key}: {str(e)}')

    def load_keys_in(self):
        return self.session.query(ApiKey).all()
