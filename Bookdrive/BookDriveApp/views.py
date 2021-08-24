from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import donator, benificiary
from .forms import donatorform, status_form, User_form, benif_form, status1_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = User_form()
		if request.method == 'POST':
			form = User_form(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
			else:	
				messages.success(request, 'Account was created for ' + user)

				return redirect('Home')
			

		context = {'form':form}
		return render(request, 'HTML/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('login')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'HTML/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('home')

@login_required(login_url ='login')
def Donor(request):
	form = donatorform()
	if request.method == 'POST':
		form = donatorform(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form':form}
	return render(request, 'HTML/Donor.html', context)

@login_required(login_url ='login')
def benif(request):
	form = benif_form()
	if request.method == 'POST':
		form = benif_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form':form}
	return render(request, 'HTML/Benif.html', context)


def home(request):
	return render(request, 'HTML/Homepage.html')

def List(request):

	donator_info = donator.objects.all()
	total_user = donator_info.count()
	
	context = {'donator_info':donator_info, 'total_user':total_user, }
	return render(request, 'HTML/Table.html', context)

def update(request, pk):

	user = donator.objects.get(id=pk)
	form = status_form(instance=user)
	if request.method == 'POST':
		form = status_form(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('List')

	context = {'form':form}
	return render(request, 'HTML/Donor.html', context)

def updatee(request, pk):

	user = benificiary.objects.get(id=pk)
	form = status1_form(instance=user)
	if request.method == 'POST':
		form = status1_form(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('Grantee')

	context = {'form':form}
	return render(request, 'HTML/Benif.html', context)

def Grantee(request):
	
	benif_info = benificiary.objects.all()
	context = {'benif_info':benif_info,  }
	return render(request, 'HTML/grantee.html', context)