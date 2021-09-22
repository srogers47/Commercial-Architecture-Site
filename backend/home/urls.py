from django.urls import path
from .views import HomeView

urlpatterns = [
        # Home/Landing 
        path('', HomeView.as_view()),

        ]

