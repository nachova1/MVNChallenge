from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.prompts import PromptTemplate

from langchain_ollama import ChatOllama

# Inicializa el modelo local con Ollama
llm = ChatOllama(model="llama3")

# Inicializa el API Wrapper de Wikipedia
wikipedia_api = WikipediaAPIWrapper(lang="es")

# Defino la herramienta de busqueda Wikipedia
wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api)

# Plantilla para el agente LangChain
template = """Eres un asistente útil. Usa la información proporcionada de Wikipedia para responder a la siguiente pregunta del usuario.

Información de Wikipedia:
{wiki_content}

Pregunta:
{query}

Respuesta:"""

prompt = PromptTemplate(template=template, input_variables=["wiki_content", "query"])

# Crear una secuencia que primero pasa por el prompt y luego el LLM
# Esto garantiza que la cadena este correctamente creada antes de su uso
def create_chain():
    return prompt | llm

def ask_agent(query: str):
    # Ejecuta la búsqueda en Wikipedia
    wiki_result = wikipedia_tool.run(query)
    
    inputs = {"wiki_content": wiki_result, "query": query}
    #Aca se crea correctamente la cadena
    chain = create_chain()
    #Y aca se usa
    response = chain.invoke(inputs)

    return response.content


