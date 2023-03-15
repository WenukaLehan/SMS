from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import StudentInfoForm

from .models import StudentInfo
from GuardianInfoHandler.models import GuardianInfo
from GuardianInfoHandler.forms import GuardianInfoForm


class StudentView(View):  
    def get(self, request):
        return render(request, template_name="add_student_form.html", context={
            "student_form_data" : StudentInfoForm(),
            "guardian_form_data" : GuardianInfoForm()
            })
    
    def post(self, request):
        data = request.POST
        print(data)
        student_instace = StudentInfo(
            index_number = data['index_number'][0],
            
        )
        return HttpResponse('Student Added Successfully')