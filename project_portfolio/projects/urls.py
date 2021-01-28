from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(
        r'^api/v1/projects/(?P<pk>[0-9]+)$',
        views.get_delete_update_project,
        name='get_delete_update_project'
    ),
    url(
        r'^api/v1/projects/$',
        views.get_post_projects,
        name='get_post_projects'
    ),
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
