from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import profile,paper,payment,Notification
from .form import profileform,paperform,signupform,paper_edit,profile_update
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy

@login_required
def create(request):
    qs=profile.objects.filter(user__iexact=request.user.username)
    print(qs)
    if qs==0:
        form=profileform(request.POST or None)
        if form.is_valid(): 
            instance=form.save()
            instance.user=request.user.username
            instance.save()

            return HttpResponseRedirect(reverse('paper'))
        context={'pro':form}
        return render(request,"create.html",context)
    return HttpResponseRedirect(reverse('dashboard'))

@login_required
def update_profile(request,pk=None):
    qs=get_object_or_404(profile, id=pk)
    form=profile_update(request.POST or None,instance=qs)
    if form.is_valid():
        instance=form.save()
        instance.user=request.user.username
        instance.save()
        return HttpResponseRedirect(reverse('dashboard'))
    context={'pro':form}
    return render(request,"create.html",context)
    #return HttpResponseRedirect(reverse('dashboard'))

@login_required
def create_paper(request):
    form=paperform(request.POST or None,request.FILES or None)
    print(form)
    if form.is_valid():
        instance=form.save()
        instance.user=request.user.username
        instance.save()

        return HttpResponseRedirect(reverse('dashboard'))
    context={'pro':form}
    return render(request,"create_paper.html",context)


@login_required
def dashboard(request): 
    #instance=profile.objects.all()[::-1]
    objects=paper.objects.filter(user__iexact=request.user.username)[::-1]
    print(objects)
    p=profile.objects.filter(user__iexact=request.user.username)
    context={"instan":objects,"fix":p}
    print(p)

    return render(request,"dadhboard.html",context)

    
@login_required
def update(request,pk=None):
    qs=get_object_or_404(paper,id=pk)
    if qs and request.user.username==qs.user:
        form=paper_edit(request.POST or None, request.FILES or None,instance=qs)
        if form.is_valid():
            instance=form.save()
            instance.user=request.user.username
            instance.save()

            return HttpResponseRedirect(reverse('dashboard'))
        context={'pro':form}
        return render(request,"create_paper.html",context)
    return HttpResponseRedirect(reverse('dashboard'))

@login_required
def delete(request,pk=None):
    qs=get_object_or_404(paper,id=pk)
    if qs and request.user.username==qs.user:
        qs.delete()
        return HttpResponseRedirect(reverse('dashboard'))
    return HttpResponseRedirect(reverse('dashboard'))




# Create your views here.
