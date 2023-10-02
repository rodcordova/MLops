from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

@app.get("/userdata/{User_id}")
def userdata(User_id:str):
    return 'hello'