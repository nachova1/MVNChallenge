from fastapi import FastAPI
from pydantic import BaseModel
from ai import ask_agent
import uvicorn

app = FastAPI()

# Modelo para la solicitud del usuario
class UserQuery(BaseModel):
    query: str

# Endpoint que recibe la consulta y llama al agente LangChain
@app.post("/ask")
async def ask_question(user_query: UserQuery):
    query = user_query.query
    response = ask_agent(query)
    #Formo la respuesta en formato JSON
    return {"content": response}


if __name__ == "__main__":
    # Ejecuto la aplicación con Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

