from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
 
def loginin(request):
    if request.method=='POST' :
        uname=request.POST['username']
        pword=request.POST['password']

        user=authenticate(username=uname,password=pword)


        if user is not None:
            login(request, user)
            return JsonResponse({"message":"loged in"})
        else:
            return HttpResponse("error")
    return render(request, "auth/login.html")


