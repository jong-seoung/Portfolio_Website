from django.urls import path
from polls.content.views import Contact, UploadProject, Sendmail

urlpatterns = [
    path('contact',Contact.as_view()),
    path('upload',UploadProject.as_view()),
    path('Sendmail',Sendmail.as_view()),
]

