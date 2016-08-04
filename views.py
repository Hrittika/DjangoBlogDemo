from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


from .forms import PostForm
# Create your views here.
from .models import Post

def blog_create(request):
	form= PostForm(request.Post or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
	    messages.error(request,"Not Successfully Created")	
	#if request.method == "POST":
	#	print request.POST.get("body")
	#	print request.POST.get("title")

	context = {
       "form" : form,
     

	}

	return render(request,"post_form.html",context)

def blog_detail(request, id):
	instance = get_object_or_404(Post, id=id)

	context = {
       "title" : instance.title,
       "instance" : instance,

	}

	return render(request,"blog_detail.html",context)


def blog_list(request):
	queryset = Post.objects.all()
	context = {
	   "object_list": queryset,
       "title" : "List"

	}

	return render(request,"base.html",context)

def blog_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form= PostForm(request.Post or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"<a href='#'>Item</a> Saved")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
       "title" : instance.title,
       "instance" : instance,
       "form" : form,

	}

	return render(request,"blog_form.html",context)

def blog_delete(request):
	return HttpResponse("<h1>Hello</h1>")



