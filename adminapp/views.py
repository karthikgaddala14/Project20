from django.shortcuts import render
from django.views import View
from .models import jobs
# Create your views here.
class home(View):
    def get(self,request):
        qs= jobs.objects.all()
        condic={'records': qs}
        return render(request,'display.html',context=condic)