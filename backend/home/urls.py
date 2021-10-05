from django.urls import path
from .views import home_view 

urlpatterns = [
        # Home/Landing 
        path('', home_view, name="landing"),

        ]

