import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Use /hello-world URL
def hello_world(request):
    return HttpResponse("Hello World")


# Use /date URL
def current_date(request):
    today = datetime.date.today()
    return HttpResponse(today.strftime("Today is %d, %B %Y"))


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    today = datetime.date.today()
    bday = datetime.date(year, month, day)
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
    
    if age > 0:
        return HttpResponse("Your age is %s years old" % age)
    else:
        return HttpResponse("Please enter a valid date is /YYYY/MM/DD format.")

# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    try:
        b = birthday.split('-')
        bday = datetime.date(int(b[0]), int(b[1]), int(b[2]))
    except:
        return HttpResponse("Please enter date in YYYY-MM-DD format.")

    
    today = datetime.date.today()
    

    if bday.year > today.year:
        return HttpResponse("Please enter a birthdate not in the future.")
    elif ((today.month, today.day) > (bday.month, bday.day)):
        bday = bday.replace(year=today.year + 1)
    else:
        bday = bday.replace(year=today.year)
    
    days = (bday - today).days

    if days == 0:
        return HttpResponse("Happy birthday!")
    else:
        return HttpResponse("Days until next birthday: %s" % days)




# Use /profile URL
def profile(request):
    context = {
            "my_name": "Joshua",
            "my_age": "38",
            }
    return render(request, 'profile.html', context)

"""
    The goal for next task is to practice routing between two URLs.
    You will have:
        - /authors --> contains a list of Authors (template is provided to you)
        - /author/<authors_last_name> --> contains the detail for given author,
        using the AUTHORS_INFO provided below.

    First view just have to render the given 'authors.html' template sending the
    AUTHORS_INFO as context.

    Second view has to take the authors_last_name provided in the URL, look for
    for the proper author info in the dictionary, and send it as context while
    rendering the 'author.html' template. Make sure to complete the given
    'author.html' template with the data that you send.
"""

AUTHORS_INFO = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
    }
}

# Use provided URLs, don't change them
def authors(request):
    return render(request, 'authors.html', AUTHORS_INFO)

def author(request, authors_last_name):
    return render(request, 'author.html', AUTHORS_INFO[authors_last_name])
