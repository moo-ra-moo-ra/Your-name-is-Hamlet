from django.urls import path
from . import views

app_name = 'hamlet'

urlpatterns = [
    path('', views.index, name='index'),
    path('A_name_list', views.A_name_list, name='A_name_list'),
    path('A1_easy_name', views.A1_easy_name, name='A1_easy_name'),
    path('A2_global_name', views.A2_global_name, name='A2_global_name'),
    path('A3_pure_name', views.A3_pure_name, name='A3_pure_name'),
    path('A4_popular_name', views.A4_popular_name, name='A4_popular_name'),
    path('A5_fetus_name', views.A5_fetus_name, name='A5_fetus_name'),
    path('B_nick_name_list', views.B_nick_name_list, name='B_nick_name_list'),
    path('B1_random_nick_name', views.B1_random_nick_name, name='B1_random_nick_name'),
    path('B2_novel_nick_name', views.B2_novel_nick_name, name='B2_novel_nick_name'),
    path('C_others_list', views.C_others_list, name='C_others_list'),
    path('C1_random', views.C1_random, name='C1_random'),
    path('C2_lotto', views.C2_lotto, name='C2_lotto'),

]