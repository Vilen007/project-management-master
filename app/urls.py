from django.urls import path
from . import views


path("login/", views.login, name="login")

urlpatterns = [
    path('projects', views.projects, name="projects"),
    path('missions', views.missions, name="missions"),
    path('', views.login, name="login"),
    path('logout',views.logoutt, name="logout"),
    path('tasks/<int:pk>/', views.tasks, name='tasks'),

    path('upload/', views.upload, name='upload-project'),
    path('tasks/<int:pk>/uploadtask/', views.uploadtask, name='upload-task'),

    path('details/<int:pk>/', views.project_details, name='details'),

    path('details/<int:project_id>/updateproject', views.update_project),
    path('details/<int:pk>/delete/', views.ProjectDelete.as_view(), name="delete_project"),

    path('tasks/<int:proj>/delete/<int:pk>', views.TaskDelete.as_view(), name="delete_task"),
    # path('details/update/<int:project_id>', views.update_project),
    # path('details/delete/<int:project_id>', views.delete_project),
    path('tasks/<int:proj>/updatetask/<int:pk>', views.update_task),
    path('task_details/<int:pk>', views.detail_task ,name='detailstask'),
    path('comment/<int:pk>',views.taskComment),

    path('settings', views.getUser, name="settings"),

    path('infos/<int:pk>/', views.info, name='infos'),
    path('infos/<int:pk>/uploadinfo/', views.uploadinfo, name='upload-info'),
    path('infos/<int:proj>/updateinfo/<int:pk>', views.update_info),

    path('gettable', views.gettable, name="showtable"),
    # path('comment/<int:id>/', views.getcomment, name="comment")


    path('dashboard/', views.dashboard, name='dashboard'),

    path('view/', views.projectView, name="projectview"),

    path('userview/', views.userView, name="userview"),
]

