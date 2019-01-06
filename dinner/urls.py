from django.urls import path

from . import views

app_name = 'dinner'

urlpatterns = [
    path('', views.Homepage.as_view(), name='index'),
    path('add/', views.AddDin.as_view(), name='addDinner')
]
