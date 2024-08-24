from fastapi import FastAPI 
from pydantic import BaseModel
import uvicorn
import os 

app = FastAPI()

@app.get("/") 
def welcome():
    return {"message": "Welcome to ChatGPT AI Application"}

@app.post("/dummy") 
def demo_function(data):
    return {"message": data}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=80)