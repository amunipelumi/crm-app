from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from . forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm
from . models import Record


# home
def homepage(request):
    return render(request, 'myapp/index.html')


# register/create
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Account created successfully!')
            return redirect('login')
            
    context = {'form':form}
    return render(request, 'myapp/register.html', context)


# login
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')
            
            # else:
            #     messages.info(request, 'Incorrect login details!') 
            #     return redirect('')

    context = {'form':form}
    return render(request, 'myapp/login.html', context)


# dashboard
@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()

    context = {'records':records}
    return render(request, 'myapp/dashboard.html', context)


# create record
@login_required(login_url='login')
def create_record(request):
    form = AddRecordForm()

    if request.method == 'POST':
        form = AddRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Record added!')
            return redirect('dashboard')
    
    context = {'form':form}
    return render(request, 'myapp/create-record.html', context)


# view record
@login_required(login_url='login')
def view_record(request, pk):

    record = Record.objects.get(id=pk)
    context = {'record':record}

    return render(request, 'myapp/view-record.html', context) 


# update record
@login_required(login_url='login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record) 

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            messages.success(request, 'Record updated!')
            return redirect('dashboard')
        
    context = {'form':form}
    return render(request, 'myapp/update-record.html', context)


# delete record
@login_required(login_url='login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)
    record.delete()
    
    messages.success(request, 'Record deleted!')
    return redirect('dashboard')


# logout
def logout(request):
    auth.logout(request)

    messages.info(request, 'You logged out of your account!')
    return redirect('login')