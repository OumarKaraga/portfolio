from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from backend.models import User
from .forms import AddBook

#view config and rendering logic for the LOGIN/Account-Creation page

def login(request):
	return render(request, 'backend/login.html')

def user_page(request, validation):
	try:
		user = User.objects.get(validation=validation)
	except:
		raise Http404("Request not found")


	context = {'username': user.name,
	           'email': user.email,
	           'password': user.password
	           }
	return render(request, 'backend/new_user.html', context)

# view config and rendering for the user's profile page

def profile(request):
	return render(request, 'backend/profile.html')

# view config and rendering for the user's interests page

def interests(requests):
	return render(request, 'backend/interests.html')
	
def signup(request):
	return render(request, 'backend/signup.html')

def dataCollected(request, argument):
	values = argument.split("Z")
	entry = User(name=values[0], email=values[2], password=values[1], validation=values[0]+values[1])
	entry.save()
	username = entry.name
	email = entry.email
	context = {'username': username,'email' : email}
	return render(request, 'backend/profile.html',context)

def getData(request):
	return render(request, 'backend/form.html')

def get_name(request):
	form = None
	if request.method == "post":
		form = AddBook(request.POST)
		if form.is_Valid:
			return HttpResponseRedirect("/backend/signup")
		else:
			form = AddBook()
	return render(request, 'backend/form.html', {"form" : form})





