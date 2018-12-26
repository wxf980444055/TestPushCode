from typing import Dict, Any

from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

usr_list = [
    {"user": "jack", "pwd": "abc"},
    {"user": "todm", "pwd": "ABC"},
]


def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("nide qing qiu wo shou dao le!")
    # return render(request, "index.html")

    if request.method == "POST":
        usrname = request.POST.get("usrname", None)
        password = request.POST.get("password", None)
        print(usrname, password)
    return render(request, "index.html",)

    # if request.method == "POST":
    #     username = request.POST.get("username", None)
    #     password = request.POST.get("password", None)
    #     print(username, password)
    #     temp = {"user": username, "pwd": password}
    #     usr_list.append(temp)
    #     return render(request, "index.html", {"datat": usr_list})
