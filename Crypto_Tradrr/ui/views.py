from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, 'base.html')

# todo: set up views for other pages
# Will be multiple pages each for a particular view of data (Min of 3)

# todo: create history.html
def history(response):
    return render(response, 'history.html')
