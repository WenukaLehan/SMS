from django import forms

class GuardianInfoForm(forms.Form):
    gurdian_full_name = forms.CharField(label='Guardian Full Name', max_length=255)
    gurdian_name_with_initials = forms.CharField(label='Guardian Name with Initials',max_length=255)
    gurdian_date_of_birth = forms.DateField(label="Guardian Date of Birth")
    gurdian_gender = forms.CharField(label="Guardian Gender", widget=forms.RadioSelect(choices=[('M','Male'),('F','Female')]))
    gurdian_address = forms.CharField(label="Guardian Address", widget=forms.Textarea)
    gurdian_special_notes = forms.CharField(label="Guardian Special Notes",widget=forms.Textarea)
    gurdian_nic = forms.CharField(label='NIC', max_length=15)
    gurdian_job = forms.CharField(label='Job', max_length=15)
    gurdian_relation = forms.CharField(label='Relation to Student', max_length=15)
    