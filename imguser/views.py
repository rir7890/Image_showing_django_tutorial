from django.shortcuts import render, redirect
from .forms import MyModelForm
from .models import MyModel

# Create your views here.


def upload_image(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            form.save()
            request.session['user_name'] = name
            return redirect('display_profile')
    else:
        form = MyModelForm()
    return render(request, 'myapp/upload_image.html', {'form': form})


def success(request):
    return render(request, 'myapp/success.html')


def display_profile(request):
    name = request.session.get('user_name')
    data = MyModel.objects.get(name=name)
    return render(request, 'myapp/profile.html', {'data': data})
