from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def services(request):
    return HttpResponse("This is the services page.")

def result(request):
    marks = 85
    if marks >= 90:
        grade = 'Excellent'
        return HttpResponse(f"Your grade is: {grade}")
    elif marks >= 80:
        grade = 'Very Good'
        return HttpResponse(f"Your grade is: {grade}")
    elif marks >= 70:
        grade = 'Good'
        return HttpResponse(f"Your grade is: {grade}")
    elif marks >= 60:
        grade = 'Average'
        return HttpResponse(f"Your grade is: {grade}")
    elif marks <= 40:
        grade = 'Fail'
        return HttpResponse(f"Your grade is: {grade}")
    else:
        return HttpResponse("Invalid marks.")



def weather(request):
    type = "sunny"
    if type == "sunny":
        return HttpResponse("The weather is sunny.")
    elif type == "rainy":
        return HttpResponse("The weather is rainy.")
    elif type == "cloudy":
        return HttpResponse("The weather is cloudy.")
    else:
        return HttpResponse("The weather is unknown.")


def greetings(request):
    time = 12
    if time < 12:
        return HttpResponse("Good morning!")
    elif time < 17:
        return HttpResponse("Good afternoon!")
    else:
        return HttpResponse("Good evening!")



def items(request):
    itemList = {
        'pizza': 'Pizza costs Rs. 500',
        'burger': 'Burger costs Rs. 300',
        'pasta': 'Pasta costs Rs. 400',
        'egg' : '12 Egg costs Rs. 100',
        'anda' : 'Anda costs Rs. 10',
        'anda curry' : 'Anda Curry costs Rs. 150',
        'anda fry' : 'Anda Fry costs Rs. 120',
        'anda paratha' : 'Anda Paratha costs Rs. 200',

        'milk' : '1 liter Milk costs Rs. 50',
        'bread' : '1 loaf Bread costs Rs. 30',
        'rice' : '1 kg Rice costs Rs. 80',
        'dal' : '1 kg Dal costs Rs. 100',
        'oil' : '1 liter Oil costs Rs. 120',
        'sugar' : '1 kg Sugar costs Rs. 60',
        'salt' : '1 kg Salt costs Rs. 20',
        'spices' : 'Spices costs Rs. 150',
        'fruits' : 'Fruits costs Rs. 200',
        'vegetables' : 'Vegetables costs Rs. 150',
        'chicken' : '1 kg Chicken costs Rs. 250',
        'beef' : '1 kg Beef costs Rs. 300',
        'fish' : '1 kg Fish costs Rs. 200',
        'eggs' : '1 dozen Eggs costs Rs. 80',
        'cheese' : '1 kg Cheese costs Rs. 200'
    }

    content = "<h1>Item List</h1><ul>"
    for item, desc in itemList.items():
        content+= f'<li><h3>{item}: {desc}</h3></li>'
    content += "</ul>"
    return HttpResponse(content)


def Dgreetings(request,name,time):
    if(time>=24 or time<0):
        return HttpResponse(f"<h1>Invalid time value: {time}. Please provide a valid time between 0 and 23.</h1>")
    if time < 12:
        return HttpResponse(f"<h1>Good morning, {name}!</h1>")
    elif time < 17:
        return HttpResponse(f"<h1>Good afternoon, {name}!</h1>")
    else:
        return HttpResponse(f"<h1>Good evening, {name}!</h1>")
