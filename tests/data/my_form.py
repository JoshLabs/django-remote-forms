from django import forms


class MyForm(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, required=False)
    check = forms.BooleanField()
    select = forms.ChoiceField(choices=[('label', '1'), ('label2', '2')], initial='2')


EXPECTED_FORM = {
    'class_name': 'MyForm',
    'name': 'MyForm',
    'data': {
        'check': None,
        'name': None,
        'select': '2',
        'text': None
    },
    'is_bound': False,
    'label_suffix': ':',
    'ordered_fields': ['name', 'text', 'check', 'select'],
    'prefix': None,
    'errors': {},
    'typed_errors': {},
    'non_field_errors': [],
    'fieldsets': [],
    'fields': {
        'check': {
            'error_messages': {'required': 'This field is required.'},
            'help_text': '',
            'initial': None,
            'label': None,
            'required': True,
            'class_name': 'BooleanField',
            'widget': {
                'attrs': {},
                'check_test': True,
                'input_type': 'checkbox',
                'is_hidden': False,
                'is_localized': False,
                'is_required': True,
                'needs_multipart_form': False,
                'class_name': 'CheckboxInput'
            }
        },
        'name': {
            'error_messages': {'required': 'This field is required.'},
            'help_text': '',
            'initial': None,
            'label': None,
            'max_length': None,
            'min_length': None,
            'required': True,
            'class_name': 'CharField',
            'widget': {
                'attrs': {},
                'input_type': 'text',
                'is_hidden': False,
                'is_localized': False,
                'is_required': True,
                'needs_multipart_form': False,
                'class_name': 'TextInput'
            }
        },
        'select': {
            'choices': [{'display': '1', 'value': 'label'},
                        {'display': '2', 'value': 'label2'}],
            'error_messages': {
                'invalid_choice': 'Select a valid choice. %(value)s is not one of the available choices.',
                'required': 'This field is required.'
            },
            'help_text': '',
            'initial': '2',
            'label': None,
            'required': True,
            'class_name': 'ChoiceField',
            'widget': {
                'attrs': {},
                'choices': [{
                    'display': '1',
                    'value': 'label'
                },
                    {
                        'display': '2',
                        'value': 'label2'
                    }],
                'input_type': 'select',
                'is_hidden': False,
                'is_localized': False,
                'is_required': True,
                'needs_multipart_form': False,
                'class_name': 'Select'
            }
        },
        'text': {
            'error_messages': {'required': 'This field is required.'},
            'help_text': '',
            'initial': None,
            'label': None,
            'max_length': None,
            'min_length': None,
            'required': False,
            'class_name': 'CharField',
            'widget': {
                'attrs': {'cols': '40', 'rows': '10'},
                'input_type': 'textarea',
                'is_hidden': False,
                'is_localized': False,
                'is_required': False,
                'needs_multipart_form': False,
                'class_name': 'Textarea'
            }
        }
    },
}
