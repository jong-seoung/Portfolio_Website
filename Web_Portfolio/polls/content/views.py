from django.shortcuts import render
from rest_framework.views import APIView
from polls.user.models import User

class Main(APIView):
    def get(self,request):
        email = request.session.get('email',None)
        
        if email is None:
            return render(request,"user/login.html")

        user = User.objects.filter(email=email).first()
        myemail = User.objects.filter(email="jjong015189@gmail.com").first()

        if user is None:
            return render(request,"user/login.html")

        return render(request,"portfolio/main.html",context=dict(user=user,myemail=myemail))

    def post(self,request):
        return render(request,"portfolio/main.html")


class Contact(APIView):
    def get(self,request):
        return render(request,"content/contact.html")

