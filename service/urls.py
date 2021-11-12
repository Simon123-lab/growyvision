from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.account_registration, name='account_registration'),
    path('login',views.account_login, name='account_login'),
    path('logout',views.logout_user, name='logout'),
    path('cpanel',views.client_panel, name='client_panel'),
    path('panel',views.user_panel, name='user_panel'),
    path('likes',views.post_likes, name='likes'),
    path('order',views.client_order, name='order'),
    path('videos',views.watch_videos, name='videos'),
    path('follows',views.page_follows, name='follows'),
    path('reviews',views.add_review, name='reviews'),
    path('entry',views.contest_submition, name='entry'),
    path('verify',views.confirm_views, name='verify'),
    path('withdraw',views.withdraw, name='withdraw'),
    path('faq',views.FAQs, name='faq'),
    path('confirm_task/',views.confirm_task, name='confirm_task'),
    path('feedback',views.feedback,name='feedback'),
    path('watch',views.watch,name='watch'),
    
    # reset password implementation
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
    
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_STORE)