from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker
import os



user = "postgres"
password = quote_plus("96!x3Skaterboiix3!96")
host = "localhost"
database = "translator"

database_url = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(database_url)

def get_db():
    db = SessionLocal()
    try: 
        yield db  
    finally:
        db.close()
        
#SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
#retrieves the database connection URL from the environment variables
#engine = create_engine(SQLALCHEMY_DATABASE_URL)
#creates an instance of the SQLAlchemy engine -> sets up the connection to the database / in the parenthesis you tell to wich database the engine should connect to
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# creates a SessionLocal class that can be used to instantiate database sessions 
#sessionmaker is a function to create a new session class
