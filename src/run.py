from fastapi import FastAPI
import os

import uvicorn
import requests

ROOT_PATH = os.environ['ROOT_PATH']

app = FastAPI(root_path=ROOT_PATH if ROOT_PATH else '/s')

@app.get("/")
async def root():
    return {"message":"Hello, World!"}

@app.get("/get_results")
async def get_chars():
    result = requests.get("https://swapi.py4e.com/api/people/1")
    result = result.text
    return eval(result)['name']



if __name__ == '__main__':
    uvicorn.run(
        "run:app",
         port=8000, 
         host="0.0.0.0",
         log_level="debug",
         reload=True)