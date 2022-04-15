from django.views.generic import CreateView, DetailView, UpdateView

from .models import Incoming


class IncomingCreateView(CreateView):
    model = Incoming
    fields = ["title", "author", "description", "document"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class IncomingDetailView(DetailView):
    model = Incoming
    