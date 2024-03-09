from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('detail/<int:todo_id>',detail_todo,name='detail')
]
