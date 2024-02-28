from django.urls import path
from home import views

urlpatterns=[
    
    # Admin Url
    path('', views.inicio, name="inicio"),

    # Principal Url's
    path('about/', views.about, name="about"),
    path('skills/', views.skills, name="skills"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('services/', views.services, name="services"),
    path('blog/', views.blog, name="blog"),
    path('blog/<str:slug>', views.entry, name="entry"),
    path('contact/', views.contact, name="contact"),


    # singIn and singUp Url's
    path('confirm/<int:user_id>/<str:token>/', views.confirm_account, name='confirm_account'),
    path('singUp/', views.singUp, name="singUp"),
    path('signIn/', views.signIn, name="signIn"),
    path('logout/', views.logout_session, name='logout')
]