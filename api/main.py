from fastapi import FastAPI
from routes import auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {
        "message": "Welcome to DevChat API",
        "status": "Running",
        "code": 200
        }
