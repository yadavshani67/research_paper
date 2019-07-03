from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import profile,paper,payment,Notification
from .form import profileform,paperform
def create(request):
    form=profileform(request.POST or None)
    if form.is_valid():
        instance=form.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/paper')
    context={'pro':form}
    return render(request,"create.html",context)

def create_paper(request):
    form=paperform(request.POST or None,request.FILES or None)
    print(form)
    if form.is_valid():
        #print(form)
        instance=form.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/dashboard")
    context={'pro':form}
    return render(request,"create_paper.html",context)

def dashboard(request):
    #objects=profile.objects.all()[::-1]
    objects=paper.objects.all()
    print(objects)
    context={'instan':objects}

    return render(request,"dadhboard.html",context)

# Create your views here.
