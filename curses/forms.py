from django import forms

class ContactCurses(forms.Form):
	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(
		label='Message/Duvida', widget=forms.Textarea
)