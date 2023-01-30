from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def htmlfile(request):
    if request.method=='Post':
        un=request.POST['usn']
        pw=request.POST['psw']
        print(un)
        print(pw)
        return HttpResponse('data is submitted')
    

    return render(request,'htmlfile.html')