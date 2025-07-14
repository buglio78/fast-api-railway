from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Ciao! FastAPI funziona su Railway 🚂"}

@app.get("/step/{step_id}")
def get_step(step_id: int):
    return {"step_id": step_id, "status": "In lavorazione"}
