"""Defines URL patterns for the_app."""

from django.urls import path
from . import views

app_name = 'the_app'
urlpatterns = [
	# Home page
	path('', views.home, name='home'),
	# Page to view all users
	path('userbase', views.userbase, name='userbase'),
	# Detail page for a single topic.
	path('userbase/<int:user_id>/', views.profile, name='profile'),
	# Create a new profile
	path('new_profile/', views.new_profile, name='new_profile'),
	# Add a rating/comment
	path('entry/<int:profile_id>/', views.entry, name='entry'),
	# Page for editing an entry
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	]