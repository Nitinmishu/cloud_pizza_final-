from django.shortcuts import redirect, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Order, Pizza, Customer
from django.contrib.auth.models import User


# admin login page
def adminloginview(request):
    return render(request, "pizzap/adminlogin.html")


# take user input with authentication
def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']
    # inbuilt django function authenticate
    user = authenticate(username=username, password=password)

    # if user exit
    if user is not None and user.username == "nitin":
        login(request, user)
        # login succesful enter to this page
        return redirect('adminorders')

    # if user not exit
    if user is None:
        # adding a error message if wrong usernane password with using inbuilt feature of message
        messages.add_message(request, messages.ERROR, "invalid credentials")
        return redirect('adminloginpage')


# admin home logout and redirect to adminlogin pafe
def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')


# homaepage view
def homepageview(request):
    return render(request, "pizzap/homepage.html")


# user sign in page
def usersignup(request):
    username = request.POST["username"]
    password = request.POST["password"]
    phone_no = request.POST["Contact"]
    # if username already exists
    if User.objects.filter(username=username).exists():
        messages.add_message(request, messages.ERROR, 'user already exists')
        return redirect('homepage')

    # if username doesnt exist already (then its fine to create user)
    u = User.objects.create_user(username=username, password=password)
    u.save()

    Customer(user=u, phone_no=phone_no).save()
    messages.add_message(request, messages.ERROR, 'User Created Succesfully')
    return redirect('homepage')


def loginuser(request):
    return render(request, 'pizzap/userlogin.html')


def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    # inbuilt django function authenticate
    user = authenticate(username=username, password=password)

    # if user exit
    if user is not None:
        login(request, user)
        # login succesful enter to this page
        return redirect('customerpage')

    # if user not exit
    if user is None:
        # adding a error message if wrong usernane password with using inbuilt feature of message
        messages.add_message(request, messages.ERROR, "invalid credentials")
        return redirect('userlogin')


def customerpageview(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    username = request.user.username
    context = {'username': username, 'pizzas': Pizza.objects.all()}
    return render(request, 'pizzap/customerpage.html', context)


def logoutuser(request):
    logout(request)
    return redirect('userlogin')


def orderplaced(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')

    customer = Customer.objects.filter(user=request.user).first()
    address = request.POST['address']
    item_ordered = ""
    item_ordered_list = []
    total_amount = 0
    for pizza in Pizza.objects.all():
        pizza_id = pizza.id
        name = pizza.name
        price = pizza.price

        Quantity = request.POST.get(str(pizza_id), "")

        if str(Quantity) != "0" and str(Quantity) != "":
            curr_pizza_amount = int(Quantity) * int(price)
            total_amount += curr_pizza_amount
            # itemordered = name + " Price : " + str(curr_pizza_amount) + "  Quantity : " + Quantity + "    "
            itemordered = f'{name} x {Quantity} (€ {curr_pizza_amount})'
            item_ordered_list.append(itemordered)

    item_ordered = '; '.join(item_ordered_list)
    Order(customer=customer, address=address, item_ordered=item_ordered, total_amount=total_amount).save()
    messages.add_message(request, messages.ERROR, "order succesfully placed")
    return redirect('customerpage')


def userorderpage(request):
    customer = Customer.objects.filter(user=request.user).first()
    orders = Order.objects.filter(customer=customer).order_by('-id')
    context = {'orders': orders}
    return render(request, 'pizzap/userorder.html', context)


def adminorders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'pizzap/adminorders.html', context)


def orderaccepted(request, orderpk):
    order = Order.objects.filter(id=orderpk)[0]
    if order.status == "Declined":
        messages.add_message(request, messages.ERROR, 'Can\'t accept a declined order')
    else:
        order.status = "Accepted"
        order.save()
    return redirect(request.META['HTTP_REFERER'])


def orderdeclined(request, orderpk):
    order = Order.objects.filter(id=orderpk)[0]
    order.status = "Declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])
