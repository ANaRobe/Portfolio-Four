from .models import Cocktail
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit


class CocktailForm(ModelForm):
    class Meta:
        model = Cocktail
        fields = ['title', 'user', 'image', 'ingredients', 'steps', 'mixing_time', 'taste']

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout =Layout(
            HTML('<h2>Add a new Cocktail Recipe</h2>'),
        )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Add', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
        return helper
