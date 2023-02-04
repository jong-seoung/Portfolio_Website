from django.http import HttpResponse
from django.views.generic import TemplateView

class Base(TemplateView):                # base
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return self.render_to_response(ctx)

class MainView(TemplateView):                # 메인 화면
    template_name = 'main.html'

class About(TemplateView):                # About
    template_name = 'about.html'

class Aboutme(TemplateView):              # About me
    template_name = 'aboutme.html'
    
class Education(TemplateView):            # Education
    template_name = 'edu.html'

class Career(TemplateView):               # career
    template_name = 'carerr.html'

class FrontEnd(TemplateView):               # Front
    template_name = 'front.html'

class BackEnd(TemplateView):               # Back
    template_name = 'back.html'

class Etc(TemplateView):               # Etc
    template_name = 'etc.html'


class ProjectListView(TemplateView):         # 프로젝트
    template_name = 'project.html'

    def get(self, request, *args, **kwargs):
        ctx = {}                             # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)


class ProjectDetailView(TemplateView):       # 게시글 상세
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return self.render_to_response(ctx)


class ProjectCreateUpdateView(TemplateView):  # 게시글 추가, 수정
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):  # 화면 요청
        ctx = {}
        return self.render_to_response(ctx)

    def post(self, request, *args, **kwargs): # 액션
        ctx = {}
        return self.render_to_response(ctx)
