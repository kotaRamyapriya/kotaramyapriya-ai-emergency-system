from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Emergency Response System is running!"}

@app.get("/service1")
def service1():
    return {"message": "Service 1 response"}

@app.get("/service2")
def service2():
    return {"message": "Service 2 response"}
