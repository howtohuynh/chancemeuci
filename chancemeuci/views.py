from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from chancemeuci.models import Applicant
from chancemeuci.forms import ApplicantForm
from chancemeuci.data.ctd import csv_to_dict
from chancemeuci.data.calculator import calculate

# List to be used to convert .csv files to dict
appliedList = ['applied', 'admitted', 'enrolled', 'selectivity_rate', 'yield_rate', 'gpa', 'verbal', 'math',
               'writing']
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
        r.sort()
        chance_string = "Your overall chance is {}, but can range anywhere from {}% to {}%.".format(chances, r[0], r[-1])
        hs = highSchool(form_data)
        args = {'form': form, 'form_data': form_data, 'min': r[0], 'max': r[-1], 'chances': chance_string, 'ld': l, 'hs': hs}
        return render(request, self.template_name, args)


# Returns the average acceptance rate of factors that are weighed on a lower scale
def lowWeight(d: dict) -> float:
    low_weight = []
    x = d['major'].split(" | ")[0]
    y = d['major'].split(" | ")[1]

    low_weight.append((('School', x), school[x]))
    low_weight.append((('Major', y), major[x][y]))
    low_weight.append((('Gender', d['gender']), gender[d['gender']]))
    low_weight.append((('Ethnicity', d['ethnicity']), ethnicity[d['ethnicity']]))
    low_weight.append((('School & Gender', x + " & " + d['gender']), school_gender[x][d['gender']]))
    low_weight.append((('School & Ethnicity', x + " & " + d['ethnicity']), school_ethnicity[x][d['ethnicity']]))
    low_weight.append((('Residency', d['residency']), residency[d['residency']]))
    return low_weight

# Returns the average acceptance rate of factors that are weighed on a higher scale
def highWeight(d: dict) -> float:
    high_weight = []
    high_weight.append((('UC GPA', d['uc_gpa']), uc_gpa[d['uc_gpa']]))
    high_weight.append((('SAT Verbal', d['sat_verbal']), sat_verbal[d['sat_verbal']]))
    high_weight.append((('SAT Math', d['sat_math']), sat_math[d['sat_math']]))
    high_weight.append((('SAT Writing', d['sat_writing']), sat_writing[d['sat_writing']]))
    return high_weight

# Returns a string containing information about the amount of students enrolled from a certain high school
def highSchool(d: dict) -> str:
    if d['high_school'] != 'OTHER / NOT LISTED':
        string = "In 2016, {} people from {} enrolled at UC Irvine.".format(high_school[d['high_school']]['admitted'], d['high_school'].title())
    else:
        string = ''
    return string
