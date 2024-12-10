from sqlalchemy import Column, Integer, String, Text, JSON

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#this will create the table with the name "translation tasks" once we load our server : 

class TranslationTask(Base):
    __tablename__ = "translation_tasks"  #creates a table called translation_tasks

    # now defining all the roles
    id = Column(Integer, primary_key=True, index=True)
    # integer -> this column stores integer values
    # primary key=True -> no other row in this column can have the same value
    # index=True -> creates an index which speeds up queries that filter / sort by the id
    text = Column(Text, nullable=False)
    #text -> column stores text data
    #nullable=False -> required field, can't be empty
    languages = Column(JSON, nullable=False)
    # JSON -> stores data in JSON format -> allows to store structured data like lists or dictionaries directly in the DB
    status = Column(String, default="in progress")

    translation = Column(JSON, default={})