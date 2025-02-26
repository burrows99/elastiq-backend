make sure you are in elastiq/backend

docker build -f Dockerfile -t elastiq-backend-docker . // builds image

docker run -d -p 8000:8000 elastiq-backend-docker to run the conatiner