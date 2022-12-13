from django.shortcuts import render
from rest_framework.views import APIView
from polls.user.models import User
from uuid import uuid4
from config.settings import MEDIA_ROOT
import os
from .models import Project
from rest_framework.response import Response

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
            user = User.objects.filter(email=project.email).first()
            
        #     like_count = Like.objects.filter(project_id=project.id, is_like=True).count()
        #     check_liked = Like.objects.filter(project_id=project.id, email=email,check_like=True).exists()
            project_list.append(dict(id = project.id,
                image=project.image,
                content=project.content,
        #         like_count=like_count,
                profile_image=user.profile_img,
                nickname=user.nickname,
        #         check_liked = check_liked,
                hashtag=project.hashtag,
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
        hashtag = request.data.get('hashtag')
        project_name = request.data.get('project_name')
        url_blog = request.data.get('url_blog')
        url_github = request.data.get('url_github')

        # 피드에 저장
        Project.objects.create(image=image, content=content,email=email,hashtag=hashtag,project_name=project_name,
        url_github=url_github,url_blog=url_blog,)


        return Response(status=200)

