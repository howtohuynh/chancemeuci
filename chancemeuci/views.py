from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from chancemeuci.models import Applicant
from chancemeuci.forms import ApplicantForm
from chancemeuci.data.ctd import csv_to_dict
from chancemeuci.data.calculator import calculate


appliedList = ['applied', 'admitted', 'enrolled', 'selectivity_rate', 'yield_rate', 'gpa', 'verbal', 'math',
               'verbal + math', 'writing', 'verbal + math + writing']

highschoolList = ['admitted']

school = csv_to_dict('chancemeuci/data/csv_files/school.csv', appliedList)
major = csv_to_dict('chancemeuci/data/csv_files/major.csv', appliedList)
gender = csv_to_dict('chancemeuci/data/csv_files/gender.csv', appliedList)
high_school = csv_to_dict('chancemeuci/data/csv_files/high_school.csv', highschoolList)
residency = csv_to_dict('chancemeuci/data/csv_files/residency.csv', appliedList[:5])
ethnicity = csv_to_dict('chancemeuci/data/csv_files/ethnicity.csv', appliedList)
school_gender = csv_to_dict('chancemeuci/data/csv_files/school_gender.csv', appliedList)
school_ethnicity = csv_to_dict('chancemeuci/data/csv_files/school_ethnicity.csv', appliedList)


class index(CreateView):
    template_name = 'chancemeuci/applicant_form.html'
    model = Applicant
    fields = ['major', 'gender', 'ethnicity', 'residency', 'high_school', 'uc_gpa', 'sat_math', 'sat_verbal',
              'sat_writing']

    def get(self, request):
        form = ApplicantForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ApplicantForm(request.POST or None)
        if form.is_valid():
            form_data = form.cleaned_data
            form.save()
        result = []
        x = form_data['major'].split(" | ")[0]
        y = form_data['major'].split(" | ")[1]
        result.append(school[x])
        result.append(major[x][y])
        result.append(gender[form_data['gender']])
        result.append(residency[form_data['residency']])
        result.append(ethnicity[form_data['ethnicity']])
        result.append(school_gender[x][form_data['gender']])
        result.append(school_ethnicity[x][form_data['ethnicity']])
        args = {'form': form, 'form_data': result, 'chances': calculate(result)}
        return render(request, self.template_name, args)


def datasource(request):
    return render(request, 'chancemeuci/datasource.html')

def development(request):
    return render(request, 'chancemeuci/development.html')

def comments(request):
    return render(request, 'chancemeuci/comments.html')

def notes(request):
    return render(request, 'chancemeuci/notes.html')

