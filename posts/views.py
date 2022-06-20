from msilib.schema import ListView
from typing import List
from django.shortcuts import render
from .models import *
from django.views.generic import ListView


class HomePageView(ListView):
    model = Posts
    template_name = 'home.html'
    context_object_name = 'all_posts'



