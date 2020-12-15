from django.shortcuts import render
from testapp.models import Student
from testapp.forms import StudentForm
from django.http import HttpResponse

# Create your views here.
def display_view(request):
    students=Student.objects.all()
    return render(request,'testapp/display.html',{'students':students})
def home_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)#request.FILES CONTAINS FILE INFO
        if form.is_valid():
            form.save()
            return HttpResponse('done')
    return render(request,'testapp/home.html',{'form':form})

def index(request):
    return render(request,'testapp/index.html')    
