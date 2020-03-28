from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class NewGatepassform(forms.Form):
    full_name=forms.CharField(label='Full_Name',max_length=100)
    national_id=forms.CharField(label='National_ID',min_length=8,max_length=8)
    phone_number=forms.CharField(label='Phone_Number',min_length=10,max_length=10)
    gender=forms.CharField(label='Gender',max_length=50)
    vehicle_name=forms.CharField(label='Vehicle_Name',max_length=100)
    vehicle_number=forms.CharField(label='Vehicle_Number',min_length=13,max_length=13)
    date=forms.DateField(widget=DateInput)
    entry_time=forms.CharField(label='Entry_Time',min_length=7,max_length=7)
    exit_time=forms.CharField(label='Exit_Time',min_length=7,max_length=7)
class SearchForm(forms.Form):
    national_id=forms.CharField(label='National_ID',min_length=8,max_length=8)
