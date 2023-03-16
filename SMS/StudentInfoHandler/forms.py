from django import forms

class StudentInfoForm(forms.Form):
    index_number = forms.IntegerField(label="Index Number")
    full_name = forms.CharField(label='Full Name', max_length=255)
    name_with_initials = forms.CharField(label='Name with Initials',max_length=255)
    date_of_birth = forms.DateField(label="Date of Birth (MM/DD/YYYY)", )
    gender = forms.CharField(label="Gender", widget=forms.RadioSelect(choices=[('M','Male'),('F','Female')]))
    enrolled_date = forms.DateField(label='Enrolled Date')
    address = forms.CharField(widget=forms.Textarea)
    alumni_status = forms.BooleanField(label='Alumni Status')
    special_notes = forms.CharField(widget=forms.Textarea)
    class_info = forms.CharField(max_length=255)
    RFID_key = forms.CharField(max_length=255)
    
    mother_name = forms.CharField(max_length=255)
    mother_status = forms.ChoiceField(choices=[('Alive','Alive'), ('Passed','Passed')],required=True)   # Alive/Passed
    mother_special_notes = forms.CharField(widget=forms.Textarea)
    father_name = forms.CharField(max_length=255)
    father_status = forms.ChoiceField(choices=[('Alive','Alive'), ('Passed','Passed')], required=True)  # Alive/Passed
    father_special_notes = forms.CharField(widget=forms.Textarea)
    
    