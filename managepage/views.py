from django.shortcuts import render

# Create your views here.

def waitingList(request):
    return render(request,'managepage/index.html')