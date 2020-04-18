from django.shortcuts import render

# Create your views here.
def coco(request):
    return render(request , "mldeploy/coco.html")

def mnist(request):
    return render(request , "mldeploy/mnist.html")

