

from django.http import HttpResponse


# Q3---Ans:

def search(request):
    item = request.GET.get('item')
    brand = request.GET.get('brand')
    return HttpResponse(f"This is item: {item} and Brand is: {brand}")



# Q4---Ans:

def employee(request,emp_id):
    return HttpResponse(f"This is Accepted employee ID:{emp_id}")