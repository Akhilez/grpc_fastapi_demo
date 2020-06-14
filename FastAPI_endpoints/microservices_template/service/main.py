from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Some Key": "Some Value"}