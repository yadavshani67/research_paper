"""research_paper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from research.views import create,create_paper,dashboard,update,delete,update_profile
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',create,name="create"),
    path('dashboard/',dashboard,name="dashboard"),
    path('paper/',create_paper,name="paper"),
    path('accounts/',include('accounts.urls')),
    path('update_profile/<int:pk>/',update_profile,name="update_profile"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('dashboard/',TemplateView.as_view(template_name='dadhboard.html'),name='dashboard/'),
    path('edit/<int:pk>/',update,name="update"),
    path('delete/<int:pk>/',delete,name="delete")
  
   # path('^accounts/',include('allauth.urls')),
]
