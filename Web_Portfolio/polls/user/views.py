from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import User
from uuid import uuid4
from config.settings import MEDIA_ROOT
import os


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

# 로그인
class Login(APIView):
    def get(self,request):
        return render(request,"user/login.html")

    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=404, data=dict(message="회원 정보가 잘못되었습니다."))

        if user.check_password(password):
            # 세션 or 쿠키에 넣는다
            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=400, data= dict(message="회원정보가 잘못되었습니다."))

# 로그아웃
class Logout(APIView):
    def get(self,request):
        request.session.flush()
        print(request.session)
        return render(request,"user/login.html")

class Uploadprofile(APIView):
    def post(self,request):

        # 파일 불러오기
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        # 파일을 읽어서 파일을 만들기
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_img = uuid_name
        email = request.data.get('email')

        user = User.objects.filter(email=email).first()

        user.profile_img = profile_img
        user.save()

# 소셜 로그인

# 소셜 로그인
# BASE_URL = 'http://localhost:8000/api/v1/accounts/rest-auth/'
# KAKAO_CALLBACK_URI = BASE_URL + 'kakao/callback/'
# NAVER_CALLBACK_URI = BASE_URL + 'naver/login/callback/'
# GOOGLE_CALLBACK_URI = BASE_URL + 'google/callback/'
# GITHUB_CALLBACK_URI = BASE_URL + 'github/callback/'


# class KakaoLogin(SocialLoginView):
#     adapter_class = KakaoOAuth2Adapter
#     callbakc_url = KAKAO_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer


# class NaverLogin(SocialLoginView):
#     adapter_class = NaverOAuth2Adapter
#     callback_url = NAVER_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer


# class GithubLogin(SocialLoginView):
#     adapter_class = GitHubOAuth2Adapter
#     callback_url = GITHUB_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer


# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = GOOGLE_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer