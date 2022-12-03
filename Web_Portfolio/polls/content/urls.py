from django.urls import path
from polls.content.views import Contact

urlpatterns = [
    path('',Contact.as_view()),
]
