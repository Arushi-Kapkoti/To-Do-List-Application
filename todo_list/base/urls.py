from django.urls import path
from . views import TaskList, TaskDetail, TaskCreate, TaskUpdate,DeleteView, CustomLoginView, logout, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login/',CustomLoginView.as_view(),name='login'),
    #path('logout/',LogoutView.as_view(next_page='login',http_method_names=['get', 'post']),name='logout'),
    path('logout/',logout,name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('', TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(),name='task'),
    path('task-create/', TaskCreate.as_view(),name='task-create'),
    path('taks-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('taks-delete/<int:pk>/',DeleteView.as_view(),name='task-delete'),

]

#path('logout/',LogoutView.as_view(http_method_names=['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace'], next_page='login', redirect_field_name='next'),name='logout'),