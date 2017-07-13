from django.forms import ModelForm
from chancemeuci.models import Applicant

class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'