from django import forms
from .utils import empty_form_dict, management_dict


class EmptyForm(forms.Form):
    pass


EXPECTED_FORM = empty_form_dict()
