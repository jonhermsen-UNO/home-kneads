from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 'page_title': 'Hello, World!' }
    return render(request, 'app/index.html', context)
