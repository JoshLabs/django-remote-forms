"""
Helper functions for test data generation.
"""


def empty_form_dict(prefix=None, add_my_field=False):
    dict = {
        'data': {},
        'errors': {},
        'fields': {},
        'fieldsets': [],
        'is_bound': False,
        'label_suffix': ':',
        'name': 'EmptyForm',
        'non_field_errors': [],
        'ordered_fields': [],
        'prefix': prefix,
        'title': 'EmptyForm',
        'typed_errors': {}
    }
    if add_my_field:
        dict['data']['my_field'] = None
        dict['ordered_fields'] = ['my_field']
        dict['fields']['my_field'] = {
            'min_length': None,
            'title': 'CharField',
            'required': True,
            'error_messages': {'required': 'This field is required.'},
            'help_text': '',
            'initial': None,
            'max_length': None,
            'label': None,
            'widget': {
                'title': 'TextInput',
                'is_localized': False,
                'is_hidden': False,
                'attrs': {},
                'is_required': True,
                'input_type': 'text',
                'needs_multipart_form': False
            }
        }
    return dict


def management_dict(prefix='form', initial_forms=None, total_forms=None, min_num=None, max_num=1000):
    return {
        'errors': {},
        'typed_errors': {},
        'non_field_errors': [],
        'fields': {
            'INITIAL_FORMS': _management_field(required=True, initial=initial_forms),
            'TOTAL_FORMS': _management_field(required=True, initial=total_forms),
            'MIN_NUM_FORMS': _management_field(required=False, initial=min_num),
            'MAX_NUM_FORMS': _management_field(required=False, initial=max_num)
        },
        'prefix': prefix,
        'title': 'ManagementForm',
        'fieldsets': [],
        'ordered_fields': ['TOTAL_FORMS', 'INITIAL_FORMS', 'MIN_NUM_FORMS', 'MAX_NUM_FORMS'],
        'name': 'ManagementForm',
        'is_bound': False,
        'data': {
            'INITIAL_FORMS': initial_forms,
            'MIN_NUM_FORMS': min_num,
            'TOTAL_FORMS': total_forms,
            'MAX_NUM_FORMS': max_num
        },
        'label_suffix': ':'
    }


def _management_field(required, initial=None):
    return {
        'initial': initial,
        'title': 'IntegerField',
        'min_value': None,
        'error_messages': {'invalid': 'Enter a whole number.', 'required': 'This field is required.'},
        'max_value': None,
        'widget': _management_widget(required=required),
        'required': required,
        'help_text': '',
        'label': None
    }


def _management_widget(required=True):
    return {
        'input_type': 'hidden',
        'is_required': required,
        'is_localized': False,
        'needs_multipart_form': False,
        'is_hidden': True,
        'attrs': {},
        'title': 'HiddenInput'
    }
