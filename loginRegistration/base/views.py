from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "home.html", {})

def authView(request):
    if request.method == "POST":