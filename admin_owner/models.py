from django.conf import settings
from django.db import models
from profiles.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Reject"),
)


class Maincategory(models.Model):
    product_type = models.CharField(max_length=60, null=True,blank=True)
    product_desc = models.TextField()
    create_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.product_type


class Subcategory(models.Model):
    product_name = models.CharField(max_length=30,null=True,blank=True)
    product_desc = models.TextField()
    product_type = models.ForeignKey(Maincategory, related_name='Subcategory', on_delete=models.CASCADE,null=True)
    product_image = models.ImageField(upload_to='subcategory-images/', null=True,blank=True)
    created_by = models.ForeignKey(User, related_name="Users", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '%s' %(self.product_name)

class Products(models.Model):
    subproduct=models.CharField(max_length=40,null=True,blank=True)
    brand_name=models.CharField(max_length=30,null=True,blank=True)
    product_name=models.ForeignKey(Subcategory,related_name='Products', on_delete=models.CASCADE,null=True,blank=True)
    product_type = models.ForeignKey(Maincategory, related_name='Products', on_delete=models.CASCADE,null=True,blank=True)
    size=models.IntegerField()
    price=models.IntegerField()
    prod_image=models.ImageField(upload_to='product-images/')

    def __str__(self):
        return '%s' %(self.subproduct)

class Post_advertise(models.Model):
    product_type = models.ForeignKey(Maincategory, related_name='Post_advertise', on_delete=models.CASCADE,null=True)
    product_name = models.ForeignKey(Subcategory, related_name='Post_advertise', on_delete=models.CASCADE,null=True)
    product=models.CharField(max_length=40,null=True)
    price = models.IntegerField()
    contact_supplier = models.IntegerField()
    prod_image = models.ImageField(upload_to='addvertise/')
    create_by = models.ForeignKey(User, related_name="Post_advertise", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s' %(self.product)





class Blog(models.Model):
    title=models.CharField(max_length=60,null=True,blank=True)
    blog_desc=models.TextField(null=True,blank=True)
    blog_image=models.ImageField(upload_to='blogimages/')
    created_date=models.DateField(auto_now_add=True,null=True,blank=True)
    full_desc=models.TextField()
    created_by=models.ForeignKey(User, related_name="Blog", on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cat_blog=models.CharField(max_length=60,null=True,blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return '%s' %(self.title)





