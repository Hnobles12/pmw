from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Project

def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)

# Create your views here.
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    
    projects = Project.objects.all() 
    # projects = [project.as_json() for project in projects]
    
    ctx = {
        "projects": projects,
        # "proj_json": json.dumps([project.as_json() for project in projects])
        "proj_json": json.dumps([project.as_dict() for project in projects])
    }
    return render(request, 'dashboard.html', ctx)


import json
class Test:
    def __init__(self):
        self.number = 100
        self.text = "Test Text"
    def as_json(self):
        return json.dumps(self.__dict__)

def vue_test(request):
    ctx = {
        "obj": Test().as_json(),
        "message":"Howdy Vue!"
    }
    return render(request, 'vue_test.html', ctx)
    