from django.db import models


class custommanager(models.Manager):
    def get_pet_age(self):
        # return super().get_queryset().filter(age=1)
        #return super().get_queryset().order_by('age')
        return super().get_queryset().filter(species='dog')
    
# Create your models here.
class pet(models.Model):
    gender = (("Male","male"),("Female","female"))
    image = models.ImageField(upload_to="media")
    name = models.CharField(max_length = 200)
    species = models.CharField(max_length = 200)
    breed = models.CharField(max_length = 200)
    age = models.IntegerField()
    gender = models.CharField(max_length = 200, choices = gender)
    description = models.CharField(max_length = 500)
    price = models.FloatField()
    slug = models.SlugField(default='',null=False)

    pets = custommanager()

    class Meta:
        db_table = "pet"


class customer(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.CharField(max_length = 200)
    phoneno = models.BigIntegerField()
    password = models.CharField(max_length=200)

    class Meta:
        db_table = "customer"


class cart(models.Model):
    productid = models.ForeignKey(pet,on_delete = models.CASCADE)
    customerid = models.ForeignKey(customer,on_delete= models.CASCADE)
    quantity = models.IntegerField()
    totalamount = models.FloatField()

    class Meta:

        db_table = "cart"


class order(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    pincode = models.CharField(max_length = 100)
    ordernumber = models.CharField(max_length = 100)
    phoneno = models.BigIntegerField()
    totalbillamount = models.FloatField(default =0)
    class Meta:
        db_table = 'order'

class payment(models.Model):
    customerid = models.ForeignKey(customer,on_delete = models.CASCADE)
    oid = models.ForeignKey(order,on_delete = models.CASCADE)
    paymentstatus = models.CharField(max_length = 100,default = 'pending')
    transactionid = models.CharField(max_length = 200)
    paymentmode = models.CharField(max_length = 100,default='paypal')

    class Meta: 
        db_table = 'payment'

class orderdetail(models.Model):
    ordernumber = models.CharField(max_length = 100)
    customerid = models.ForeignKey(customer,on_delete = models.CASCADE)
    productid = models.ForeignKey(pet, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    totalprice = models.IntegerField()
    paymentid = models.ForeignKey(payment,on_delete = models.CASCADE,null=True)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)


    class Meta: 
        db_table ='orderdetail'



