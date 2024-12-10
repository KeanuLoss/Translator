import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def get_db():
    db = SessionLocal()
    try: 
        yield db  
    finally:
        db.close()
        
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
#retrieves the database connection URL from the environment variables

engine = create_engine(SQLALCHEMY_DATABASE_URL)
#creates an instance of the SQLAlchemy engine -> sets up the connection to the database / in the parenthesis you tell to wich database the engine should connect to
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# creates a SessionLocal class that can be used to instantiate database sessions 
#sessionmaker is a function to create a new session class