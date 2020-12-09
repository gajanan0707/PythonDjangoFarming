from django.urls import path
from admin_owner import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('showmaincategory/',views.show,name='show'),
    path('showsubcategory/<int:product_id>/',views.subcategory,name='subcategory'),
    path('add-subcategory/<int:id>/',views.addsubcategory,name='addsubcategory'),
    path('edit/<int:id>/',views.edit_subcat, name='edit_subcat'),
    path('delete/<int:id>/', views.delete_subcategory, name='delete_subcategory'),
    path('subcategory/<int:id>/',views.products,name='products'),
    path('add-products/<int:id>/',views.addproduct,name='addproducts'),
    path('showadds/',views.addvertise,name='addvertise'),
    path('add-advertisement',views.adds_advertise,name='adds_advertise'),
    path('blogs',views.blogshow,name='blogshow'),
    path('add-blog',views.addblog,name='addblog'),
    path('editblog/<int:id>/',views.edit_blog,name='edit_blog'),
    path('deleteblog/<int:blog_id>/',views.delete_blog,name='delete_blog'),
    path('get-notification/',views.get_notifications, name='get_notifications'),
    path('blog-desc/',views.blogdetails,name='blogdetails'),
    path('my-profile/',views.my_profile,name='my_profile' ),
    path('show-feedback/',views.feedback_show,name='feedback_show'),
    path('contact-farmer/',views.contact_show,name='contact_show'),
]