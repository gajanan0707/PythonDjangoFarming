from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,authenticate
from profiles.models import User
from admin_owner.models import Post_advertise,Blog
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from data import form
from .form import ContactFrom,FeedbackForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from .form import FeedbackForm,ComplaintForm


#--user show view ---------#
def index(request):
    return render(request,'index.html')

#---------about view --------------------#
def about(request):
    return  render(request,'about.html')


#----------Blog View shows-----------------#
def blog(request):
    all_blog=Blog.objects.all()
    paginator = Paginator(all_blog, 3)
    page = request.GET.get('page')
    all_blog = paginator.get_page(page)

    try:
        all_blog = paginator.page(page)
    except PageNotAnInteger:
        all_blog= paginator.page(1)
    except EmptyPage:
        all_blog = paginator.page(paginator.num_pages)
    return  render(request,'blog.html',{"all_blog":all_blog})


#-------------Shows the Blog full---------------------#
def single(request):
    all_blog =Blog.objects.all()
    return  render(request,'single.html',{"all_blog":all_blog})


#-----------------Shows the Service---------------------#
def complaintfarmer(request):
    return render(request, 'complaintpage.html')

#-------------------Contact View ----------------------#
def contact(request):
    if request.method == "POST":
        cont=ContactFrom(request.POST)
        if cont.is_valid():
            cont.save()
            return redirect('index')
    else:
        cont = ContactFrom()
    return render(request, 'contact.html', {'form': cont})



#----------Feedback View--------------#
def feedback(request,blog_id):
    blogid=Blog.objects.get(id=blog_id)
    print(blogid)
    if request.method == "POST":
        f=FeedbackForm(request.POST)
        if f.is_valid():
            f=form.save(commit=False)
            f.title=blogid
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return render(request,'thanks.html')
    else:
        f= FeedbackForm()
    return  render(request,'feedback-form.html', {'form': f,'blogid':blogid})


def complate_view(request):
    if request.method == "POST":
        comp=ComplaintForm(request.POST)
        if comp.is_valid():
            comp.save()
            return redirect('index')
    else:
        comp = ComplaintForm()
    return render(request, 'complaintpage.html', {'form': comp})





















