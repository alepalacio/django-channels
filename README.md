# DJANGO CHANNELS (WEB SOCKETS) USANDO CELERY Y REDIS.

## Pequeña app que toma información de la api "http://api.icndb.com/jokes/random", extrae la data requerida, la procesa, hace peticiones, las maneja de manera asíncrona y las muestra de manera dinámica.

### Comandos utilizados:

- `pip install requests` -- Instalando la librería de requests para manejo de peticiones.

- `pip install 'celery'[redis]` -- Instalar por medio de pip celery con su broker redis.

- `sudo apt install redis-server` -- Instalar redis-server.

- `ps aux | grep redis`
 
 - `sudo service redis-server stop` -- Si en la terminal el puerto figura que está en uso, puedes detener previamente todos las apps que usen el puerto, y usar el que trae por defecto.

 - `redis-server` -- Inicializar el broker.

- `celery -A src beat -l INFO` -- Para inicializar el Beat, que ejecutará el task con el tiempo proporcionado.

- `celery -A src worker -l INFO` -- Para inicializar el celery y poder ver los logs de manera dinámica.

- `pip install channels` -- Instalar channels.

- `pip install channels-redis`