from django.shortcuts import render
from rest_framework.generics import *
from django.views.generic import *
from .serializers import *
from .models import User
# Create your views here.
class SorovApiView(ListCreateAPIView,DestroyAPIView,UpdateAPIView):
    queryset = User.objects.all()
    serializer_class  = SorovSerializer

class Detail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class  = SorovSerializer