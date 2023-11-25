"""
URL configuration for Thirdeye project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from Thirdeye import views
# from Services.models import Services
from Home.models import FormSubmit



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.Homepage), 
    path('contact/',views.contact),
    path('services/',views.services),
    path('clients/',views.clients),
    path('ThankYou/',views.ThankYou),
    path('Order/',views.Order),
    path('SaveEnquery/',views.SaveEnquery,name="SaveEnquery"),

]

