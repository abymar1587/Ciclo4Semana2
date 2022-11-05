from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo")
async def root():
    return {"message": "Hola MisionRIC 2023"}
