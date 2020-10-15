from django.urls.base import reverse
from django.utils import timezone
from django.shortcuts import render,redirect,reverse
from . import models
from django.http import Http404
from math import ceil
from django.core.paginator import Paginator ,EmptyPage
from django.views.generic import ListView
# Create your views here.


class HomeView(ListView):
    """ HomeView"""

    model = models.Room
    paginate_by=10
    ordering="created"
    paginate_orphans=5
    context_object_name="rooms"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"]=now
        return context

def room_detail(request,pk):
    try:
        room = models.Room.objects.get(pk=pk)
        render(request,"rooms/detail.html",{'room':room})

    except models.Room.DoesNotExist:
        raise Http404()        