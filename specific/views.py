from django.shortcuts import render
def about(request):
    return render(request,'about.html')

def hmm(request):
    return render(request,'hmm.html')