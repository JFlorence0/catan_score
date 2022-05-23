from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
	"""Each user profile will have a table of data which builds their rating."""
	profile = models.ForeignKey(User, on_delete=models.CASCADE)
	type_select = (
		('0', 'Online'),
		('1', 'In Person'),
		)
	off_online = models.CharField(max_length=10, choices=type_select)
	comment = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return f"{self.comment[:20]}..."

