from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def ajaxfrm(request):
    return render(request, 'ajaxapp/ajaxfrm.html')

def ajaxmeet(request):
    meets = [
        '금융 SW 교육 무상 제공및 교육 기기 무상 대여',
        'KB국민은행 취업 박람회 참가및 취업지원 서비스 제공',
        '프로젝트 우수 참가자 KB국민은행 해외 지점 방문',
        '금융 SW 교육 무상 제공및 교육 기기 무상 대여',
        'KB국민은행 취업 박람회 참가및 취업지원 서비스 제공',
        '프로젝트 우수 참가자 KB국민은행 해외 지점 방문',
        '금융 SW 교육 무상 제공및 교육 기기 무상 대여',
        'KB국민은행 취업 박람회 참가및 취업지원 서비스 제공',
        '프로젝트 우수 참가자 KB국민은행 해외 지점 방문',
        '금융 SW 교육 무상 제공및 교육 기기 무상 대여',
        'KB국민은행 취업 박람회 참가및 취업지원 서비스 제공',
        '프로젝트 우수 참가자 KB국민은행 해외 지점 방문',
    ]
    context = {
        'meets': meets
    }
    return JsonResponse(context)
def ajaxschedule(request):
    edus = [
        '2022.7.4 ~ 2020.7.15  :: 모집',
        '2022.7.18 ~ 2020.7.28  :: 선발',
        '2022.8.01 ~ 2020.10.28  :: 교육',
        '2022.10 ~ 2020.11  :: 취업 컨설팅'
    ]
    context = {
        'edus': edus
    }
    return JsonResponse(context)