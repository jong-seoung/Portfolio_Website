from django.shortcuts import render
from rest_framework.views import APIView

class Login(APIView):
    def get(self,request):
        return render(request,"user/login.html")

class Join(APIView):
    def get(self,request):
        return render(request,"user/join.html")