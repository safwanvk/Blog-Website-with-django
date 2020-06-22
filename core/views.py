from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView

from .models import Blog


class IndexView(TemplateView):
    template_name = "core/index.html"


class BlogView(ListView):
    model = Blog
    paginate_by = 100
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "core/blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ContactView(TemplateView):
    template_name = "core/contact.html"


class AboutView(TemplateView):
    template_name = "core/about.html"
