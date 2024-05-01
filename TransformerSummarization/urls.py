from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/summarize', permanent=True)),
    path('summarize/', views.main_page, name='main_page'),
    path('generate_summary/', views.generate_summary, name='generate_summary'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
