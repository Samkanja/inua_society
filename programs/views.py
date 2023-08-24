from django.shortcuts import render

from .models import Program,AboutUs,Activity,BoardMember
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



class HomePageView(ListView):
    model = Program
    template_name = 'homepage.html'
    context_object_name = 'programs'

class AboutUsViewPage(ListView):
    model = AboutUs
    template_name = 'about.html'
    context_object_name = 'aboutus'

class NavBarViewList(ListView):
    model = Program
    template_name = 'navbar.html'
    context_object_name = 'programs'

class BoardMemberView(ListView):
    model = BoardMember
    template_name = 'boardmembers.html'
    context_object_name = 'boardmembers'



class ActivityDetailView(DetailView):
    model = Program
    template_name = 'detail.html'
    context_object_name = 'program'

    def get_object(self,queryset=None):
        return Program.objects.get_object_by_public_id(public_id=self.kwargs['public_id'])

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        program = self.object
        context['activities'] = program.activity_set.all()
        return context 




