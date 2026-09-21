from fastapi import FastAPI, HTTPException
from app.core.config import APP_NAME
from app.services.user_service import get_user
import logging

app=FastAPI()
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger(__name__)

@app.get("/")
def root():
    logger.debug("GET / called")
    return {"AppName":APP_NAME}

@app.get("/health")
def health():
    logger.debug("GET / called")
    return {"STATUS": "ok"}



@app.get("/users/{user_id}")
def getuser(user_id:int):
    logger.debug("GET / called")
    result = get_user(user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="USER NOT FOUND")
    return result
