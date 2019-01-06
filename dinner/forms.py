from django.forms import ModelForm

from dinner.models import Options


class AddOptions(ModelForm):
    class Meta:
        model = Options
        fields = ['dinner_name', 'dinner_ingredients', 'dinner_instructions']
