from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    if 'username' in request.session:
        #change reg to home
        return redirect(reg)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username,password=password)
        if user is not None:
            #create session
            #change reg to home
            return redirect(reg)
    else:
        return render(request, 'index.html')
def reg(request):
    return HttpResponse("<h2>Reg</h2>")