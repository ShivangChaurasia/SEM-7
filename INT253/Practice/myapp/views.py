from django.http import HttpResponse

from django.http import Http404
from django.shortcuts import render
from myapp import templates
# Create your views here.




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



# def student(request, id):
#     if id:
#         return HttpResponse(f"This is student page and The Student Id is : {id}")
#     else:
#         return HttpResponse("Student Not found", status = 404);


# def student(request, id):
#     if id:
#         return HttpResponse(f"This is student page and The Student Id is : {id}")
#     else:
#         raise Http404("Student Not Found");


# def student_regex(request,roll):
#     return HttpResponse(f'This is roll no. {roll}');


def product(request):
    return HttpResponse("This is Product Page");


def pdt_regex(request,pdt_id):
    return HttpResponse(f"This is Product ID : {pdt_id}")


def employee(request):
    return HttpResponse("This is Employee Page");


def emp_regex(request,emp_id):
    return HttpResponse(f"This is Employee ID : {emp_id}")



def validate_emp(request):
    return HttpResponse(f"This is Employee Page");

def validate_regex(request, id):
    if id:
        return HttpResponse(f"This is employee Id: {id}");
    else:
        raise Http404("Employee Not Found");


def student(request):
    return HttpResponse("This is Student Portal");

def stu_profile(request, id,name):
    return HttpResponse(f"The Student Id: {id} and Name is : {name}");

def stu_search(request):
    name = request.GET.get('name');
    course = request.GET.get('course');
    if name and course:
        return HttpResponse("Searching...")
    else:
        return HttpResponse("Invalid Request")



def stu_register(request):

    if request.method=="GET":
        return render(request,'registration.html');
    elif request.method=="POST":
        name = request.POST.get('name');
        age = request.POST.get('age');
        email = request.POST.get('email');
        age = int(age);
        if age>=18:
            return HttpResponse(f"Registration Successfull... Name: {name}, Age: {age}, email: {email}");
        else:
            return HttpResponse("Not Eligible...");
    else:
        return HttpResponse("Something Went Wrong!! ");
