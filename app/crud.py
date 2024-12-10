from sqlalchemy.orm import Session
import models

def create_translation_task(db: Session, text:str, languages:list):
    #db, text and language are the arguments that are required for the function to work
    task = models.TranslationTask(text=text, languages=languages)
    db.add(task) #goes to the db session and adds it to the db
    db.commit()
    db.refresh(task)
    #after every added "item" you need to commit and refresh
    #commit saves the updates
    #reloads the updated task object from the database
    return task


# the method that will fetch the translation task
# it returns the query according to the ID that we pass it
def get_translation_task(db: Session, task_id: int):
    return db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()
#.query starts a database query for the model in the parenthesis
#.filter adds a filter condition to the query
#models.TranslationTask.id represents the id field / column of the TranslationTask table
#Task_id is the variable you're searching for
#.first retrieves the first record that matches the filter condition


#passes the translated payload to the database
def update_translation_task(db: Session, task_id: int, translations: dict):
    task = db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()
    task.translations = translations
    task.status = "completed"
    db.commit()
    db.refresh(task)
    return task
    