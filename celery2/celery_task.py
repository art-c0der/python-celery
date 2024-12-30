from celery import Celery


app = Celery('celery2')
app.config_from_object('celery_config')

@app.task
def add_numbers():
  return
