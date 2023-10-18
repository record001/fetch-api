from django.urls import path,include
from .views import *
urlpatterns = [
    path('', SorovApiView.as_view()),
    path('detail/<int:pk>/', Detail.as_view()),
]