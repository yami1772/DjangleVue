from django.urls import path
from . import views

urlpatterns = [
    # ex: /backend/
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('insert/', views.insert),
    path('find/', views.find),
    path('modify/<int:studentNum>/', views.modify),
    path('delete/<int:studentNum>/', views.delete),
    path('show_list/', views.show_list),
    path('addStu/', views.addStu),

]