from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import profile,paper,payment,Notification
from .form import profileform
def create(request):
    form=profileform(request.POST or None)
    if form.is_valid():
        instance=form.save()
        return HttpResponseRedirect('http://127.0.0.1:8000:/admin/')
    context={'pro':form}
    return render(request,"create.html",context)

# Create your views here.
