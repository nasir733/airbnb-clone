from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid# Create your models here.
from django.core.mail import send_mail   
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import reverse
from django.template.loader import render_to_string
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
    LOGIN_EMAIL="email"
    LOGIN_GITHUB='github'
    
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        
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
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120,default="")
    login_method = models.CharField(
            max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
        )

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                ("Verify Airbnb Account"),
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return