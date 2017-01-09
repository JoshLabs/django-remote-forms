"""
Helper functions for test data generation.
"""


def empty_form_dict(prefix=None):
    return {
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


def management_dict(total_forms=None):
    return {
        'errors': {},
        'typed_errors': {},
        'non_field_errors': [],
        'fields': {
            'INITIAL_FORMS': _management_field(required=True),
            'TOTAL_FORMS': _management_field(required=True, initial=total_forms),
            'MIN_NUM_FORMS': _management_field(required=False),
            'MAX_NUM_FORMS': _management_field(required=False, initial=1000)
        },
        'prefix': 'form',
        'title': 'ManagementForm',
        'fieldsets': [],
        'ordered_fields': ['TOTAL_FORMS', 'INITIAL_FORMS', 'MIN_NUM_FORMS', 'MAX_NUM_FORMS'],
        'name': 'ManagementForm',
        'is_bound': False,
        'data': {
            'MIN_NUM_FORMS': None,
            'INITIAL_FORMS': None,
            'TOTAL_FORMS': total_forms,
            'MAX_NUM_FORMS': 1000
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
        'widget': _man_widget_required if required else _management_widget_optional,
        'required': required,
        'help_text': '',
        'label': None
    }


_management_widget_optional = {
    'input_type': 'hidden',
    'is_required': False,
    'is_localized': False,
    'needs_multipart_form': False,
    'is_hidden': True,
    'attrs': {},
    'title': 'HiddenInput'
}
_man_widget_required = {
    'input_type': 'hidden',
    'is_required': True,
    'is_localized': False,
    'needs_multipart_form': False,
    'is_hidden': True,
    'attrs': {},
    'title': 'HiddenInput'
}
