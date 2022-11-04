from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {
        "message":"Howdy Vue!"
    }
    return render(request, 'index.html', ctx)