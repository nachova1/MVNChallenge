from fastapi import FastAPI
from pydantic import BaseModel
from agent import ask_agent
from dotenv import load_dotenv
import os
import uvicorn

# Cargar las variables del archivo .env
load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")

app = FastAPI()

# Modelo para la solicitud del usuario
class UserQuery(BaseModel):
    query: str

# Endpoint que recibe la consulta y llama al metodo ask_agent
@app.post("/ask")
def ask_question(user_query: UserQuery):
    query = user_query.query
    response = ask_agent(query)
    #Formo la respuesta en formato JSON
    return {"content": response}


if __name__ == "__main__":
    # Ejecuto la aplicación con Uvicorn
    uvicorn.run(app, host=host, port=port)

