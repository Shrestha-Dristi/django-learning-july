from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ourapp_home(request):
    return HttpResponse("""
<h1>Hello World</h1>
<h2>We are learning Django</h2>
""")
