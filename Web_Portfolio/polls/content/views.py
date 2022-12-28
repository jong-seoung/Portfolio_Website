from django.shortcuts import render
from rest_framework.views import APIView
from polls.user.models import User
from uuid import uuid4
from config.settings import MEDIA_ROOT
import os
from .models import Project, Like
from rest_framework.response import Response
from django.core.mail import EmailMessage

class Main(APIView):
    def get(self,request):
        email = request.session.get('email',None)

        if email is None:
            return render(request,"user/login.html")

        user = User.objects.filter(email=email).first()
        myemail = User.objects.filter(email="jjong015189@gmail.com").first()

        if user is None:
            return render(request,"user/login.html")
        
        project_object_list = Project.objects.all().order_by('-id') #select * from content_feed;
        project_list=[]
        

        for project in project_object_list:
            
            like_count = Like.objects.filter(project_id=project.id, is_like=True).count()
            is_liked = Like.objects.filter(project_id=project.id, email=email,is_like=True).exists()
            project_list.append(dict(id = project.id,
                image=project.image,
                content=project.content,
                like_count=like_count,
                profile_image=user.profile_img,
                nickname=user.nickname,
                is_liked = is_liked,
                project_name=project.project_name,
                url_blog=project.url_blog,
                url_github=project.url_github,
                ))
        return render(request,"portfolio/main.html",context=dict(project_list=project_list,user=user,myemail=myemail))

    def post(self,request):
        return render(request,"portfolio/main.html")
    



class Contact(APIView):
    def get(self,request):
        email = request.session.get('email',None)

        if email is None:
            return render(request,"user/login.html")

        user = User.objects.filter(email=email).first()
        myemail = User.objects.filter(email="jjong015189@gmail.com").first()

        if user is None:
            return render(request,"user/login.html")

        return render(request,"content/contact.html",context=dict(user=user,myemail=myemail))
    
class Sendmail(APIView):
    def get(self,request):
        contactme_namebox = request.GET.get('contactme_namebox')
        contactme_emailbox = request.GET.get('contactme_emailbox')
        contactme_message_textbox = request.GET.get('contactme_message_textbox')

        email = EmailMessage(
            '웹에서 온 메일입니다',
            '%s\n %s\n %s\n' %
            (contactme_namebox, contactme_emailbox, contactme_message_textbox),
            to=['jjong015189@naver.com'],  
        )
        email.send()

        return render(request,"content/contact.html")



class UploadProject(APIView):
    def post(self,request):

        # 파일 불러오기
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        # 파일을 읽어서 파일을 만들기
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        email = request.session.get('email',None)
        project_name = request.data.get('project_name')
        url_blog = request.data.get('url_blog')
        url_github = request.data.get('url_github')

        # 피드에 저장
        Project.objects.create(image=image, content=content,email=email,project_name=project_name,
        url_github=url_github,url_blog=url_blog,)


        return Response(status=200)

class ToggleLike(APIView):
    def post(self,request):
        project_id = request.data.get('project_id',None)
        favorite_text = request.data.get('favorite_text',True)

        if favorite_text == 'favorite_border':
            is_like = True
        else:
            is_like = False
        email = request.session.get('email',None)

        like = Like.objects.filter(project_id=project_id,email=email).first()

        if like:
            like.is_like = is_like
            like.save()
        else:
            Like.objects.create(project_id=project_id, is_like=is_like,email=email)

        return Response(status=200)