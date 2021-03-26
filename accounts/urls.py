from django.urls import path, reverse

from . import views
app_name = 'app'

urlpatterns = [

    path('register',views.registration,name='register'),
    path('login',views.login_user,name='login_user'),
    path('logout',views.logout,name='logout'),
    path('del_user',views.del_acc,name='delete_account')


]