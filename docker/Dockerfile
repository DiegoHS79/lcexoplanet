FROM python:3.13.0rc1-bullseye

# Instalar las dependencias necesarias
RUN apt-get update && apt-get install -y curl sudo

# Añadir usuario y modificar permisos
RUN useradd --create-home podium
RUN chown -R podium:podium /home/podium
RUN usermod -aG sudo podium

# Copiar e instalar los requerimientos de Python
WORKDIR /home/podium/code
COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Cambiar a usuario podium
USER podium

EXPOSE 8888