from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from recipes.models import Baker


@receiver(post_save, sender=User)
def create_baker_profile(sender, instance, created, **kwargs):
    if created:
        Baker.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_baker_profile(sender, instance, **kwargs):
    instance.baker.save()
