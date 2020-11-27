from django.shortcuts import render


from django.http import HttpResponse
from . import forms
from. import models
from django.template import loader


def importLogs(request):
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            context = {'form' : form}
        else:
            form = forms.DocumentForm()
            text = "This fileformat is not supported. Please use a CSV or XES file."
            context = {'form' : form, 'text' : text}



    else:
        form = forms.DocumentForm()
        context = {'form' : form}

    template = loader.get_template('main.html')
    return HttpResponse(template.render(context, request))
