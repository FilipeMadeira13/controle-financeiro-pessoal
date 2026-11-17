from django.urls import path

from finance.views import index


urlpatterns = [
    path('', index)
]