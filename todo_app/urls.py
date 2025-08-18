from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name="home"),
    path('addtask/',views.addtask,name="newtask"),
    path('completedtasks/',views.completedtasks,name="completedtask"),
]
