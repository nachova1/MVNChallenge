## Assistant Project with LangChain and Ollama3

This project is an assistant based in LangChain that intgrate a local model (ollama3) and a search tool Wikipedia to response questions.

The assistant uses FastAPI to expose an APIREST which receives a usser question and returns a response based in information obtained from Wikipedia and local model.

## Technologies Used

- **LangChain**: Framework to build IA agents.
- **Ollama3**: Local model acting as LLM (Large Language Model).
- **FastAPI**: Framework to build API.
- **Wikipedia API Wrapper**: Searh tool from Wikipedia.
- **Docker**: Used to containerize the application and its dependencies.

## Requirements
Before starting, make sure you have the following components installed:

- Python 3.12 or lastest
- pip packet handler
- Docker (optional to container)
- Ollama instaled and configured to use the model "ollama3"

## First Steps

First, clone the repository with the following comand: git clone https://github.com/nachova1/MVNChallenge.git

Open the project in a text editor, Visual Studio Code for example

Then access the MVNChallenge folder with the following command: cd MVNChallenge

### Dependencies Installation

With the following comand you can install all the dependencis of the project: pip install -r requirements.txt

### Important Consideration

This project uses the local model Ollama3. Take sure that you have installed it in your system.

Check if you have the local model with the following command: ollama list

Make sure to have installed the version 3 of Ollama. If you don't have, installed it with the following command: ollama pull ollama3

## Ejecution

To ejecut the local application, you can use the following command: uvicorn api:app --reload

The API will be available in the following URL: http://127.0.0.1:8000

With the URL you can make request from Postman or another APIS testing tool

## Endpoint

Type: POST

Route: http://127.0.0.1:8000/ask

This endpoint recives a JSON question and returns a JSON response generated by the agent using Wikipedia and the local model Ollama3

Example:

![image](https://github.com/user-attachments/assets/01d55bbf-3b75-4c46-935b-ebee8ccbf30a)

## Ejecution with Docker

Create a docker image with the following command: docker build -t mvn-challenge .

In 'mvn-challenge' you can use the name which you preffer

Then, you have to build the container with the following command: docker run -d -p 8000:8000 mvn-challenge

Make sure if you have the container with the following command: docker ps

If is availible, you will can see it.

## Notes

The API uses FastAPI to the server and to expose the endpoint.

LangChain is responsible for managing the flow of interaction between the local ollama3 model and the Wikipedia tool.

The application is designed to be containerized using Docker, but can also run locally without problems.
