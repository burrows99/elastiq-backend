# app/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import ReviewRequest
from app.cohere_client import classify_review
import logging

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development purposes)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Set up logging for production
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI in Docker!"}

@app.post("/classify_review/")
async def classify_sentiment(request: ReviewRequest):
    """
    Classify the sentiment of the provided movie review.
    Accepts a review as input and returns the sentiment prediction.
    """
    try:
        sentiment = await classify_review(request.review)  # Calls the mock classify_review function
        return {"review": request.review, "sentiment": sentiment}
    except Exception as e:
        logger.error(f"Error classifying review: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")