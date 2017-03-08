from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from polls.models import *
from django.urls import reverse
from .forms import *

def index(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print 'clean_data',form.cleaned_data
            return HttpResponse('ok')
        else:

            if form.errors.has_key("__all__"):
                form._errors['all'] = form.error_class([form.errors["__all__"]])


            print 'error',form.errors
            print 'error',form.errors.as_json()
            print 'error',form.errors.as_data()


    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})


def server_list(request):

    if request.method == 'GET':
        server_list = Host.objects.all()


        return render(request,'server_list.html',{'server_list':server_list})
    elif request.method == 'POST':
        pass


def server_detail(request,server_id):
    server_obj = Host.objects.get(id=server_id)

    if request.method == 'GET':
        form = HostModelForm(instance=server_obj)
        return render(request,'server_detail.html',{'form':form,'server_id':server_id})


    elif request.method == 'POST':
        form = HostModelForm(request.POST,instance=server_obj)
        if form.is_valid():
            form.save()



        # return HttpResponseRedirect(reverse('server_detail',kwargs={'server_id':server_obj.id}))
        return HttpResponseRedirect(reverse('server_list'))
