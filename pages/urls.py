from django.urls import path 
from pages.views import home_view, Menu_next_view


urlpatterns = [
    path('', home_view),
    path('', Menu_next_view)
]
