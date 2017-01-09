from django import forms
from .utils import empty_form_dict, management_dict


class EmptyForm(forms.Form):
    pass


EXPECTED_FORM = empty_form_dict()

EXPECTED_EMPTY_FORMSET = {
    'management_form': management_dict(),
    'forms': []
}

EXPECTED_FORMSET = {
    'management_form': management_dict(total_forms=1),
    'forms': [empty_form_dict(prefix='form-0')]
}

EXPECTED_FORMSET_THREE = {
    'management_form': management_dict(total_forms=3),
    'forms': [
        empty_form_dict(prefix='form-0'),
        empty_form_dict(prefix='form-1'),
        empty_form_dict(prefix='form-2'),
    ]
}
