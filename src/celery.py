import os
from celery import Celery

#Declaro las configuraciones necesarias.  Sino consigue el primer parámetro, pasa al segundo.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

#app = una instancia de Celery con el nombre de mi proyecto.
app = Celery('src')

app.config_from_object('django.conf:settings', namespace='CELERY')

#Declaro el beat, indicando la tareja a ejecutar con la ruta a la tarea, y schedule con un value que es expresado en segundos.
app.conf.beat_schedule = {
    'get_joke_3s':{
        'task':'jokes.tasks.get_joke',
        'schedule':3.0
    }
}

app.autodiscover_tasks()
