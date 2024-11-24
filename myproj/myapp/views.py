from django.shortcuts import render , redirect
from myapp.models import users_log_psw
from myapp.models import katalog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        new = users_log_psw(log = data["login"], psw = data["pass"], name = data["name"])
        new.save()

    res = users_log_psw.objects.all()
    return render(request, "index.html", {"test": res})



def second(request):
    data = katalog.objects.all()
    return render(request,"second.html", {"test":data})

def item(request,itemid):
    data = katalog.objects.filter(id = itemid)
    data_all = katalog.objects.all()
    return render(request,"item.html", {"data":data,"data_all":data_all})



def reg(request):
    if request.method == "POST":
        data = request.POST
        new = User.objects.create_user(data['lgn'], "",data['psw'])
        new.save()
    return render(request,"reg.html")

def auth(request):
    if request.method =="POST":
        data = request.POST
        user = authenticate(username = data["lgn"], password = data["psw"])
        if user is not None:
            request.session["true"] = user.id 
            return redirect(second)
        
        else:
            return redirect(auth)
    else:
        return render(request, "auth.html")
    

