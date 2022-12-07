from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import User

class Login(APIView):
    def get(self,request):
        return render(request,"user/login.html")

class Join(APIView):
    def get(self,request):
        return render(request,"user/join.html")

    # 회원가입
    def post(self,request):
        email = request.data.get('email',None)
        name = request.data.get('name',None)
        nickname = request.data.get('nickname',None)
        password = request.data.get('password',None)
        
        User.objects.create(email=email,name=name,nickname=nickname,password=make_password(password),profile_img="default_profile.png")

        return Response(status=200)
