from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

Base = declarative_base()

# engine = create_engine(settings.DATABASE_URL, echo=True)
# engine = create_engine(settings.DATABASE_URL, echo=True, pool_size=3000, max_overflow=20)

engine =create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        connect_args={
            "keepalives": 1,
            "keepalives_idle": 30,
            "keepalives_interval": 10,
            "keepalives_count": 5,
        }
    )
Session = sessionmaker(bind=engine)
session = Session()
