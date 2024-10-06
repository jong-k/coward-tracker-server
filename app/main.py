from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from app.api.main import api_router

load_dotenv()

app = FastAPI()


@app.get("/")
def greeting():
    return "Hello World!"


app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
