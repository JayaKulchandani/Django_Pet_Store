from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import pet,customer,cart,order,orderdetail
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from datetime import date

# Create your views here.

class PetListView(ListView):
    model = pet
    template_name="Petlist.html"
    context_object_name = "petobj"

    def get_context_data(self, **kwargs):
        data = self.request.session['username']
        context = super().get_context_data(**kwargs)
        context['session'] = data
        return context


class PetListViewCM(ListView):
    queryset = pet.pets.get_pet_age()
    template_name="Petlist.html"
    context_object_name = "petobj"

class PetDetailView(DetailView):
    model = pet
    template_name="petdetail.html"
    context_object_name = "i"



def nav(request):
    return render(request,"main.html",{"session":request.session['username']})

def search(request):
    if request.method == "POST":
        sq = request.POST.get('searchquery')
        print(sq)
        result = pet.pets.filter(Q(breed__icontains=sq) | Q(name__icontains=sq) | Q(species__icontains=sq) | Q(gender__iexact=sq))
        return render(request,'Petlist.html',{'petobj':result})


def registration(request):

    if request.method=="GET":
        return render(request,"Registration.html")
    elif request.method=="POST":
        fn = request.POST.get("fn")
        ln = request.POST.get("ln")
        email =request.POST.get("email")
        phoneno = request.POST.get("phone")
        password= request.POST.get("pass")
        passw = make_password(password)
        customerobj = customer(firstname=fn,lastname=ln,phoneno=phoneno,email=email,password=passw)
        customerobj.save()

        return HttpResponse("Customer registered Successfully")
    

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    
    elif request.method=="POST":
        cust = customer.objects.filter(email = request.POST.get("email"))

        if cust:
            custobj = customer.objects.get(email=request.POST.get("email"))
            passfe = request.POST.get("pass")
            flag = check_password(passfe,custobj.password)
           
            if flag:
                request.session['username'] = request.POST.get("email")
                session =  request.session['username']
                return redirect('../Petlist/')
               # return render(request,"Petlist.html",{'session' : session})

            else:
                
                return HttpResponse("Wrong username or password")


def addtocart(request):
   
    productid = request.POST['pid']
    print(productid)
    pobj = pet.pets.get(id=productid)
    usersession = request.session['username']
   
    if customer.objects.filter(email =usersession):
        cobj = customer.objects.get(email =usersession)
        flag = cart.objects.filter(customerid = cobj.id,productid = pobj.id) 
        if flag:
            cartobj = cart.objects.get(customerid = cobj.id,productid = pobj.id)
            cartobj.quantity = cartobj.quantity +1; 
            cartobj.totalamount =   cartobj.quantity * pobj.price ;
            cartobj.save()
        else: 
            cartobj = cart(quantity=1,totalamount= pobj.price,customerid = cobj,productid = pobj)
            cartobj.save()
        cartobjdisplay = cart.objects.filter(customerid = cobj.id)
        return render(request,'petlist.html',{'session': usersession,'petobj':pet.pets.all()})
    else:
        return redirect('../login/')

def viewcart(request):
    usersession = request.session['username']
    customerobj = customer.objects.get(email=usersession)
    cartobj = cart.objects.filter(customerid =customerobj.id ) 
    return render(request,'cart.html',{'petobj':cartobj,'session': usersession})


def changequantity(request):
    usersession = request.session['username']
    customerobj = customer.objects.get(email=usersession)
    pid = request.POST.get("pid")
    bq = request.POST['buttonquantity']
    if bq =='+':
        cartobj = cart.objects.get(customerid = customerobj.id,productid = pid)
        cartobj.quantity = cartobj.quantity + 1
        cartobj.totalamount = cartobj.quantity * cartobj.productid.price
        cartobj.save()
    else:
        cartobj = cart.objects.get(customerid = customerobj.id,productid = pid)
        cartobj.quantity = cartobj.quantity - 1
        cartobj.totalamount = cartobj.quantity * cartobj.productid.price
        cartobj.save()
        if cartobj.quantity ==0 :
            cartobj.delete()
    cartobj = cart.objects.filter(customerid =customerobj.id ) 
    return render(request,'cart.html',{'petobj':cartobj,'session': usersession})

def summarypage(request):
    usersession = request.session['username']
    customerobj = customer.objects.get(email=usersession)
    cartobj = cart.objects.filter(customerid = customerobj.id)
    totalbill = 0

    for i in cartobj:
        totalbill = i.totalamount + totalbill
    
    print(type(cartobj))
    return render(request,"summary.html",{'session': usersession,'petobj':cartobj,'totalbill': totalbill})


def payment(request):
    return render (request,"payment_page.html")


def placeorder(request):
    usersession = request.session['username']
    customerobj = customer.objects.get(email=usersession)
    nam = request.POST.get('name')
    addres= request.POST.get('address')
    phonen = int(request.POST.get('phoneno'))
    cit = request.POST.get('city')
    stat = request.POST.get('state')
    pincod = int(request.POST.get('pincode'))
    totalbillamoun = float(request.POST.get('totalbillamount'))
    orderobj = order(name= nam,city = cit,state=stat,address = addres, phoneno = phonen,pincode = pincod,totalbillamount = totalbillamoun)
    orderobj.save()

    dateobj = date.today()

    print(dateobj)
    datedata = str(dateobj).replace('-','')

    orderno = str(orderobj.id) + datedata
    orderobj.ordernumber = orderno
    orderobj.save()

    cartobj = cart.objects.filter(customerid = customerobj.id)

    for i in cartobj:
        orderdetailobj = orderdetail(ordernumber = orderno, productid = i.productid,customerid = i.customerid,quantity = i.quantity,totalprice = i.totalamount)
        orderdetailobj.save()
        i.delete()

    orderdetialobjectdisplay = orderdetail.objects.filter()
    return render(request,'payment_page.html',{'orderobj':orderobj})


def logout(request):
    request.session['username'] = ''
    # del(request.session['username'] )
    return redirect('../login/')
    
