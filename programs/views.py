from django.shortcuts import render

from .models import Program,AboutUs
from django.views.generic.list import ListView



class HomePageView(ListView):
    model = Program
    template_name = 'homepage.html'
    context_object_name = 'programs'

class AboutUsViewPage(ListView):
    model = AboutUs
    template_name = 'about.html'
    context_object_name = 'aboutus'
