import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp3.models import MyModel
from django.db import transaction

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal triggered for instance: {instance.name}")
    # Simulate a database operation inside the signal
    instance.signal_processed = True
    instance.save()
    print(f"Signal processed for {instance.name} in thread: {threading.current_thread().name}")
