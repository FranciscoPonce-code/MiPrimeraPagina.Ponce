from django.shortcuts import render

# Create your views here.

from django.shortcuts import render  # noqa: F811

def home(request):
    return render(request, "miapp/index.html")
