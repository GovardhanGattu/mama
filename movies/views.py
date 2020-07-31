from django.shortcuts import render,redirect
from movies.models import *
from movies.forms import *

# Create your views here.
def movieform(request):
	form=Movieform()
	if request.method=="POST":
		data=Movieform(request.POST)
		data.save()
		if True:
			return redirect('movies')
	return render(request,'moviesform.html',{"form":form})

def movies(request):
	obj=Movies.objects.all()
	return render(request,'movies.html',{"obj":obj})

def trash(request,id):
	data=Movies.objects.get(id=id)
	data.delete()
	# return HttpResponse("Data Deleted Sucessfully...!!!")
	return redirect('movies')