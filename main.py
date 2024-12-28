from fastapi import FastAPI

app = FastAPI()

@app.get("/hiakku")
async def root():
    return { "message": "Hi i am akku" }