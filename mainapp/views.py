from django.http import HttpResponse
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")