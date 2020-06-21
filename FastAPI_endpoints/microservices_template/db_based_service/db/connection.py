from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from secrets import db_path

engine = create_engine(db_path)

Session = sessionmaker(bind=engine)
