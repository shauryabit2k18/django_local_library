from django.shortcuts import render

# Create your views here.
def index_main(request):
    return render(request , "my_portfolio/index.html")


def gallery(request):
    return render(request , "my_portfolio/gallery.html")

def contact(request):
    return render(request , "my_portfolio/contact.html")

def certi(request):
    return render(request , "my_portfolio/certi.html")

def about(request):
    return render(request , "my_portfolio/about.html")
