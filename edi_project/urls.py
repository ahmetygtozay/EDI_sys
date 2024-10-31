"""
URL configuration for edi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# edi_project/urls.py
from django.contrib import admin
from django.urls import path, include
from edi_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('edi/', include('edi_app.urls')),  # edi_app URL'lerini ekleyin
    path('create/', views.create_edi_message, name='create_edi_message'),
    path('list/', views.list_edi_messages, name='list_edi_messages'),
    path('upload/', views.upload_edi, name='upload_edi_file'),
    path('messages/translate/<int:message_id>/', views.translate_edi_message, name='translate_edi_message'),
]
