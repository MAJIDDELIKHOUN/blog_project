from django.urls import path
from .views import Home

app_name = 'home_app'
urlpatterns = [
    path('', Home, name='home'),
]
