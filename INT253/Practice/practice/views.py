from django.http import HttpResponse
from django.shortcuts import render

from myapp import templates

def home(request):
    return HttpResponse("Welcome to django!!");

def about(request):
    return HttpResponse("This is about page!!");

def contact(request):
    return HttpResponse("This is contact page!!");


def student(request, id,name):
    return HttpResponse(f"Student Id is: {id} \n His name is:{name}");



def student_info(request):
    id = request.GET.get('id');
    name = request.GET.get('name');
    return HttpResponse(f"{id} is the student id and {name} is the student name");


def method_check(request):

        if request.method=='GET':
            return render(request,'method.html');
        elif request.method=='POST':
            name = request.POST.get('name');
            email = request.POST.get('email');
            age =  request.POST.get('age');
            age = int(age);

            if age>=18:
                return HttpResponse(f"Hello, {name}, Your Registered Email is {email}, and You are eligible for voting");
            else:
                return HttpResponse(f"Hello, {name}, Your Registered Email is {email}, and You are not eligible for voting");
        else:
            return HttpResponse("Invalid Request Method");


