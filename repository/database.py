from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


DATABASE_URL = ""
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()


def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()