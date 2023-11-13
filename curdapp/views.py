from django.shortcuts import render,redirect
#from curdapp.forms import Userform
from curdapp.models import Employess

def index(request):
     emp=Employess.objects.all()
     context={
          'emp':emp,
     }
     return render(request, 'index.html',context)
def Add(request):
     if request.method == 'POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          address=request.POST.get('address')
          phone=request.POST.get('phone')
          

          emp=Employess(
               name=name,
               email=email,
               address=address,
               phone=phone
          )
          emp.save()
          return redirect('home')
     return render(request,'index.html')
def Edit(request):
          emp=Employess.objects.all()
          context={
               'emp' : emp,
          }
          return redirect(request,'index.html',context)
def Update(request,id):
      if request.method == 'POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          address=request.POST.get('address')
          phone=request.POST.get('phone')
          emp=Employess(
                id=id,
                name=name, 
                email=email,
                address=address, 
                phone=phone)
          emp.save()
          return redirect('home')
      
      return redirect(request,'index.html')
def Delete(request,id):
      emp=Employess.objects.filter(id=id)
      emp.delete()
      
      context={
               'emp' : emp,
          }
      return redirect('home')
      
      




      
