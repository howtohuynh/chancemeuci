from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from chancemeuci.models import Applicant
from chancemeuci.forms import ApplicantForm
from chancemeuci.data.ctd import csv_to_dict
from chancemeuci.data.calculator import calculate


appliedList = ['applied', 'admitted', 'enrolled', 'selectivity_rate', 'yield_rate', 'gpa', 'verbal', 'math',
               'verbal + math', 'writing', 'verbal + math + writing']
appliedList2 = ['applied', 'admitted', 'enrolled', 'selectivity_rate', 'yield_rate']
highschoolList = ['admitted']

school = csv_to_dict('chancemeuci/data/csv_files/school.csv', appliedList)
major = csv_to_dict('chancemeuci/data/csv_files/major.csv', appliedList)
gender = csv_to_dict('chancemeuci/data/csv_files/gender.csv', appliedList)
high_school = csv_to_dict('chancemeuci/data/csv_files/high_school.csv', highschoolList)
residency = csv_to_dict('chancemeuci/data/csv_files/residency.csv', appliedList[:5])
ethnicity = csv_to_dict('chancemeuci/data/csv_files/ethnicity.csv', appliedList)
school_gender = csv_to_dict('chancemeuci/data/csv_files/school_gender.csv', appliedList)
school_ethnicity = csv_to_dict('chancemeuci/data/csv_files/school_ethnicity.csv', appliedList)
uc_gpa = csv_to_dict('chancemeuci/data/csv_files/gpa.csv', appliedList2)
sat_verbal = csv_to_dict('chancemeuci/data/csv_files/verbal.csv', appliedList2)
sat_math = csv_to_dict('chancemeuci/data/csv_files/math.csv', appliedList2)
sat_writing = csv_to_dict('chancemeuci/data/csv_files/writing.csv', appliedList2)


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
        l = lowWeight(form_data)
        h = highWeight(form_data)
        data = l
        data.extend(h)
        cl = calculate(l)
        ch = calculate(h)
        r = cl[0]
        r.extend(ch[0])
        chances = "{0:.2f}%".format(((ch[1] * 2) + cl[1])/3)
        args = {'form': form, 'form_data': form_data, 'range': sorted(r), 'chances': chances, 'ld': l, 'hd': h}
        return render(request, self.template_name, args)


def datasource(request):
    return render(request, 'chancemeuci/datasource.html')

def development(request):
    return render(request, 'chancemeuci/development.html')

def comments(request):
    return render(request, 'chancemeuci/comments.html')

def notes(request):
    return render(request, 'chancemeuci/notes.html')

def lowWeight(d: dict) -> float:
    low_weight = []
    x = d['major'].split(" | ")[0]
    y = d['major'].split(" | ")[1]
    low_weight.append(school[x])
    low_weight.append(major[x][y])
    low_weight.append(gender[d['gender']])
    low_weight.append(ethnicity[d['ethnicity']])
    low_weight.append(school_gender[x][d['gender']])
    low_weight.append(school_ethnicity[x][d['ethnicity']])
    low_weight.append(residency[d['residency']])
    return low_weight

def highWeight(d: dict) -> float:
    high_weight = []
    high_weight.append(uc_gpa[d['uc_gpa']])
    high_weight.append(sat_verbal[d['sat_verbal']])
    high_weight.append(sat_math[d['sat_math']])
    high_weight.append(sat_writing[d['sat_writing']])
    return high_weight

