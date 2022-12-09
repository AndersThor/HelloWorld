from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello World!")

#def inputTest(request):
#    return render()
