from django.views.generic import TemplateView

# Create your views here.
class HomePageview(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
