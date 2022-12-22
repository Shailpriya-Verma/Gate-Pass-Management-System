from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db import connection
# Create your views here.
#import functions for sending email
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    return render(request,'Host/index.html')

def studentLogin(request):
    if request.method=="POST":
        sid=request.POST.get('sid')#123
        passwd=request.POST.get('passwd')#12345
        ltype=request.POST.get('ltype')
        if ltype=="Student":
            x=registration.objects.all().filter(rid=sid,passwd=passwd)
            if x:
                request.session['userid']=sid
                request.session['name']=x[0].name
                request.session['passwd'] = x[0].passwd
                request.session['regid']=x[0].rid
                request.session['course']=x[0].course
                request.session['year']=x[0].ryear
                request.session['pic']=str(x[0].pic)
                request.session['email']=x[0].email
                request.session['contact'] = x[0].mob
                request.session['address'] = x[0].address
                print(request.session.get('userid'))
                return HttpResponse("<script>alert('Welcome to Student Zone..');window.location.href='/host/index/'</script>")
            else:
                return HttpResponse("<script>alert('Registration id or password is incorrect..');window.location.href='/host/studentLogin/'</script>")
        elif ltype=="Guard":
            y=guardregistration.objects.all().filter(guardid=sid,passwd=passwd)
            if y:
                request.session["GuardId"]=(sid)
                request.session['Name'] = str(y[0].name)
                request.session['Picture'] = str(y[0].pic)
                request.session['Email'] = str(y[0].email)
                request.session['Contact'] = str(y[0].mob)
                request.session['Address'] = str(y[0].address)
                request.session["Gpasswd"] = passwd
                return HttpResponse("<script>alert('welcome to Guard Zone..');window.location.href='/host/guardDashboard/'</script>")
            else:
                return HttpResponse(
                    "<script>alert('Registration id or password is incorrect..');window.location.href='/host/studentLogin/'</script>")
        elif ltype=="Admin":
            z=adminlogin.objects.all().filter(userid=sid,passwd=passwd).count()
            if z == 1:
                request.session["adminId"] = sid
                request.session["Apasswd"] = passwd
                return HttpResponse("<script>alert('welcome to admin Zone..');window.location.href='/host/adminDashboard/'</script>")
            else:
                return HttpResponse(
                    "<script>alert('Registration id or password is incorrect..');window.location.href='/host/studentLogin/'</script>")

    return render(request,'Host/studentlogin.html')
