from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^v1/projects/(?P<pk>[0-9]+)$',
        views.get_delete_update_project,
        name='get_delete_update_project'
    ),
    url(
        r'^v1/projects/$',
        views.get_post_projects,
        name='get_post_projects'
    )
]
