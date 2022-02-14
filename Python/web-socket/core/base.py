from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from core.base_class import Base
from core import config 

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, pool_size=30, max_overflow=120)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base session query config
Base.query = db_session.query_property()
