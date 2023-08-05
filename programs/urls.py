from django.urls import path
from .views import HomePageView,AboutUsViewPage

app_name = 'inua'

urlpatterns = [
    path('',HomePageView.as_view(),name='homepage'),
    path('aboutus/',AboutUsViewPage.as_view(),name='aboutus')
]