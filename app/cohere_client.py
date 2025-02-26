import cohere
from app.utils import load_api_key, load_cohere_model_id

cohere_client = cohere.Client(load_api_key())


async def classify_review(review: str) -> str:
    """
    Classify the sentiment of a movie review using a fine-tuned Cohere model without examples.
    :param review: Movie review text
    :return: Predicted sentiment (Positive, Negative, Neutral)
    """
    # Call the Cohere classify method using the fine-tuned model
    response = cohere_client.classify(
        model=load_cohere_model_id(),  # Fine-tuned model ID
        inputs=[review]  # Provide the review as input
    )

    # Return the predicted sentiment
    return response.classifications[0].prediction