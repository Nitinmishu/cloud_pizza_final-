from django.urls import path
from .views import orderaccepted, orderdeclined, adminorders, userorderpage, adminloginview, \
    authenticateadmin, logoutadmin, logoutuser, orderplaced, homepageview, \
    usersignup, loginuser, customerpageview, userauthenticate

urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('authenticateadmin/', authenticateadmin),
    path('adminlogout/', logoutadmin),
    path('', homepageview, name='homepage'),
    path('usersignup/', usersignup),
    path('loginuser/', loginuser, name="userlogin"),
    path("customer/welcome/", customerpageview, name='customerpage'),
    path('customer/authenticate/', userauthenticate),
    path('logoutuser/', logoutuser),
    path('orderplaced/', orderplaced),
    path('userorder/', userorderpage),
    path('adminorders/', adminorders, name='adminorders'),
    path('acceptorder/<int:orderpk>/', orderaccepted),
    path('declineorder/<int:orderpk>/', orderdeclined),
]
