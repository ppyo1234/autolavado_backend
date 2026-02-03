from typing import Union
app = FastAPI() import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello word"}