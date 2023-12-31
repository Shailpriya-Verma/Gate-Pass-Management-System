from django.urls import path
from . import views as v1
urlpatterns = [
    path('index/', v1.home),
    path('', v1.studentLogin),
    path('studentLogin/', v1.studentLogin),
    path('addGuard/', v1.AddGuard),
    path('stRegistration/', v1.StudentRegistration),
    path('guardDashboard/', v1.GuardDashboard),
    path('adminDashboard/', v1.AdminDashboard),
    path('stulogout/', v1.stulogout),
    path('guardlogout/', v1.guardLogout),
    path('adminlogout/', v1.adminLogout),
    path('requestGP/', v1.RequestGP),
    path('manageguard/', v1.manageguard),
    path('managestudent/', v1.managestudent),
    path('manageGP/', v1.manageGP),
    path('viewGP/', v1.viewGP),
    path('guardviewGP/', v1.guardviewGP),
    path('viewdetails/', v1.viewdetails),
    path('Schangepassword/', v1.Schangepassword),
    path('Achangepassword/', v1.Achangepassword),
    path('Gchangepassword/', v1.Gchangepassword),
    path('Areports/', v1.Areports),
    path('Supdateprofile/', v1.Supdateprofile),
    path('Gupdateprofile/', v1.Gupdateprofile),
    path('forgotpassword/', v1.Forgotpassword),
    path('gatepass/', v1.Gatepass),

]