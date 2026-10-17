FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt /app/requirements.txt
COPY . /app


RUN cd /app && pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
# Dar permisos de ejecución al entrypoint y configurarlo
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]