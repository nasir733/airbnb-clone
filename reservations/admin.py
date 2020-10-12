from django.contrib import admin
from .import models
# Register your models Reservation.


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    ''' Reservation Admin Definition '''

    list_display = (
        'room',
        'check_in',
        'status',
        'check_out',
        'guest',
        'in_progress',
        'is_finished',
    )
    list_filter = ("status",)
