from dotenv import load_dotenv
import os

load_dotenv()  # This loads the environment variables from a .env file

def load_api_key() -> str:
    api_key = 'DIUnF2CeqzMmRd5KFzlnF1qtEuwNJgcwUPJ0emfm'
    if not api_key:
        raise ValueError("Cohere API key is missing. Set the COHERE_API_KEY environment variable.")
    return api_key

def load_cohere_model_id() -> str:
    model_id = 'fb460d8e-dcb9-4dec-af45-6332b2fa87e1-ft'
    if not model_id:
        raise ValueError("Cohere ModelID is missing. Set the COHERE_MODEL_ID environment variable.")
    return model_id