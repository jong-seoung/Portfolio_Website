from django.urls import path
from polls.user.views import Login, Join, Logout, Uploadprofile
# KakaoLogin, NaverLogin, GoogleLogin, GithubLogin

urlpatterns = [
    path('login',Login.as_view()),
    path('join',Join.as_view()),
    path('logout',Logout.as_view()),
    path('profile/upload',Uploadprofile.as_view(), name='profile'),
    # path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao'),
    # path('rest-auth/naver/', NaverLogin.as_view(), name='naver'),
    # path('rest-auth/google/', GoogleLogin.as_view(), name='google'),
    # path('rest-auth/github/', GithubLogin.as_view(), name='github'),
]
