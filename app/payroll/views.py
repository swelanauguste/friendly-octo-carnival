from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import DeductionChange


class DeductionChangeListView(ListView):
    model = DeductionChange


class DeductionChangeDetailView(DetailView):
    model = DeductionChange
