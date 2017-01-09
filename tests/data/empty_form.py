from django import forms


class EmptyForm(forms.Form):
    pass


EXPECTED_FORM = {
    'data': {},
    'errors': {},
    'fields': {},
    'fieldsets': [],
    'is_bound': False,
    'label_suffix': ':',
    'name': 'EmptyForm',
    'non_field_errors': [],
    'ordered_fields': [],
    'prefix': None,
    'title': 'EmptyForm',
    'typed_errors': {}
}

EXPECTED_FORMSET = [
    {
        'data': {},
        'errors': {},
        'fields': {},
        'fieldsets': [],
        'is_bound': False,
        'label_suffix': ':',
        'name': 'EmptyForm',
        'non_field_errors': [],
        'ordered_fields': [],
        'prefix': 'form-0',
        'title': 'EmptyForm',
        'typed_errors': {}
    }
]

EXPECTED_FORMSET_THREE = [
    {
        'data': {},
        'errors': {},
        'fields': {},
        'fieldsets': [],
        'is_bound': False,
        'label_suffix': ':',
        'name': 'EmptyForm',
        'non_field_errors': [],
        'ordered_fields': [],
        'prefix': 'form-0',
        'title': 'EmptyForm',
        'typed_errors': {}
    },
    {
        'data': {},
        'errors': {},
        'fields': {},
        'fieldsets': [],
        'is_bound': False,
        'label_suffix': ':',
        'name': 'EmptyForm',
        'non_field_errors': [],
        'ordered_fields': [],
        'prefix': 'form-1',
        'title': 'EmptyForm',
        'typed_errors': {}
    },
    {
        'data': {},
        'errors': {},
        'fields': {},
        'fieldsets': [],
        'is_bound': False,
        'label_suffix': ':',
        'name': 'EmptyForm',
        'non_field_errors': [],
        'ordered_fields': [],
        'prefix': 'form-2',
        'title': 'EmptyForm',
        'typed_errors': {}
    }
]