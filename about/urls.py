
from django.urls import path
from . import views
from .views import (SendContactFormTemplateView) #ManageTemplateView, 

urlpatterns = [
    path('about/', views.about_page, name='about'),
 
    # path('manage', ManageTemplateView.as_view(), name='manage'),
    path('contact/contact_form', SendContactFormTemplateView.as_view(), name='contact_form'),
    
]
