from django.urls import path
from polls.user.views import Login, Join

urlpatterns = [
    path('login',Login.as_view()),
    path('join',Join.as_view()),
]
