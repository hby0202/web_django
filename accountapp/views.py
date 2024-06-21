from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        # 파라미터
        temp = request.POST.get('hello_world_input')

        # DB 객체 연결
        new_hello_world = HelloWorld()
        # DB 컬럼 입력
        new_hello_world.text = temp
        # DB 저장
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # url을 만들어주는 함수 :reverse
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})