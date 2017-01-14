from django import forms

from django_remote_forms.forms import RemoteForm


def test_disabled_form():
    form = DisabledForm()
    remote_form = RemoteForm(form)
    remote_form_dict = remote_form.as_dict()
    assert remote_form_dict == EXPECTED_FORM


class DisabledForm(forms.Form):
    ssn = forms.CharField(disabled=True)
    name = forms.CharField(disabled=False)
    age = forms.IntegerField(required=True, disabled=True)
    location = forms.CharField(required=False, disabled=False)


EXPECTED_FORM = {
    'class_name': 'DisabledForm',
    'label_suffix': ':',
    'typed_errors': {},
    'prefix': None,
    'non_field_errors': [],
    'name': 'DisabledForm',
    'is_bound': False,
    'fieldsets': [],
    'errors': {},
    'ordered_fields': ['ssn', 'name', 'age', 'location'],
    'data': {
        'ssn': None,
        'name': None,
        'age': None,
        'location': None
    },
    'fields': {
        'name': {
            'initial': None,
            'required': True,
            'max_length': None,
            'label': None,
            'help_text': '',
            'widget': {
                'is_localized': False,
                'input_type': 'text',
                'is_required': True,
                'is_hidden': False,
                'attrs': {},
                'needs_multipart_form': False,
                'class_name': 'TextInput'
            },
            'class_name': 'CharField',
            'min_length': None,
            'disabled': False,
            'error_messages': {'required': 'This field is required.'}
        },
        'ssn': {
            'initial': None,
            'required': True,
            'max_length': None,
            'label': None,
            'help_text': '',
            'widget': {
                'is_localized': False,
                'input_type': 'text',
                'is_required': True,
                'is_hidden': False,
                'attrs': {},
                'needs_multipart_form': False,
                'class_name': 'TextInput'
            },
            'class_name': 'CharField',
            'min_length': None,
            'disabled': True,
            'error_messages': {'required': 'This field is required.'}
        },
        'age': {
            'max_value': None,
            'initial': None,
            'required': True,
            'label': None,
            'help_text': '',
            'widget': {
                'is_localized': False,
                'input_type': 'text',
                'is_required': True,
                'is_hidden': False,
                'attrs': {},
                'needs_multipart_form': False,
                'class_name': 'TextInput'
            },
            'class_name': 'IntegerField',
            'min_value': None,
            'disabled': True,
            'error_messages': {
                'invalid': 'Enter a whole number.',
                'required': 'This field is required.'
                }
        },
        'location': {
            'initial': None,
            'required': False,
            'max_length': None,
            'label': None,
            'help_text': '',
            'widget': {
                'is_localized': False,
                'input_type': 'text',
                'is_required': False,
                'is_hidden': False,
                'attrs': {},
                'needs_multipart_form': False,
                'class_name': 'TextInput'
            },
            'class_name': 'CharField',
            'min_length': None,
            'disabled': False,
            'error_messages': {'required': 'This field is required.'}
        }
    },
}
