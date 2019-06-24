from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def moora_project_list(request):
    return render(request, 'moora_project_list.html')


def A_name_list(request):
    return render(request, 'A_name_list.html')


def A1_easy_name(request):
    return render(request, 'A1_easy_name.html')


def A2_global_name(request):
    return render(request, 'A2_global_name.html')


def A3_pure_name(request):
    return render(request, 'A3_pure_name.html')


def A4_popular_name(request):
    return render(request, 'A4_popular_name.html')


def A5_fetus_name(request):
    return render(request, 'A5_fetus_name.html')


def B_nick_name_list(request):
    return render(request, 'B_nick_name_list.html')


def B1_random_nick_name(request):
    return render(request, 'B1_random_nick_name.html')


def B2_novel_nick_name(request):
    return render(request, 'B2_novel_nick_name.html')


def C_others_list(request):
    return render(request, 'C_others_list.html')


def C1_random(request):
    return render(request, 'C1_random.html')


def C2_lotto(request):
    return render(request, 'C2_lotto.html')
