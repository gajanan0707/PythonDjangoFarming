from django import forms
from .models import Maincategory,Subcategory,Products,Post_advertise,Blog

class MaincategoryForm(forms.ModelForm):
    product_desc = forms.CharField(label="Product Description", widget=forms.Textarea(attrs={'rows': 5, 'placeholder': "Please Enter Product description"}), help_text="Please enter description upto 200 character")

    class Meta:
        model = Maincategory
        fields = ('product_type', 'product_desc')

class SubcategoryForm(forms.ModelForm):
    product_desc=forms.CharField(label="Product Description", widget=forms.Textarea(attrs={'rows':5, 'placeholder':"Please enter the product description"}), help_text="Please enter description upto 200 character")

    class Meta:
        model=Subcategory
        fields=('product_name','product_desc','product_type','product_image','created_by')


class ProductsForm(forms.ModelForm):

    class Meta:
        model=Products
        fields=('subproduct','brand_name','product_name','product_type','size','price','prod_image')

class AddsproductForm(forms.ModelForm):

    class Meta:
        model=Post_advertise
        fields=('product_type','product_name','product','price','contact_supplier','prod_image','create_by')

class AddBlogForm(forms.ModelForm):

    class Meta:
        model=Blog
        fields=('title','blog_desc','blog_image','created_by','full_desc','cat_blog')



