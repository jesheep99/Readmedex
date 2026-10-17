FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente y la plantilla (incluyendo main.py y Real-Readme.md)
COPY . /app

# Dar permisos de ejecución al entrypoint y configurarlo
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]