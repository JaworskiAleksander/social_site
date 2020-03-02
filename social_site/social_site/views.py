# Creating very simple view for our home page
# link it to the social_site.urls.py

from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'
    