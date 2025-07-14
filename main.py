from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🚂 FastAPI Railway è attivo!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Ciao, {name}!"}
