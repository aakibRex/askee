from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.urls import reverse

from accounts.models import users
from app.models import clgInfo


def registration(request):
    clg_names = clgInfo.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        clg_name = request.POST['clgName']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = users.objects.create_user(name=name, email=email, college_name=clg_name,
                                         password=password1)
        user.save()
        user = auth.authenticate(email=email, password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        # return redirect("/")
    else:
        return render(request, 'registration.html', {'clg_names': clg_names})


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password']

        user = auth.authenticate(email=email, password=password1)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                print(request.POST.get('next'))
                return redirect(request.POST.get('next'))
            else:
                return redirect("/")
        else:
            return redirect("/")
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def del_acc(request):
    if request.user.is_authenticated:
        # print(request.user.name,request.user.id)
        user_id = request.user.id
        user = users.objects.filter(id=user_id)
        # auth.logout(request)
        user.delete()
    return redirect("/")
