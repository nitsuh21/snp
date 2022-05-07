from pydoc import text
from unittest import TextTestResult
from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def feed(request):
    posts = Post.objects.all().order_by("-id")
    context={
                'Posts':posts
            }
    return render(request,'index.html',context)
def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                text = request.POST.get('text')
                attachment = request.POST.get('attachment')
                sharedlink = request.POST.get('sharedlink')
                print(text)
                print(attachment)
                print(sharedlink)
                post = Post(text=text,attachment=attachment,sharedlink=sharedlink)
                post.save()
                return redirect('feed')
            except Exception as e:
                print(e)
                return redirect('feed')
        else:
            return redirect('feed')
    else:
        return redirect('login')
        
        