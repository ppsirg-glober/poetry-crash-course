from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def salute():
    return "hello"
