from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404

from .models import Entry
from .forms import EntryForm

# Create your views here.
def home(request):
	"""The home page from the_app."""
	return render(request, 'the_app/home.html')

@login_required
def userbase(request):
	"""Show all links to user"""
	users = User.objects.all()
	user_ex = [user.entry_set.count() for user in users]
	score_dict = {users[i]:user_ex[i] for i in range(len(users))}
	profiles = User.objects.order_by('date_joined')
	context = {'profiles':profiles, 'users': users, 'user_ex':user_ex, 'score_dict':score_dict}
	return render(request, 'the_app/userbase.html', context)

@login_required
def profile(request, user_id):
	"""Show a single profile and it's attributes."""
	user = User.objects.get(id=user_id)
	entry_count = user.entry_set.count
	entries = user.entry_set.order_by('-date_added')
	if entries:
		entry = entries[0]
	else:
		entry = None
	context = {'user':user, 'entries':entries, 'entry':entry, 'entry_count':entry_count}
	return render(request, 'the_app/profile.html', context)

@login_required
def new_profile(request):
	"""Create a new profile"""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = ProfileForm()

	else:
		# POST data submitted; process data.
		form = ProfileForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('the_app:userbase')

	# Display a blank or invalid form.
	context = {'form':form}
	return render(request, 'the_app/new_profile.html', context)

@login_required
def entry(request, profile_id):
	"""Add a entry for a particular profile"""
	user = User.objects.get(id=profile_id)

	if user != request.user:
		raise Http404

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = EntryForm()
	else:
		# POST data submitted; process data.
		form = EntryForm(data=request.POST)
		if form.is_valid():
			entry = form.save(commit=False)
			entry.profile = user
			entry.save()
			return redirect('the_app:profile', profile_id)
	
	# Display a blank or invalid form.
	context = {'user': user, 'form': form}
	return render(request, 'the_app/entry.html', context)

@login_required
def edit_entry(request, entry_id):
	"""Edit existing entry."""
	entry = Entry.objects.get(id=entry_id)
	user = entry.profile
	if user != request.user:
		raise Http404
	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = EntryForm(instance=entry)
	else:
		# POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('the_app:profile', user_id=user.id)

	context = {'entry':entry, 'user': user, 'form':form}
	return render(request, 'the_app/edit_entry.html', context)








