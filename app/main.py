from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import schemas 
import crud 
import models
from database import get_db, engine 


#when we start the main file, each time the FastAPI loads up the server it will make sure that the certain database exists and that the table exist - if it doesn't it will create it 
models.Base.metadata.create_all(bind=engine) 
#this creates the database 

app = FastAPI()

#setup for Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/index", response_class = HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# look up what this does, isn't explained in the course

# set up an endpoint for posting data to the database
@app.post("/translate", response_model=schemas.Task)
def translate(request: schemas.TranslationRequest): #the incoming data is part of the request and is validated by the schema
# the user sends the text & language and the API sends back the task_id
    task = crud.create_translateion_task(get_db.db, request.text, request.launguages)

#background_task.add_task(perform_translation, task.id, request.text, request.languages, get_db.db)
#for the background tasks you need to write utility functions 
    #return {"task_id":{task.id}}