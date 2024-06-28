from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
# def bloglist(request):
#     post=Post.objects.all()
#     return render(request,"blog/bloglist.html",{"posts":post})

class bloglists(ListView): #CBV starts here to List the view
    model=Post
    template_name="blog/bloglist.html"
    context_object_name="posts"
    success_url=reverse_lazy('bloglist') #bloglist hme bloglist matlab ="" ke url pe bhej dega, urls me jaake dekho "" ko

class blogdetails(DetailView): #individual details batao sabka
    model=Post
    template_name="blog/blogdetail.html"
    context_object_name="posts"

class createpost(CreateView):
    model=Post
    template_name='blog/form.html'
    fields=["title","content"] #post yahin pe create ho rha hai
    success_url=reverse_lazy('bloglist')

class updatepost(UpdateView):
    model=Post
    template_name='blog/form.html'
    fields=["title","content"] #post yahin pe create ho rha hai
    success_url=reverse_lazy('bloglist')

class deletepost(DeleteView):
    model=Post
    template_name='blog/deletepost.html'
    success_url=reverse_lazy('bloglist')