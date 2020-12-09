from django.shortcuts import render, redirect
from .models import Maincategory, Subcategory, Products,Post_advertise,Blog
from .form import MaincategoryForm, SubcategoryForm,ProductsForm,AddsproductForm,AddBlogForm
from django.http import HttpResponse
from profiles.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from data.models import Feedback,Contact


# ------------------------------ Showing the Dealer Dashboard View------------------------------------------------#
@login_required
def dashboard(request):
    latest_blog = Blog.objects.all().order_by('-id')[:3]
    last_3_blog = reversed(latest_blog)
    return render(request, 'admin_template/index.html', {'notifications': last_3_blog})



# ------------------------------ Showing the Maincategory Data View ------------------------------------------------#
def show(request):
    all_cat = Maincategory.objects.all()
    return render(request, 'admin_template/showmaincategory.html', {"values": all_cat})



# ------------------------------ Showing the Subcategory Data View ------------------------------------------------#

def subcategory(request, product_id):
    all_sub = Maincategory.objects.get(id=product_id)
    return render(request, 'admin_template/showsubcategory.html', {'all_sub': all_sub})



# ------------------------------ Showing the Edit Subcategory Data Pendig View ------------------------------------------------#
def edit_subcat(request, id):
    subcat_id = Maincategory.objects.get(id=id)
    if request.method == "POST":
        form = SubcategoryForm(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('show', subcat_id.id)
    else:
        form = SubcategoryForm(instance=subcat_id)
    return render(request, 'admin_template/edit.html', {'form': form})



# ------------------------------ Deleting Subcategory Data View ------------------------------------------------#
def delete_subcategory(request, id):
    subcat_id = Subcategory.objects.get(id=id)
    subcat_id.delete()
    return redirect('subcategory', subcat_id.Maincategory_id)



# ------------------------------ Adding The Subcategory Data View ------------------------------------------------#
@login_required
def addsubcategory(request, id):
    user=User.objects.get(username=request.user.username)
    if user.user_type == 'dealer':
        prod = Maincategory.objects.get(id=id)
        if request.method == "POST":
            form = SubcategoryForm(request.POST,request.FILES)
            if form.is_valid():
                Subcategory = form.save(commit=False)
                Subcategory.created_by = request.user
                Subcategory.Maincategory = prod
                Subcategory.save()
                return redirect('subcategory', id)
        else:
            form = SubcategoryForm()
            return render(request, 'admin_template/add-subcategory.html', {"data": prod, "form": form})
    else:
        messages.error(request,"Only Dealer can added Subcategory ")
        return dashboard(request)



# ------------------------------ Showing the Products Data ------------------------------------------------#
def products(request,id):
    all_items=Products.objects.filter(product_name_id=id)
    return render(request, 'admin_template/showproducts.html', {"all_items": all_items})



# ------------------------------ Add Products Data View ------------------------------------------------#
def addproduct(request,id):
    items=Subcategory.objects.get(product_name_id=id)
    if request.method == "POST":
        form=ProductsForm(request.POST,request.FILES)
        if form.is_valid():
            Products=form.save(commit=False)
            Products.Subcategory=items
            Products.save()
            return redirect('products',id)
    else:
        form=ProductsForm()
        return render(request,'admin_template/add-products.html',{"data":items, "form":form})

#---------------------------------- SHOW ADDS ------------------------------------------------------#
def addvertise(request):
    all_adds = Post_advertise.objects.all()
    return render(request,'admin_template/showadds.html',{"all_adds":all_adds})

#--------------------------------- ADDING ADDS View ------------------------------------------------------#
def adds_advertise(request):
    if request.method == "POST":
        form=AddsproductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addvertise')
    else:
        form=AddsproductForm()
        return render(request,'admin_template/add-advertisement.html',{"form":form})


#--------------------------------- Showing the Blogs View --------------------------------------------------#
def blogshow(request):
    all_blog=Blog.objects.filter(created_by_id=request.user.id).order_by('-created_date')
    paginator = Paginator(all_blog, 3)
    page = request.GET.get('page')
    all_blog = paginator.get_page(page)

    try:
        all_blog = paginator.page(page)
    except PageNotAnInteger:
        all_blog= paginator.page(1)
    except EmptyPage:
        all_blog = paginator.page(paginator.num_pages)
    return render(request, 'admin_template/blogs.html',{"all_blog":all_blog})



#--------------------------------- Adding the Blogs View --------------------------------------------------#
def addblog(request):
    if request.method == "POST":
        form=AddBlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogshow')
    else:
        form=AddBlogForm()
        return render(request,'admin_template/add-blog.html',{"form":form})

# ------------------------------------Edit Blog View pendig -------------------------------------------------#
def edit_blog(request, id):
    created_by_id = Blog.objects.get(id=id)
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogshow')
    else:
        form = AddBlogForm(instance=  created_by_id)
    return render(request, 'admin_template/editblog.html', {'form': form})


#----------------------- Delete Blog View ----------------------------------------------------------------#
def delete_blog(request,blog_id):
    blog_id = Blog.objects.get(id=blog_id)
    blog_id.delete()
    return redirect('blogshow')

#------------------------ Notification Show ----------------------------------------------------------------#
def get_notifications(request):
    latest_blog = Blog.objects.all().order_by('-id')[:3]
    last_3_blog = reversed(latest_blog)

#--if click the read more then call this view --------------------------#
def blogdetails(request):
    all_blog=Blog.objects.all()
    return render(request,'blog-desc.html',{"blog":all_blog})

#-------------------Profile shows-----------------------#
def my_profile(request):
    return render(request,'admin_template/my-profile.html')


#-----------------Feedback shows dealer----------------#

def feedback_show(request):
    all_feedback=Feedback.objects.all()
    return render(request,'admin_template/show-feedback.html',{"Feed":all_feedback})

def contact_show(request):
    all_contact=Contact.objects.all()
    return render(request,'admin_template/contact-farmer.html',{"cont":all_contact})






