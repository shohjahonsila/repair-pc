from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog-single/', BlogsinglePageView.as_view(), name='blogsingle'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('index', IndexPageView.as_view(), name='index'),
    path('mail/', MailPageView.as_view(), name='mail'),
    path('price/', PricePageView.as_view(), name='price'),
    path('project/', ProjectPageView.as_view(), name='project'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('single-project/', SingleprojectPageView.as_view(), name='singleproject'),
    path('team/', TeamPageView.as_view(), name='team'),
    path('lock/', LockPageView.as_view(), name='lock'),
]
