from django.shortcuts import render
from .models import Reply_of_Massage

# Create your views here.

def wait(request):
    if request.method == "POST":
        name = request.POST.get('naam')
        massage = request.POST.get('mymassage')
        date = request.POST.get('datetime')
        replay = request.POST.get('herreplay')
        replaysave = Reply_of_Massage(name = name ,date = date , mymassage = massage , replay = replay)
        replaysave.register()
    return render(request,'wait.html')



