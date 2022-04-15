from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from incoming.models import Incoming

# from outgoing.models import Outgoing


class SearchView(TemplateView):
    template_name = "search/search.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context["object_list"] = Incoming.objects.all()
        return context


class IncomingSearchListView(ListView):
    model = Incoming
    paginate_by = 10
    template_name = "search/search.html"

    def get_queryset(self):
        queryset = Incoming.objects.all()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q)
                | Q(author__icontains=q)
                | Q(description__icontains=q)
            ).distinct()
        return queryset
