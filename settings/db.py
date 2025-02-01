from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn = "sqlite:///pylogin.db"

engine = create_engine(conn, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
