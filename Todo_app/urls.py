from django.urls import path
from .views import Tasklist,TaskDetail,TaskCreate,TaskUpdate,TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',Tasklist.as_view(), name="tasks"),
    path('taskCreate/',TaskCreate.as_view(), name="taskCreate"),
    path('taskDetail/<int:pk>/', TaskDetail.as_view(), name="taskDetail"),
    path('taskUpdate/<int:pk>/', TaskUpdate.as_view(), name="taskUpdate"),
    path('taskDelete/<int:pk>/', TaskDelete.as_view(), name="taskDelete"),

    path('login/',CustomLoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    # path('register/', RegisterPage.as_view(), name="register"),

]