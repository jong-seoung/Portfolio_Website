from django.urls import path
from polls.content.views import Contact

urlpatterns = [
    path('contact',Contact.as_view()),
]