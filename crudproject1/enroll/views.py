from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration 
from .models import User
# Create your views here.

# This function will add and show items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            rl = fm.cleaned_data['role']
            reg = User(name=nm,email=em,role=rl)
            reg.save()
            fm = StudentRegistration()
        
    else: 
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

#This function will update and edit

def update_data(request,id):
    return render (request,'enroll/updatestudent.html',{'id':id})


#This function will delete 
def delete_data(request,id): 
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

 