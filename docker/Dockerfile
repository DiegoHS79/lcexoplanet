FROM python:3.13.0rc1-bullseye

# Instalar las dependencias necesarias
RUN apt-get update && apt-get install -y curl sudo

# Añadir usuario y modificar permisos
RUN useradd --create-home podium && \
    chown -R podium /home/podium && \
    usermod -aG sudo podium && \
    find /usr/local/lib -type d -exec chmod 777 {} \; && \
    find /usr/local/bin -type d -exec chmod 777 {} \;

# Copiar e instalar los requerimientos de Python
WORKDIR home/podium/code
COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Cambiar a usuario podium
USER podium

EXPOSE 8888