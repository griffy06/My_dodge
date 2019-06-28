from django import forms


class OutpassForm(forms.Form):
        destination = forms.CharField(label='destination',max_length=100)
        vehicle = forms.CharField(label='vehicle',max_length=100)
        time = forms.TimeField(label='time')