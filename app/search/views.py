from django.shortcuts import render
from django.views.generic import TemplateView

from incoming.models import Incoming
# from outgoing.models import Outgoing

class SearchView(TemplateView):
    template_name = 'search/search.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context['incoming_objects'] = Incoming.objects.all()
        return context