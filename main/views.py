from django.shortcuts import render,HttpResponseRedirect
from main.form import StudentForm
from main.models import Student

# Create your views here.
def index(request):
    if request.method=="POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            rollno=fm.cleaned_data['rollno']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            new=Student(name=name,rollno=rollno,email=email,password=password)
            new.save()
    students=Student.objects.all()
    form=StudentForm()
    context={'form':form,'students':students}
    return render(request,'main/base.html',context)

def delete(request,id):
        student=Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect('/')


def update(request,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi)
    context={"fm":fm}
    return render(request,'main/update.html',context)

        


