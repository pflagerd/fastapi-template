from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()

# Serve files from the current directory
app.mount("/", StaticFiles(directory="./", html=True), name="static")

uvicorn.run(app, host="127.0.0.1", port=8888)
