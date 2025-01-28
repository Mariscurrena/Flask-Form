#Se instala la distribución Alpine
FROM alpine:3.19

#Dentro de la shell de Alpine se descarga python y pip para poder correr el programa
#Esta es una manera alternativa de actualizar, la manera convencional no funcionó
RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    rm /usr/lib/python3.11/EXTERNALLY-MANAGED && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    pip install --no-cache --upgrade pip setuptools wheel

#Crea un directorio para alojar la aplicacion dentro de la imagen alpine
WORKDIR /app

#El punto "." indica que se va a copiar todo lo que este en el directorio donde se encuentra.
#El segundo path, indica la ubicación en la imagen donde lo voy a copiar (Directorio creado en el paso anterior)
COPY . /app

#Se instalan los requerimientos
#--no-cache-dir es para que no utilice la memoria cache
RUN pip3 --no-cache-dir install -r requirements.txt

#Ejecutamos el programa, es necesario exponer el puerto al que vamos a acceder
EXPOSE 5000
CMD ["python3", "src/app.py"]