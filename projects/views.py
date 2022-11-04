from django.shortcuts import render

# Create your views here.
def main(request):
    ctx = {
    }
    return render(request, 'main.html', ctx)

def vue_test(request):
    ctx = {
        "message":"Howdy Vue!"
    }
    return render(request, 'vue_test.html', ctx)
    