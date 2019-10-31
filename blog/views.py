from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
now = datetime.datetime.now()
# Create your views here.
def data(request): 
    return render(request,'blog/data.html')
class PostListView(ListView):
    model =Post
    template_name='blog/about.html'
    context_object_name='posts'
    ordering=['-date_posted']
class PostDetailView(LoginRequiredMixin,DetailView):
    model =Post
class PostCreateView(LoginRequiredMixin,CreateView):
    model =Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model =Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    def test_fun(self):
        if self.request.user == post.author:
            return True
        return False
class PostDetailView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model =Post
    def test_fun(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False       

def about(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/about.html',context)

