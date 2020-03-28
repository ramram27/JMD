from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Gateapp.Forms import NewGatepassform,SearchForm
from Gateapp import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username'];
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('/Gateapp/view-Person/')
        else:
            data['error']="Username or password is incorrect"
            res=render(request,'Gateapp/login.html',data)
            return res
    else:
        return render(request,'Gateapp/login.html',data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/Gateapp/login/')

@login_required(login_url="/Gateapp/login/")
def SearchPerson(request):
    form=SearchForm()
    res=render(request,'Gateapp/Search_Person.html',{'form':form})
    return res

@login_required(login_url="/Gateapp/login/")
def search(request):
    form=SearchForm(request.POST)
    gs=models.Ram.objects.filter(national_id=form.data['national_id'])
    res=render(request,'Gateapp/Search_Person.html',{'form':form,'gs':gs})
    return res


@login_required(login_url="/Gateapp/login/")
def deletePerson(request):
    Personid=request.GET['Personid']
    g=models.Ram.objects.filter(id=Personid)
    g.delete()
    return HttpResponseRedirect('Gateapp/view-Person')

@login_required(login_url="/Gateapp/login/")
def editPerson(request):
    g=models.Ram.objects.get(id=request.GET['Personid'])
    fields={'full_name':g.full_name,'national_id':g.national_id,'phone_number':g.phone_number,'gender':g.gender,'vehicle_name':g.vehicle_name,'vehicle_number':g.vehicle_number,'date':g.date,'entry_time':g.entry_time,'exit_time':g.exit_time}
    form=NewGatepassform(initial=fields)
    res=render(request,'Gateapp/edit_Person.html',{'form':form,'g':g})
    return res

@login_required(login_url="/Gateapp/login/")
def edit(request):
    if request.method=='POST':
       form=NewGatepassform(request.POST)
       g=models.Ram()
       g.id=request.POST['Personid']
       g.full_name=form.data['full_name']
       g.national_id=form.data['national_id']
       g.phone_number=form.data['phone_number']
       g.gender=form.data['gender']
       g.vehicle_name=form.data['vehicle_name']
       g.vehicle_number=form.data['vehicle_number']
       g.date=form.data['date']
       g.entry_time=form.data['entry_time']
       g.exit_time=form.data['exit_time']
       g.save()
    return HttpResponseRedirect('Gateapp/view-Person')

@login_required(login_url="/Gateapp/login/")
def viewPerson(request):
    gs=models.Ram.objects.all()
    #username=request.session['username']
    res=render(request,'Gateapp/view_Person.html',{'gs':gs})
    return res

@login_required(login_url="/Gateapp/login/")
def NewPerson(request):
    form=NewGatepassform()
    res=render(request,'Gateapp/New_Person.html',{'form':form})
    return res

@login_required(login_url="/Gateapp/login/")
def add(request):
    if request.method=='POST':
        form=NewGatepassform(request.POST)
        g=models.Ram()
        g.full_name=form.data['full_name']
        g.national_id=form.data['national_id']
        g.phone_number=form.data['phone_number']
        g.gender=form.data['gender']
        g.vehicle_name=form.data['vehicle_name']
        g.vehicle_number=form.data['vehicle_number']
        g.date=form.data['date']
        g.entry_time=form.data['entry_time']
        g.exit_time=form.data['exit_time']
        g.save()
        s="Person Record Stored<br><a href='/Gateapp/view-Person'>View All Person</a>"
        return HttpResponse(s)
