from django.urls import path  # Import path for routing URLs
from . import views  # Import the views module to link routes to view functions

urlpatterns = [
    path('', views.index, name='index'),  # Maps the root URL to the `index` view
]