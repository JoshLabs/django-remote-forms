from django import forms


class EmptyForm(forms.Form):
    pass


EXPECT = {
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
