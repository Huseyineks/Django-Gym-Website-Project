from django.shortcuts import render,redirect
from .forms import AppForm
def FooterForm(request):
    form = AppForm(request.POST or None)
    context = dict(
        form = form
    )
    if form.is_valid():
       context = dict(
        form = form
    )
       newForm = form.save()
       return redirect('homepage')
    
    return render(request,'faqs.html',context)

    