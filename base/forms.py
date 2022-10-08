from .models import Cocktail
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit, Button


class CocktailForm(ModelForm):
    class Meta:
        model = Cocktail
        fields = ['title', 'user', 'image', 'ingredients', 'steps', 'mixing_time', 'taste', 'slug']

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            HTML('<h2>Manage Cocktail Recipe</h2>'),
        )

        # print the self object so we can see all fields available
        print("Self: ", vars(self))
        # print self.initial to narrow down the search and confirm its a dictionary to access
        print("Initial Values: ", self.initial)

        for field in self.Meta().fields:
            helper.layout.append(Field(field, wrapper_class='row'))
        helper.layout.append(Submit('submit', 'Add', css_class='btn-success'))
        helper.add_input(Button('delete', 'Delete', onclick='window.location.href="{}"'.format(f'/delete/{self.initial["slug"]}/')))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
        return helper
