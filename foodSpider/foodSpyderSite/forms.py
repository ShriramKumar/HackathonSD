from django import forms

class InputForm(forms.Form):
    input_recipe = forms.CharField(label='input_recipe', max_length=100)