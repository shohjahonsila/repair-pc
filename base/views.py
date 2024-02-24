from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class BlogsinglePageView(TemplateView):
    template_name = 'pages/blog-single.html'

class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class FaqPageView(TemplateView):
    template_name = 'pages/faq.html'

class IndexPageView(TemplateView):
    template_name = 'pages/index.html'

class MailPageView(TemplateView):
    template_name = 'pages/mail.html'

class PricePageView(TemplateView):
    template_name = 'pages/price.html'

class ProjectPageView(TemplateView):
    template_name = 'pages/project.html'

class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'

class SingleprojectPageView(TemplateView):
    template_name = 'pages/single-project.html'

class TeamPageView(TemplateView):
    template_name = 'pages/team.html'

class LockPageView(TemplateView):
    template_name = 'pages/lock.html'
