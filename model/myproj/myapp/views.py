from django.shortcuts import render
def cubevol(request):
    context={}
    context['volume'] = "0"
    context['a'] = "0"
    context['a'] = "0"
    context['a'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        a = request.POST.get('length','0')
        a = request.POST.get('length','0')
        a = request.POST.get('length','0')
        print('request=',request)
        print('length=',a)
        print('length=',a)
        print('length=',a)
        area = int(l) * int(b)
        context['volume'] = volume
        context['a'] = a
        context['a'] = a
        print('Volume=',volume)
    return render(request,'myapp/math.html',context)
