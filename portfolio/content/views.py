from django.http import HttpResponse
from django.views.generic import TemplateView

class MainView(TemplateView):                # 메인 화면
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return self.render_to_response(ctx)

class ProjectListView(TemplateView):         # 게시글 목록
    template_name = 'base.html'

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
