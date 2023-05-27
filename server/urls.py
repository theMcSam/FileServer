from django.urls import path, include
from . import views

urlpatterns = [
    path("/", views.webroot, name="webroot"),
    path("home", views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('resetpassword', views.password_reset, name='resetpassword'),
    path('token/<str:user>/<str:token>', views.password_reset_confirm, name='token'),
    path('activate/<str:user>/<str:token>', views.activate_account, name="activate")
]
