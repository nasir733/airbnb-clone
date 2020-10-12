from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    """Custeom User Model """
    GENDER_MALE = "male"
    GENDER_FEMALe = 'female'
    GENDER_OTHER = "other"
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_Urdu = "ur"
    CURRENCY_USD = "usd"
    CURRENCY_PKR = "pkr"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_Urdu, 'Urdu'),
    )
    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALe, "female"),
        (GENDER_OTHER, "other"),
    )
    CURRENCY_CHOICES = (
        (CURRENCY_PKR, 'PKR'),
        (CURRENCY_USD, 'USD'),
    )
    avatar = models.ImageField(blank=True, upload_to="avatars")
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    languages = models.CharField(
        choices=LANGUAGE_CHOICES, blank=True, max_length=2)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, blank=True, max_length=3)
    superhost = models.BooleanField(default=False)
