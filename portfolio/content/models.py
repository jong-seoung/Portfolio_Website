from django.db import models

class Project(models.Model):
    title = models.CharField('제목', max_length=126, null=False)
    content = models.TextField('프로젝트 설명', null=False)
    impression = models.TextField('소감', null=False)
    skill = models.TextField('기술', null=False)
    github = models.URLField()
    blog = models.URLField()
    demo = models.URLField()
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    created_at.editable = True
    
    # 데이터 표시 형식 변경
    def __str__(self): 
        return '[{}] {}'.format(self.id, self.title)