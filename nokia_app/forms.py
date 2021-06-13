from django import forms
from .test_source_code import nokia_test


class ParamsForm(forms.Form):
    percentage = forms.FloatField(min_value=1, max_value=99, initial=90)

    def calculate(self):
        return nokia_test(**self.cleaned_data)
