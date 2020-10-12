from django.db import models
from core import models as core_models
# Create fyour models here.


class Review(core_models.TimeStampedModel):
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    checkin = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews")
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f'{self.review} - {self.room}'

    def rating_average(self):
        avg = (self .accuracy +
               +self. communication
               + self. cleanliness
               + self. location
               + self. checkin
               + self. value
               )/6
        return round(avg, 2)
    rating_average.short_description = "Avg."
