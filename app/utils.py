from dotenv import load_dotenv
import os

load_dotenv()  # This loads the environment variables from a .env file

def load_api_key() -> str:
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        raise ValueError("Cohere API key is missing. Set the COHERE_API_KEY environment variable.")
    return api_key

def load_cohere_model_id() -> str:
    model_id = os.getenv("COHERE_MODEL_ID")
    if not model_id:
        raise ValueError("Cohere ModelID is missing. Set the COHERE_MODEL_ID environment variable.")
    return model_id