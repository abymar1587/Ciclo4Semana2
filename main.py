from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hola MisionRIC 2023"}

