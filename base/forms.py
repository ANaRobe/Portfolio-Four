from .models import Cocktail, Remark
from django.forms import ModelForm, HiddenInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit, Button
from django.utils.text import slugify


# Create Update Delete Cocktail
class CocktailForm(ModelForm):

    class Meta:
        model = Cocktail
        fields = ['title', 'image', 'alcoholic', 'mixing_time', 'taste', 'ingredients', 'steps']

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            HTML('<h2 class="page-title text-center mt-5 mb-2">Manage the Recipe of your Cocktail </h2><hr><br>'),
        )

        for field in self.Meta().fields:
            helper.layout.append(Field(field, wrapper_class='row'))

        try:
            helper.layout.append(Submit('submit', ' Save', css_class='btn-dark mt-4 px-3 hover'))
            helper.add_input(Button('delete', 'Delete', css_class='btn-danger mt-4 hover', onclick='window.location.href="{}"'.format(f'/delete/{slugify(self.initial["title"])}/')))
            helper.field_class = 'col-6 mb-4 mt-4'
            helper.label_class = 'col-3 mb-4 mt-4'
        except Exception as e:
            print(e)

        return helper


# Create Remark
class RemarkForm(ModelForm):
    class Meta:
        model = Remark
        fields = ('text',)
