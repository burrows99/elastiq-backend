# app/models.py

from pydantic import BaseModel

class ReviewRequest(BaseModel):
    review: str  # Movie review text