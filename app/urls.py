from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.Register),
    path('view_student', views.view_student),
    path('view_student_course', views.view_course)
]
