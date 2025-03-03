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
[https://elastiq-backend.onrender.com/](http://35.226.217.146:8000/classify_review)
```

### 5. Sentiment Analysis with Cohere API
The Elastiq backend integrates with Cohere to perform sentiment analysis. You can send a POST request to the following endpoint to analyze the sentiment of a text:

```bash
POST https://elastiq-backend.onrender.com/classify_review
```
Request Body Example:
```json
{
  "review": "This is a very good movie."
}
```

### 6. Deployment on GCP Compute Engine
Steps:
* Set the project ID
```bash
gcloud config set project natural-oxygen-452115-h7
```
* Enable APIs, if not done already.
```bash
gcloud services enable compute.googleapis.com
```
* Add firewall for access to port 8000, if not done already:
```bash
gcloud compute firewall-rules create allow-tcp-8000 \
  --allow tcp:8000 \
  --network default \
  --direction INGRESS \
  --priority 1000 \
  --source-ranges 0.0.0.0/0 \
  --target-tags http-server
```
* Create bare metal vm instance:
```bash
gcloud compute instances create elastiq-backend-instance \
  --zone=us-central1-a \
  --machine-type=n1-standard-1 \
  --image-family=debian-11 \
  --image-project=debian-cloud
```
* Connect to the VM through SSH
```bash
gcloud compute ssh elastiq-backend-instance --zone=us-central1-a
```
* Execute the following commands:
```bash
sudo apt-get update
sudo apt install git -y
sudo apt-get install -y docker.io
```
* Setup repo
```bash
git clone https://github.com/burrows99/elastiq-backend.git
cd elastiq-backend
```
* Build Image
```bash
docker build -f Dockerfile -t elastiq-backend-docker .
```
* Run container
```bash
docker run -d -p 8000:8000 elastiq-backend-docker
```
* See the external IP from the UI and use http://<EXTERNAL_IP>:8000 to access backend.
     

