from django.urls import path
from polls.content.views import Contact, UploadProject, Sendmail, ToggleLike

urlpatterns = [
    path('contact',Contact.as_view()),
    path('upload',UploadProject.as_view()),
    path('sendmail',Sendmail.as_view()),
    path('like',ToggleLike.as_view()),
]

