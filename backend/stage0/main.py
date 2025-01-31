from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from models import IndexResponse
from typing import Any
"""
Simple api for HNG Internship Stage 0
"""

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', response_model=IndexResponse, status_code=status.HTTP_200_OK)
async def index() -> Any:
    """Index route for HNG Internship Stage 0"""
    return IndexResponse(
            email="osamsackeyjude@gmail.com",
            current_datetime=datetime.now().replace(microsecond=0).isoformat()+'Z',
            github_url="https://github.com/judeo-s/HNG-Internship"
        )
