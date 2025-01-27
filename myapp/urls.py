from django.urls import path
from . import views  # Import views from the current app

# App name for namespacing
app_name = 'your_app_name'

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
