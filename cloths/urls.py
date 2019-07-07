from django.urls import path
from cloths import views

urlpatterns = [
    path('', views.cothList.as_view()),
]