from django.shortcuts import render

# Create your views here.
def built_in_filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'SD':'Hai I am SesHulu','dt':'dt','c':'1'}

    return render(request,'built_in_filter.html',d)