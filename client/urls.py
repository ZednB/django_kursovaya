from django.urls import path

from client.apps import ClientConfig
from client.views import ClientDetailView

app_name = ClientConfig.name

urlpatterns = [

    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_view'),
]