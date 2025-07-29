from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)

    # Champs RGPD
    is_data_consent_given = models.BooleanField(default=False,verbose_name="Consentement à l'utilisation des données")
    is_contact_consent_given = models.BooleanField(default=False,verbose_name="Consentement à être contacté")

    def __str__(self):
        return self.username
    
