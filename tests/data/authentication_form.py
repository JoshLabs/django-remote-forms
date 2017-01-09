import django
from distutils.version import StrictVersion
from django.contrib.auth.forms import AuthenticationForm

EXPECTED_FORM = {
    'label_suffix': ':',
    'prefix': None,
    'name': 'AuthenticationForm',
    'title': 'AuthenticationForm',
    'is_bound': False,
    'errors': {},
    'non_field_errors': [],
    'typed_errors': {},
    'data': {'username': None, 'password': None},
    'ordered_fields': ['username', 'password'],
    'fieldsets': [],
    'fields': {
        'username': {
            'required': True,
            'widget': {
                'needs_multipart_form': False,
                'is_localized': False,
                'input_type': 'text',
                'attrs': {'maxlength': '254'},
                'is_required': True,
                'title': 'TextInput',
                'is_hidden': False
            },
            'error_messages': {'required': 'This field is required.'},
            'max_length': 254,
            'help_text': '',
            'min_length': None,
            'label': 'Username',
            'title': 'CharField',
            'initial': None
        },
        'password': {
            'required': True,
            'widget': {
                'needs_multipart_form': False,
                'is_localized': False,
                'input_type': 'password',
                'attrs': {},
                'is_required': True,
                'title': 'PasswordInput',
                'is_hidden': False
            },
            'error_messages': {'required': 'This field is required.'},
            'max_length': None,
            'help_text': '',
            'min_length': None,
            'label': 'Password',
            'title': 'CharField',
            'initial': None
        }
    },
}

if StrictVersion(django.get_version()) >= StrictVersion('1.10.0'):
    EXPECTED_FORM['fields']['username']['title'] = 'UsernameField'
    EXPECTED_FORM['fields']['username']['widget']['attrs']['autofocus'] = ''
