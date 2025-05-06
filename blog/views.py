from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
from blog.models import (
    Blog,
)

# Create your views here.
def index(request):
    return render(request, 'blog.html')

def NewsWeb(request):
    recent_blogs = Blog.objects.all().order_by("-created_at")         # all().order_by("created_at") -- sort data according to date & ("-created_at"")--it will show recent to old sorts

    context = {
        'recent_blogs':recent_blogs,    
    }
        
    return render(request, 'blog.html', context)

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    recent_blogs = Blog.objects.all().exclude(id=blog_id).order_by("-created_at")[:6]


    context = {
        'blog':blog,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'blog_details.html', context)

def contact_form(request):
    if request.method == 'POST':
        print('POST sucessful')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=subject,
                message=f"{name} - {email} - {message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            messages.error(request, "There is a problem in Sending Message! Please try again")
        else:
            messages.success(request, "Message Sent Successfully")
            return redirect('/')
    
