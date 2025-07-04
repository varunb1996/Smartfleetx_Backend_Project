from celery import Celery

celery_app = Celery("tasks", broker="redis://redis:6379/0")

@celery_app.task
def notify_operator(vehicle_id):
    print(f"Sending alert for {vehicle_id}")
