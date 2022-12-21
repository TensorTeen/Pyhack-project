from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm, Test_TextForm,TrainForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .script.Runtime.Final import testing_data,evaluvate,trainer


@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form':form})


@login_required(login_url='/login')
def test(request):
    result = None
    rating = None
    if request.method == 'POST':
        form = Test_TextForm(request.POST)
        if form.is_valid():
            result = testing_data(txt=form.cleaned_data['Test_Text'])
            rating = evaluvate(result)
        else :
            print('hi')
    else:
        form = Test_TextForm()

    return render(request, 'main/test.html', {'form':form,'result':result,'rating':rating},)

@login_required(login_url='/login')
def train(request):
    if request.method =='POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            name,epoch,batch = form.cleaned_data.values()
            trainer(name,epoch,batch)
    else:
        form = TrainForm()
    
    return render(request,'main/train.html', {'form':form})