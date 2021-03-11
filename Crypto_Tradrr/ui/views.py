from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, 'base.html')

# todo: setup views for other pages

# todo: layout content for dashboard
