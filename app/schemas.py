from pydantic import BaseModel
from typing import List, Dict

class TranslationRequest(BaseModel):  
    text: str  # the string that the user puts in for translation
    languages : List[str] # a list of strings

class TaskResponse(BaseModel):
    task_id: int   # the ID we're returning to the frontend as soon as the request has been made

class TranslationStatus(BaseModel):
    task_id: int
    status: str
    translation: Dict[str,str]

# all these schemas are validating the data and are making sure they are in the right format 