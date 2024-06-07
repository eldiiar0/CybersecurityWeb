from django import forms 
from .models import MembersMessage


class MessageForm(forms.ModelForm):
	class Meta:
		model = MembersMessage
		fields = ['title', 'text',]
		widgets = {
			'title': forms.TextInput(attrs={'label': 'Title1', 'style': 'width: 100%;',}),
		    'text': forms.Textarea(attrs={'label': 'Text', 'style': 'width: 100%;', "rows": 10}),
		}