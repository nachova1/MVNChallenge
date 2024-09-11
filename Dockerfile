# Usa una imagen base de Python con la versión que estés usando
FROM python:3.12

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del proyecto al directorio de trabajo
COPY . .

# Expone el puerto en el que correrá la aplicación (8000 para FastAPI)
EXPOSE 8000

# Comando para correr la aplicación usando Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
