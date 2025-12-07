from django.shortcuts import render

# Create your views here.
def dateInfo1(request):
    return render(request, 'future/dateInput1.html')

def dateInfo2(request):
    return render(request, 'future/dateInput2.html')

def dateInfo3(request):
    return render(request, 'future/dateInput3.html')

def dateInfo4(request):
    return render(request, 'future/dateInput4.html')

def numberinfo1(request):
    contax={'M': 'mulank'}
    return render(request, 'future/numberinfo.html', contax)

def numberinfo2(request):
    contax={'B':"bhagyank"}
    print(contax)
    return render(request, 'future/numberinfo.html', contax)

def numberinfo3(request):
    contax={'P':"personalYear"}
    return render(request, 'future/numberinfo.html', contax)

def loShuGrid(request):
    return render(request, 'future/loShuGrid.html')
