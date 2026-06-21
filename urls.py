from django.urls import path
from.import views
urlpatterns=[
    path('',views.register,name="reg"),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('display/',views.display,name='display'),
    path('list_of_tasks/',views.list_of_tasks,name='list_of_tasks'),
    path('edit/<int:id>/',views.edit_tasks,name='edit'),
    path('delete/<int:id>/',views.delete_tasks,name='delete'),
    path('history/',views.history,name='history'),
]