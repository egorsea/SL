from django.urls import path
from . import views
from .views import ajaxFormParameters

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('induktivnye-datchiki/', views.InductiveView.as_view(), name = 'induktivnye-datchiki'),
    path('opticheskie-datchiki/', views.underconsruction, name = 'opticheskie-datchiki'),
    path('emkostnye-datchiki/', views.underconsruction, name = 'emkostnye-datchiki'),
    path('induktivnye-datchiki/ajaxform/', views.ajaxFormParameters, name = 'ajaxFormParameters'),

]
