from django.db import models

# Create your models here.

class Product(models.Model):
    productId=models.AutoField
    productName=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    pubDate=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.productName

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=3000)
    email=models.CharField(max_length=50,default="")
    phone=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000,default="")
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=10,default="")
    address=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")
    zip_code=models.CharField(max_length=50,default="")
    

