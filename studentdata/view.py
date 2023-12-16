from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from tabledata.models import tabledata
from tabledata.models import passoutdata
from tabledata.models import feedata
from datetime import date
from tabledata.models import feetable

def home(request):
    return render(request,"index.html")

def registration(request):
    try:
        if request.method=="POST":
           reg="DuCat"
           name=request.POST.get('name')
           fathername=request.POST.get('fathername')
           mothername=request.POST.get('mothername')
           phoneno=request.POST.get('phoneno')
           address=request.POST.get('address')
           city=request.POST.get('city')
           gender=request.POST.get('gender')
           course=request.POST.get('course')
           btime=request.POST.get('btime')
           photo=request.POST.get('photo') 
           fee=request.POST.get('fee')
           data=tabledata(
                          reg=reg,
                          name=name,
                          fathername=fathername,
                          mothername=mothername,
                          phoneno=phoneno,
                          address=address,
                          city=city,
                          gender=gender,
                          course=course,
                          btime=btime,
                          photo=photo,
                          fee=fee,
                          refee=fee)
           data.save()
           data=tabledata.objects.all().order_by('-id')[0]
           fid=data.id
           reg="DuCat"+str(fid)
           data=tabledata(
                          id=fid,
                          reg=reg,
                          name=name,
                          fathername=fathername,
                          mothername=mothername,
                          phoneno=phoneno,
                          address=address,
                          city=city,
                          gender=gender,
                          course=course,
                          btime=btime,
                          photo=photo,
                          fee=fee,
                          refee=fee)
           data.save() 
           
    except:
        pass
    return render(request,"registration.html")

def view(request):
    return render(request,"view.html")

def viewall(request):
    data=tabledata.objects.all()
    data1={
        'alldata':data
    }
    return render(request,"viewall.html", data1)

def viewbybatchtime(request):
    try:
        if request.method=="POST":
            btime1=request.POST.get('btime1')
            url="/viewbybatchtime1/"+btime1
            return HttpResponseRedirect(url)
    except:
            pass
    return render(request,"viewbybatchtime.html")

def viewbybatchtime1(request,btime1):
    b_time=tabledata.objects.filter(btime=btime1)
    data1={
        'btimedata':b_time
    }
    return render(request,"viewbybatchtime1.html",data1)


def viewbyregno(request):
    try:
        if request.method=="POST":
           regno=request.POST.get('regno')
           url="/viewbyregno1/"+regno
           return HttpResponseRedirect(url)
    except:
        pass 
    return render(request,"viewbyregno.html")

def viewbyregno1(request,regno):
    reg_no=tabledata.objects.filter(reg=regno)
    data={
         'regno':reg_no
    }
    return render(request,"viewbyregno1.html",data)

def viewbyname(request):
    try:
        if request.method=="POST":
            fname=request.POST.get('name')
            url='/viewbyname1/'+fname
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"viewbyname.html")

def viewbyname1(request,fname):
    name=tabledata.objects.filter(name=fname)
    data1={
         'fname':name
    }
    return render(request,"viewbyname1.html",data1)

def update(request):
    try:
        if request.method=="POST":
            fupdate=request.POST.get('name')
            url='/update1/'+fupdate
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"update.html")

def update1(request,fupdate):
    get_id=tabledata.objects.get(name=fupdate)

    uid = get_id.id
    
    data1={
         'data1': get_id
    }
    try:
        if request.method=="POST":
           name=request.POST.get('name')
           fathername=request.POST.get('fathername')
           mothername=request.POST.get('mothername')
           phoneno=request.POST.get('phoneno')
           address=request.POST.get('address')
           city=request.POST.get('city')
           gender=request.POST.get('gender')
           course=request.POST.get('course')
           btime=request.POST.get('btime')
           photo=request.POST.get('photo') 
           fee=request.POST.get('fee')
           data=tabledata(
                          id=uid,
                          name=name,
                          fathername=fathername,
                          mothername=mothername,
                          phoneno=phoneno,
                          address=address,
                          city=city,
                          gender=gender,
                          course=course,
                          btime=btime,
                          photo=photo,
                          fee=fee,
                          refee=fee)
           data.save() 
           
    except:
        pass
    return render(request,"update1.html",data1)

def delete(request):
    try:
        if request.method=="POST":
            regno=request.POST.get('regno')
            fregno=tabledata.objects.get(reg=regno)
            
            data=passoutdata(
                reg=fregno.reg,
                name=fregno.name,
                fathername=fregno.fathername,
                mothername=fregno.mothername,
                phoneno=fregno.phoneno,
                address=fregno.address,
                city=fregno.city,
                gender=fregno.gender,
                course=fregno.course,
                btime=fregno.btime,
                photo=fregno.photo,
                fee=fregno.fee,
                refee=fregno.refee,
                )
            data.save()
            fregno.delete()

    except:
        pass
    return render(request,"delete.html")

def fees(request):
    return render(request,"fees.html")

def viewfee(request):
    try:
        if request.method=="POST":
            regnos=request.POST.get('regno')
            url="/viewfee1/"+regnos
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"viewfee.html")

def viewfee1(request,fregno):
    fregno=tabledata.objects.get(reg=fregno)
    data1={
        'fee':fregno
    }
    return render(request,"viewfee1.html",data1)

def submitfee(request):
    try:
        if request.method=="POST":
            regno=request.POST.get('regno')

            url="/submitdata/"+regno
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"submitfee.html")

def submitdata(request,fregno):
    reg_data=tabledata.objects.get(reg=fregno)
    data={
        'regno':reg_data
    }
    try:
        if request.method=="POST":
            reg_no=reg_data.regno
            fees=request.POST.get('fee')
            today1=date.today()
            totalfee=reg_data.refee
            rem=int(totalfee)-int(fees)
            subfees=feetable(regno=reg_no,fee=fees,totalfee=totalfee,date=today1,rem=rem)
            subfees.save()

            uid=reg_data.id

            data1=tabledata(
                id=uid,
                reg=reg_data.reg,
                name=reg_data.name,
                fathername=reg_data.fathername,
                mothername=reg_data.mothername,
                phoneno=reg_data.phoneno,
                address=reg_data.address,
                city=reg_data.city,
                gender=reg_data.gender,
                course=reg_data.course,
                btime=reg_data.btime,
                photo=reg_data.photo,
                fee=reg_data.fee,
                refee=reg_data.refee,
            )
            data1.save()
    except:
        pass
    return render(request,"submitfee1.html",data)


def passout(request):
    data=passoutdata.objects.all()
    data1={
        'alldata':data
    }
    return render(request,"passout.html",data1)