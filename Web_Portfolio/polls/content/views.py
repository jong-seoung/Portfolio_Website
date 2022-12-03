from django.shortcuts import render
from rest_framework.views import APIView

class Contact(APIView):
    def get(self,request):
        return render(request,"content/contact.html")
