# -*- coding: utf-8 -*-
from unittest import TestCase

from django import forms

from django_remote_forms.forms import RemoteForm


class TestForm(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, required=False)

    check = forms.BooleanField()
    select = forms.ChoiceField(choices=[('label', '1'), ('label2', '2')], initial='2')


EXPECT = {'data': {'check': None, 'name': None, 'select': '2', 'text': None},
          'errors': {},
          'fields': {'check': {'error_messages': {u'required': u'This field is required.'},
                               'help_text': u'',
                               'initial': None,
                               'label': None,
                               'required': True,
                               'title': 'BooleanField',
                               'widget': {'attrs': {},
                                          'check_test': True,
                                          'input_type': 'checkbox',
                                          'is_hidden': False,
                                          'is_localized': False,
                                          'is_required': True,
                                          'needs_multipart_form': False,
                                          'title': 'CheckboxInput'}},
                     'name': {'error_messages': {u'required': u'This field is required.'},
                              'help_text': u'',
                              'initial': None,
                              'label': None,
                              'max_length': None,
                              'min_length': None,
                              'required': True,
                              'title': 'CharField',
                              'widget': {'attrs': {},
                                         'input_type': u'text',
                                         'is_hidden': False,
                                         'is_localized': False,
                                         'is_required': True,
                                         'needs_multipart_form': False,
                                         'title': 'TextInput'}},
                     'select': {'choices': [{'display': '1', 'value': 'label'},
                                            {'display': '2', 'value': 'label2'}],
                                'error_messages': {
                                    u'invalid_choice': u'Select a valid choice. %(value)s is not one of the available choices.',
                                    u'required': u'This field is required.'},
                                'help_text': u'',
                                'initial': '2',
                                'label': None,
                                'required': True,
                                'title': 'ChoiceField',
                                'widget': {'attrs': {},
                                           'choices': [{'display': '1',
                                                        'value': 'label'},
                                                       {'display': '2',
                                                        'value': 'label2'}],
                                           'input_type': 'select',
                                           'is_hidden': False,
                                           'is_localized': False,
                                           'is_required': True,
                                           'needs_multipart_form': False,
                                           'title': 'Select'}},
                     'text': {'error_messages': {u'required': u'This field is required.'},
                              'help_text': u'',
                              'initial': None,
                              'label': None,
                              'max_length': None,
                              'min_length': None,
                              'required': False,
                              'title': 'CharField',
                              'widget': {'attrs': {u'cols': u'40', u'rows': u'10'},
                                         'input_type': 'textarea',
                                         'is_hidden': False,
                                         'is_localized': False,
                                         'is_required': False,
                                         'needs_multipart_form': False,
                                         'title': 'Textarea'}}},
          'fieldsets': [],
          'is_bound': False,
          'label_suffix': u':',
          'name': 'TestForm',
          'non_field_errors': [],
          'ordered_fields': ['name', 'text', 'check', 'select'],
          'prefix': None,
          'title': 'TestForm',
          'typed_errors': {}}


class GenericTestCase(TestCase):
    maxDiff = None

    def test_empty(self):
        form = TestForm()
        remote_form = RemoteForm(form)
        remote_form_dict = remote_form.as_dict()

        self.assertEqual(remote_form_dict, EXPECT)
