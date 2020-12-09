from django.urls import path
from .views import signup,check_user_exists,loginView
from django.contrib.auth import views

urlpatterns = [
    # path('login/', views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('login/', loginView, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('check_username/', check_user_exists, name='check_user_exists'),
    path('reset/', views.PasswordResetView.as_view(template_name='account/password_reset.html',email_template_name='account/password_reset_email.html',subject_template_name='account/password_reset_subject.txt'),name='password_reset'),
    path('reset/done/', views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/complete/', views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),
    path('password-change/', views.PasswordChangeView.as_view(template_name='account/change_password.html') ,name='password_change'),
    path('password_change/done/',views.PasswordChangeDoneView.as_view(template_name='account/password_changed_done.html'),name='password_change_done'),


]
