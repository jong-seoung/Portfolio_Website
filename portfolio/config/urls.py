"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from content.views import Base, MainView, About, Aboutme, Education, Career, FrontEnd, BackEnd, Etc, ProjectListView

# ProjectListView, ProjectDetailView, ProjectCreateUpdateView

# static 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', Base.as_view()),

    path('', MainView.as_view()),
    path('about/', About.as_view()),
    path('about/aboutme/', Aboutme.as_view()),
    path('about/education/', Education.as_view()),
    path('about/career/', Career.as_view()),
    path('about/skill/frontend', FrontEnd.as_view()),
    path('about/skill/backend', BackEnd.as_view()),
    path('about/skill/etc', Etc.as_view()),
    path('project/', ProjectListView.as_view()),
    # path('project/<project_id>/', ProjectDetailView.as_view()),
    # path('project/<project_id>/update', ProjectCreateUpdateView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)