from django.urls import path
from polls.user.views import Login, Join, Logout, Uploadprofile

urlpatterns = [
    path('login',Login.as_view()),
    path('join',Join.as_view()),
    path('logout',Logout.as_view()),
    path('profile/upload',Uploadprofile.as_view())
]
