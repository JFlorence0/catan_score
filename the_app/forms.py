from django import forms

from .models import Entry

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['off_online','comment']
		labels = {
			'comment':'',
			'off_online':'Online/In Person:'
			}
		widgets = {'comment': forms.Textarea(attrs={'cols': 80})}