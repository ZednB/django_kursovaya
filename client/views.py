from django.shortcuts import render

from django.views.generic import DetailView

from client.models import Client


class ClientDetailView(DetailView):
    model = Client
