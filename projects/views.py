from django.shortcuts import render

# Create your views here.
def main(request):
    ctx = {
    }
    return render(request, 'main.html', ctx)


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
    