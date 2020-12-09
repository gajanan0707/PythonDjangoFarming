from django.contrib import admin
from .models import Maincategory,Subcategory,Products,Post_advertise,Blog
# Register your models here.

class MaincategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_type','product_desc','create_date')
    list_filter = ('product_type',)
    search_fields = ('id', 'product_type')

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_desc', 'created_by','product_type', 'created_at')
    list_filter = ('product_name',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','subproduct','brand_name','product_name','product_type','size','price')
    list_filter = ('subproduct',)


class PostAddsAdmin(admin.ModelAdmin):
    list_display = ('id','product_type','product_name','product','price','contact_supplier')
    list_filter = ('product_type',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','blog_desc','blog_image','full_desc','status','cat_blog')
    search_fields = ['title', 'content']
    list_filter = ('status',)







admin.site.register(Maincategory,MaincategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Post_advertise,PostAddsAdmin)
admin.site.register(Blog,BlogAdmin)

