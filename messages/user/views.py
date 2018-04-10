from django.shortcuts import render

# Create your views here.
def require_login(request):
    return render(request, 'user/login.html')

