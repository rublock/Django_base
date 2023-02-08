from django.http import HttpResponse
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        # get all previous data
        context = super().get_context_data(**kwargs)
        # create your own data
        context["data_for_site"] = "some data to display from get_context_data()"
        return context

# get data from address panel
def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")