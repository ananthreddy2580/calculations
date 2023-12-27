from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')
def analyze(request):
    n1=request.POST.get('n1')
    n2=request.POST.get('n2')
    calc=request.POST.get('calc')
    if calc == 'add':
        cal = int(n1)+int(n2)
        return render(request,'analyze.html',{'analyzer':cal,'perform':calc})
    elif calc == 'sub':
        cal = int(n1) - int(n2)
        return render(request, 'analyze.html', {'analyzer': cal,'perform':calc})
    elif calc == 'mul':
        cal = int(n1)*int(n2)
        return render(request, 'analyze.html', {'analyzer': cal,'perform':calc})
    else:
        return HttpResponse('<h4>you must choose one</h4>')