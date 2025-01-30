from pydantic import BaseModel
"""
Models for HNG Internship Stage 0
"""


class IndexResponse(BaseModel):
    email: str
    current_datetime: str
    github_url: str