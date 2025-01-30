from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pydantic import BaseModel
from typing import Any

"""
Simple api for HNG Internship Stage 0
"""


class IndexResponse(BaseModel):
    email: str
    current_datetime: str
    github_url: str

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get('/', response_model=IndexResponse, status_code=status.HTTP_200_OK)
async def index() -> Any:
    """Index route for HNG Internship Stage 0"""
    return IndexResponse(
            email="osamsackeyjude@gmail.com",
            current_datetime=datetime.now().replace(microsecond=0).isoformat(),
            github_url="https://github.com/judeo-s/HNG-Internship/tree/main"
        )
