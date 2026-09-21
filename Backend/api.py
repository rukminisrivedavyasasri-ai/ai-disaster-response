import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BACKEND_DIR = Path(__file__).resolve().parent

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from main import run_disaster_response


app = FastAPI(
    title="AI Disaster Response System",
    description="Multi-agent disaster response backend API",
    version="1.0.0"
)


# Allow the React frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "system": "AI Disaster Response System",
        "status": "running"
    }


@app.get("/response-plan")
def get_response_plan():
    return run_disaster_response()