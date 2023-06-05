from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('canada',views.canada,name='canada'),
    path('franchise',views.franchise,name='franchise'),
    path('award',views.award,name='award'),
    path('presencemedia',views.presencemedia,name='presencemedia'),
    path('photogallery',views.photogallery,name='photogallery'),
    path('blog',views.blog,name='blog'),
    path('branches',views.branches,name='branches'),
    path('ielts',views.ielts,name='ielts'),
    path('migratecanada',views.migratecanada,name='migratecanada'),
    path('readmore',views.readmore,name='readmore'),
    path('seminar',views.seminar,name='seminar'),
    path('signup',views.signup,name='signup'),
    path('register',views.register,name='register'),

]
