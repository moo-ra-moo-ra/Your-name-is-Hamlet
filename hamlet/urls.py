from django.urls import path
from . import views

app_name = 'hamlet'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('moora_project_list/', views.moora_project_list, name='moora_project_list'),
    path('A_name_list/', views.A_name_list, name='A_name_list'),
    path('A1_easy_name/', views.A1_easy_name, name='A1_easy_name'),
    path('result_A1/', views.result_A1, name='result_A1'),
    path('A2_global_name/', views.A2_global_name, name='A2_global_name'),
    path('result_A2/', views.result_A2, name='result_A2'),
    path('A3_pure_name/', views.A3_pure_name, name='A3_pure_name'),
    path('result_A3/', views.result_A3, name='result_A3'),
    path('A4_popular_name/', views.A4_popular_name, name='A4_popular_name'),
    path('result_A4/', views.result_A4, name='result_A4'),
    path('A5_fetus_name/', views.A5_fetus_name, name='A5_fetus_name'),
    path('A5_1_pure_fetus_name/', views.A5_1_pure_fetus_name, name='A5_1_pure_fetus_name'),
    path('result_A5/', views.result_A5, name='result_A5'),
    path('A5_2_well_hearded_fetus_name/', views.A5_2_well_hearded_fetus_name, name='A5_2_well_hearded_fetus_name'),
    path('result_A52/', views.result_A52, name='result_A52'),
    path('B_nick_name_list/', views.B_nick_name_list, name='B_nick_name_list'),
    path('B1_random_nick_name/', views.B1_random_nick_name, name='B1_random_nick_name'),
    path('result_B1/', views.result_B1, name='result_B1'),
    path('B2_novel_nick_name/', views.B2_novel_nick_name, name='B2_novel_nick_name'),
    path('result_B2/', views.result_B2, name='result_B2'),
    path('C_others_list/', views.C_others_list, name='C_others_list'),
    path('C1_random/', views.C1_random, name='C1_random'),
    path('C1_random_2/', views.C1_random_2, name='C1_random_2'),
    path('result_C1/', views.result_C1, name='result_C1'),
    path('C2_lotto/', views.C2_lotto, name='C2_lotto'),
    path('C2_1_random_lotto/', views.C2_1_random_lotto, name='C2_1_random_lotto'),
    path('C2_lotto2/', views.C2_lotto2, name='C2_lotto2'),
    path('C2_2_unit_lotto/', views.C2_2_unit_lotto, name='C2_2_unit_lotto'),
    path('result_C2/', views.result_C2, name='result_C2'),
    path('result_C22/', views.result_C22, name='result_C22'),

]