# Elastiq Backend

This is the backend service for **Elastiq** built using **FastAPI**. The server runs on port `8000` and utilizes the **Cohere API** for sentiment analysis.

## Requirements

- Docker
- FastAPI
- Cohere API (for sentiment analysis)

## Getting Started

Follow the steps below to build and run the Elastiq backend using Docker.

### 1. Clone the Repository

```bash
git clone https://github.com/burrows99/elastiq-backend.git
cd elastiq-backend
```

### 2. Build the docker image
Make sure you are in the root directory of the project.

```bash
docker build -f Dockerfile -t elastiq-backend-docker .
```

### 3. Run the Docker Container
To start the container and run the server on port 8000, use the following command:

```bash
docker run -d -p 8000:8000 elastiq-backend-docker
```

### 4. Access the server
Once the local server is running, you can access it at:

```bash
http://localhost:8000
```
Deployed server can be accessed it at:

```bash
https://elastiq-backend.onrender.com/
```

### 5. Sentiment Analysis with Cohere API
The Elastiq backend integrates with Cohere to perform sentiment analysis. You can send a POST request to the following endpoint to analyze the sentiment of a text:

```bash
POST https://elastiq-backend.onrender.com/classify_review
```
Request Body Example:
```json
{
  "sentiment": "positive"
}
```