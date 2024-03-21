from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm

def register(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')  # Replace with your success URL
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})