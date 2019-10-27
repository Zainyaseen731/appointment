from django import forms
import datetime as dt

HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(10, 16)]
class SearchForm(forms.Form):
    first_name=forms.CharField(label="First_name",widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name=forms.CharField(label="Last_name",widget=forms.TextInput(attrs={'placeholder': 'Fater name'}))
    username=forms.CharField(label="User_name",widget=forms.TextInput(attrs={'placeholder': 'zain1'}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder': 'zain@gmail.com'}))
    password1=forms.IntegerField(label="Passward",widget=forms.TextInput(attrs={'placeholder': '12345678'}))
    password2=forms.IntegerField(label="Confrem Passward",widget=forms.TextInput(attrs={'placeholder': '12345678'}))


class DataStore(forms.Form):
    username=forms.CharField(label="User_name",widget=forms.TextInput(attrs={'placeholder': 'zain1'}))
    password=forms.IntegerField(label="Passward",widget=forms.TextInput(attrs={'placeholder': '12345678'}))


class DateInput(forms.DateInput):
    input_type='date'


class Data_taking(forms.Form):
    first_name=forms.CharField(label="First_name",widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name=forms.CharField(label="Last_name",widget=forms.TextInput(attrs={'placeholder': 'Fater name'}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder': 'zain@gmail.com'}))
    note=forms.CharField(label="Note",widget=forms.Textarea(attrs={'placeholder': 'Enter your reson ....',"rows":3,"cols":4}))
    date=forms.DateField(label="Date",widget=DateInput)
    time=forms.TimeField(label='Time',widget = forms.Select(choices=HOUR_CHOICES))
