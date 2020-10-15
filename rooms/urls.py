from django.urls import reverse,path
from . import views
app_name="rooms"
urlpatterns =[
    path("<int:pk>/",views.room_detail,name="detail")
]