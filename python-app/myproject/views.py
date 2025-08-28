from django.http import HttpResponse

def index(request):
    return HttpResponse("Python app is working!")
