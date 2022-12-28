from django.db import models

class Project(models.Model):
    content = models.TextField() # 글 내용
    image = models.TextField() # 피드 이미지
    email = models.EmailField(default='') # 글쓴이
    project_name = models.TextField() # 프로젝트 제목
    url_blog = models.TextField() # 블로그 url
    url_github = models.TextField() # 깃허브 url

class Like(models.Model):
    project_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_like = models.BooleanField(default=True)