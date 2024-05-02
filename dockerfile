#load image
FROM python:3.9-slim

#Define the workspace of the container
WORKDIR /app

#Copy the requirements.txt file in the container
COPY requirements.txt /app

#Install the dependances
RUN pip install -r requirements.txt

EXPOSE 8000
#Copy the curent directory content in the container 
COPY . /app

#Command to run myapi application
CMD [ "uvicorn","myapi:app","--host","0.0.0.0","--port","8000","--reload"]