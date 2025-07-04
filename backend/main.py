from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем фронтенд как статику
app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")

@app.get("/api/hello")
def read_root():
    return {"message": "Привет от FastAPI"}

@app.get("/") #sdasdasd sad  sadad sasd asd asd 
def serve_index():
    return FileResponse("../frontend/index.html") # Ваыфаыфвыфвыфыфввыфыфвфы