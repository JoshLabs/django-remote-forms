# -*- coding: utf-8 -*-
import os
import mock
from unittest import TestCase
from django.core.serializers.json import json, DjangoJSONEncoder

from django.conf import settings
from django.contrib.admin.forms import AuthenticationForm

from django_remote_forms.forms import RemoteForm

expect = {u'data': {u'password': None, u'username': None},
          u'errors': {},
          u'fields': {u'password': {u'error_messages': {u'required': u'This field is required.'},
                                    u'help_text': u'',
                                    u'initial': None,
                                    u'label': u'Password',
                                    u'max_length': None,
                                    u'min_length': None,
                                    u'required': True,
                                    u'title': u'CharField',
                                    u'widget': {u'attrs': {},
                                                u'input_type': u'password',
                                                u'is_hidden': False,
                                                u'is_localized': False,
                                                u'is_required': True,
                                                u'needs_multipart_form': False,
                                                u'title': u'PasswordInput'}},
                      u'username': {u'initial': None}},
          u'fieldsets': [],
          u'is_bound': False,
          u'label_suffix': u':',
          u'name': u'AuthenticationForm',
          u'non_field_errors': [],
          u'ordered_fields': [u'username', u'password'],
          u'prefix': None,
          u'title': u'AuthenticationForm',
          u'typed_errors': {}}


class GenericTestCase(TestCase):
    maxDiff = None

    def test_empty(self):
        form = AuthenticationForm()
        remote_form = RemoteForm(form)
        remote_form_dict = remote_form.as_dict()
        # remote_form_json = json.dumps(remote_form_dict, cls=DjangoJSONEncoder)
        self.assertEqual(remote_form_dict, expect)