def AddGuard(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mob=request.POST.get('mobile')
        gid=request.POST.get('gid')
        passwd=request.POST.get('passwd')
        cpasswd=request.POST.get('cpasswd')
        address=request.POST.get('address')
        picture=request.FILES.get('pic')
        if passwd==cpasswd:
            guardregistration(name=name,guardid=gid,passwd=passwd,address=address,pic=picture,email=email,mob=mob,rdate=datetime.now().date()).save()
            return HttpResponse("<script>alert('Guard Added Successfully...');window.location.href='/host/addGuard/'</script>")
        else:
            return HttpResponse(
                "<script>alert('Confirm password is not matched..');window.location.href='/host/addGuard/'</script>")

    return render(request,'Host/addGuard.html')
def StudentRegistration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        rid=request.POST.get('rid')
        mob=request.POST.get('contact')
        picture=request.FILES.get('pic')
        ryear=request.POST.get('ryear')
        course=request.POST.get('course')
        address=request.POST.get('address')
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        cpasswd=request.POST.get('cpasswd')
        if passwd==cpasswd:
            registration(name=name,rid=rid,course=course,ryear=ryear,address=address,pic=picture,mob=mob,email=email,passwd=passwd).save()
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail("Registration Sucessful", "Hello "+name+" \n You are sucessfully registered to Gate Pass Portal.\n Your registration id is :"+rid+" \nPassword is :"+passwd, email_from, recipient_list)
            return HttpResponse("<script>alert('You are registered successfully...');window.location.href='/host/stRegistration/'</script>")

        else:
            return HttpResponse("<script>alert('Confirm password is not matched..');window.location.href='/host/stRegistration/'</script>")
    return render(request,'Host/studentRegistration.html')

def GuardDashboard(request):
    x="RAM"
    return render(request,'Host/guardDashboard.html')
def AdminDashboard(request):

    return render(request,'Host/adminDashboard.html')

def stulogout(request):
    user=request.session.get('userid')
    if user:
        del request.session['userid']
        return HttpResponse("<script>alert('Your are signed Out..');window.location.href='/host/studentLogin/'</script>")

    return render(request,'host/stulogout.html')

def adminLogout(request):
    user = request.session.get('adminId')
    if user:
        del request.session['adminId']
        return HttpResponse(
            "<script>alert('Your are signed Out..');window.location.href='/host/studentLogin/'</script>")
    return render(request,'host/adminLogout.html')

def guardLogout(request):
    user = request.session.get('GuardId')
    if user:
        del request.session['GuardId']
        return HttpResponse(
            "<script>alert('Your are signed Out..');window.location.href='/host/studentLogin/'</script>")

    return render(request,'host/guardLogout.html')

def RequestGP(request):
    if request.method=='POST':
        regid=request.session.get('regid')
        fromdate=request.POST.get('fromdate')
        fromtime=request.POST.get('fromtime')
        todate=request.POST.get('todate')
        totime=request.POST.get('totime')
        reason=request.POST.get('reason')
        id = request.session.get('regid')
        if id:
            data = requestpass.objects.filter(regid=id,status=True)
            if data:
                return HttpResponse(
                    "<script>alert('You already have a active request.');window.location.href='/host/requestGP/'</script>")
            else :
                requestpass(regid=regid, fromdate=fromdate, fromtime=fromtime, todate=todate, totime=totime, reqtime=datetime.now(), reason=reason, status=True, adminremark='',
                permitstatus='').save()
                return HttpResponse(
            "<script>alert('Request send successfully. Wait for admin response...');window.location.href='/host/requestGP/'</script>")
    return render(request,'Host/requestGP.html')

def managestudent(request):
    a=request.GET.get('msg')
    if a:
        registration.objects.all().filter(rid=a).delete()
        return HttpResponse("<script>alert('record deleted successfully...');location.href='/host/managestudent/'</script>")
    rdata=registration.objects.all().order_by('name')
    mydict={"data":rdata}
    return render(request,'Host/managestudent.html',mydict)

def manageguard(request):
    a = request.GET.get('msg')
    if a:
        guardregistration.objects.all().filter(guardid=a).delete()
        return HttpResponse(
            "<script>alert('record deleted successfully...');location.href='/host/manageguard/'</script>")
    rdata = guardregistration.objects.all().order_by('name')
    mydict = {"data": rdata}
    return render(request,'Host/manageguard.html',mydict)

def manageGP(request):
    reqid=request.GET.get('reqid')
    status=request.GET.get('s')
    if status=="Allow":
        data=requestpass.objects.get(id=reqid)
        data.permittime=datetime.now()
        data.permitstatus=status
        data.status=False
        data.save()
        return HttpResponse("<script>alert('Permission allowed...');location.href='/host/manageGP/'</script>")
    elif status=="Deny":
        data = requestpass.objects.get(id=reqid)
        data.permitstatus = status
        data.status=False
        data.save()
        return HttpResponse("<script>alert('Permission Deny...');location.href='/host/manageGP/'</script>")

    cursor=connection.cursor()
    cursor.execute("select req.id,reg.rid,reg.name,reg.pic,req.fromdate,req.fromtime,req.todate,req.totime from Host_Registration reg,Host_Requestpass req where reg.rid=req.regid and req.status=True and req.permitstatus='' order by req.id desc")
    data=cursor.fetchall()
    md={"data":data}
    return render(request, 'Host/manageGP.html',md)

def viewGP(request):
    s=request.GET.get('status')
    id=request.GET.get('id')
    if id:
        data=requestpass.objects.get(id=id)
        data.status=False
        data.save()
        return HttpResponse("<script>alert('GetPass Deactiveted Successfully...');location.href='/host/viewGP/'</script>")


    regid=request.session.get('regid')
    data = requestpass.objects.all().filter(regid=regid).order_by('-id')
    md = {"data": data}
    return render(request, 'Host/viewGP.html',md)

def guardviewGP(request):
    data = requestpass.objects.all()
    cursor = connection.cursor()
    cursor.execute(
        "select req.id,reg.rid,reg.name,reg.pic,req.fromdate,req.fromtime,req.todate,req.totime,req.permittime,req.permitstatus from Host_Registration reg,Host_Requestpass req where reg.rid=req.regid and req.permitstatus='Allow' order by req.id desc")
    data = cursor.fetchall()
    md = {"data": data}
    return render(request, 'Host/guardviewGP.html',md)

def viewdetails(request):
    reqid=request.GET.get('reqid')
    if request.method=='POST':
        remark=request.POST.get('Remark')
        permittype=request.POST.get('btn')
        data = requestpass.objects.get(id=reqid)
        data.adminremark = remark
        data.permitstatus = permittype
        data.status=False
        data.save()
        return HttpResponse("<script>location.href='/host/manageGP/'</script>")

    cursor = connection.cursor()
    cursor.execute(
        "select req.id,reg.rid,reg.name,reg.pic,reg.course,reg.ryear,req.fromdate,req.fromtime,req.todate,req.totime,req.reqtime,req.reason from Host_Registration reg,Host_Requestpass req where reg.rid=req.regid and req.status=True and req.permitstatus='' and req.id="+reqid)
    data = cursor.fetchall()
    md = {"data": data}
    return render(request, 'Host/viewdetails.html',md)

def Schangepassword(request):
    if request.method=="POST":
        OP = request.POST.get('oldpasswd')
        NP=request.POST.get('newpasswd')
        CP=request.POST.get('cpasswd')

        x=request.session.get('userid')
        old = request.session.get('passwd')
        if (OP==old and NP==CP):
            data=registration.objects.get(rid=x)
            data.passwd=NP
            data.save()
            return HttpResponse(
                "<script>alert('Password changed successfully...');location.href='/host/Schangepassword/'</script>")

        else:
            return HttpResponse("<script>alert('Password is not matched...');location.href='/host/Schangepassword/'</script>")

    return render(request, 'Host/Schangepassword.html')

def Achangepassword(request):
    if request.method=="POST":
        OP = request.POST.get('oldpasswd')
        NP=request.POST.get('newpasswd')
        CP=request.POST.get('cpasswd')

        x=request.session.get('adminId')
        old = request.session.get('Apasswd')
        if (OP==old and NP==CP):
            data=adminlogin.objects.get(userid=x)
            data.passwd=NP
            data.save()
            return HttpResponse(
                "<script>alert('Password changed successfully...');location.href='/host/Achangepassword/'</script>")

        else:
            return HttpResponse("<script>alert('Password is not matched...');location.href='/host/Achangepassword/'</script>")

    return render(request, 'Host/Achangepassword.html')

def Gchangepassword(request):
    if request.method=="POST":
        OP = request.POST.get('oldpasswd')
        NP=request.POST.get('newpasswd')
        CP=request.POST.get('cpasswd')

        x=request.session.get('GuardId')
        old = request.session.get('Gpasswd')
        if (OP==old and NP==CP):
            data=guardregistration.objects.get(guardid=x)
            data.passwd=NP
            data.save()
            return HttpResponse(
                "<script>alert('Password changed successfully...');location.href='/host/Gchangepassword/'</script>")

        else:
            return HttpResponse("<script>alert('Password is not matched...');location.href='/host/Gchangepassword/'</script>")

    return render(request, 'Host/Gchangepassword.html')

def Areports(request):
    cursor = connection.cursor()
    cursor.execute(
        "select req.id,reg.rid,reg.name,reg.pic,req.fromdate,req.fromtime,req.todate,req.totime,req.permitstatus from Host_Registration reg,Host_Requestpass req where reg.rid=req.regid and req.permitstatus<>'' order by req.id desc")
    data = cursor.fetchall()
    md = {"data": data}
    return render(request, 'Host/Areports.html', md)

def Supdateprofile(request):
    if request.method=="POST":
        name=request.POST.get('name')
        sid=request.session.get('userid')
        course = request.POST.get('course')
        ryear = request.POST.get('ryear')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        pic = request.FILES.get('pic')
        address = request.POST.get('address')
        data=registration.objects.get(rid=sid)
        data.name=name
        data.course = course
        data.ryear = ryear
        data. email= email
        data.contact = contact
        data.pic = pic
        data.address = address
        data.save()
        return HttpResponse(
            "<script>alert('Profile Update Successfully...');location.href='/host/stulogout/'</script>")

    return render(request, 'Host/Supdateprofile.html')

def Gupdateprofile(request):
    if request.method=="POST":
        name=request.POST.get('name')
        gid=request.session.get('GuardId')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        pic = request.FILES.get('pic')
        address = request.POST.get('address')
        data=guardregistration.objects.get(guardid=gid)
        data.name=name
        data.email= email
        data.mob = contact
        data.pic = pic
        data.address = address
        data.save()
        return HttpResponse(
            "<script>alert('Profile Update Successfully...');location.href='/host/guardlogout/'</script>")

    return render(request, 'Host/Gupdateprofile.html')

def Forgotpassword(request):
    if request.method=='POST':
        regid=request.POST.get('regid')
        data=registration.objects.filter(rid=regid)
        if data:
            user_email=data[0].email
            user_password=data[0].passwd
            email_from = settings.EMAIL_HOST_USER
            email_to=[user_email]
            send_mail("Password of Gate Pass Portal",
                      "Your password of gate pass portal is : "+user_password+" \nThank You",
                      email_from, email_to)
            return HttpResponse(
                "<script>alert('Your password has been sent to your registered email id i.e "+user_email+"');location.href='/host/studentLogin/'</script>")
        else:
            return HttpResponse(
                "<script>alert('You entered wrong registration id.');location.href='/host/forgotpassword/'</script>")
    return render(request,'Host/forgotpassword.html')

def Gatepass(request):
    reqid=request.GET.get('reqid')
    x=request.session.get('userid')
    cursor = connection.cursor()
    cursor.execute(
        "select req.id,reg.rid,reg.name,reg.pic,req.fromdate,req.fromtime,req.todate,req.totime,req.reqtime,req.permitstatus,req.permittime,req.reason from Host_Registration reg,Host_Requestpass req where reg.rid=req.regid and req.id=" + reqid)


    data = cursor.fetchall()
    md = {"data": data}
    return render(request,'Host/gatepass.html',md)