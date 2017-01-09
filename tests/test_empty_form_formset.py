from django import forms
from django.forms import formset_factory, BaseFormSet
from django_remote_forms.forms import RemoteFormSet
from tests.data.empty_form import EmptyForm
from .data.utils import empty_form_dict, management_dict


def test_single_form():
    EmptyFormSet = formset_factory(EmptyForm)
    formset = EmptyFormSet()
    remote_formset = RemoteFormSet(formset)
    as_dict = remote_formset.as_dict()
    assert as_dict == {
        'management_form': management_dict(total_forms=1),
        'forms': [empty_form_dict(prefix='form-0')]
    }


def test_zero_forms():
    EmptyFormSet = formset_factory(EmptyForm, extra=0)
    formset = EmptyFormSet()
    remote_formset = RemoteFormSet(formset)
    as_dict = remote_formset.as_dict()
    assert as_dict == {
        'management_form': management_dict(),
        'forms': []
    }


def test_three_forms():
    EmptyFormSet = formset_factory(EmptyForm, extra=3)
    formset = EmptyFormSet()
    remote_formset = RemoteFormSet(formset)
    as_dict = remote_formset.as_dict()
    assert as_dict == {
        'management_form': management_dict(total_forms=3),
        'forms': [
            empty_form_dict(prefix='form-0'),
            empty_form_dict(prefix='form-1'),
            empty_form_dict(prefix='form-2'),
        ]
    }


def test_five_max():
    EmptyFormSet = formset_factory(EmptyForm, extra=2, max_num=3)
    formset = EmptyFormSet()
    remote_formset = RemoteFormSet(formset)
    as_dict = remote_formset.as_dict()
    assert as_dict == {
        'management_form': management_dict(total_forms=2, max_num=3),
        'forms': [
            empty_form_dict(prefix='form-0'),
            empty_form_dict(prefix='form-1'),
        ]
    }


def test_one_min():
    EmptyFormSet = formset_factory(EmptyForm, extra=2, min_num=1)
    formset = EmptyFormSet()
    remote_formset = RemoteFormSet(formset)
    as_dict = remote_formset.as_dict()
    assert as_dict == {
        'management_form': management_dict(total_forms=3, min_num=1),
        'forms': [
            empty_form_dict(prefix='form-0'),
            empty_form_dict(prefix='form-1'),
            empty_form_dict(prefix='form-2'),
        ]
    }


def test_additional_fields():
    class BaseEmptyFormSet(BaseFormSet):
        def add_fields(self, form, index):
            super(BaseEmptyFormSet, self).add_fields(form, index)
            form.fields['my_field'] = forms.CharField()

    EmptyFormSet = formset_factory(EmptyForm, formset=BaseEmptyFormSet)
    formset = EmptyFormSet()
    remote_formset = RemoteFormSet(formset)
    as_dict = remote_formset.as_dict()
    assert as_dict == {
        'management_form': management_dict(total_forms=1),
        'forms': [empty_form_dict(prefix='form-0', add_my_field=True)]
    }


def test_formset_prefix_change():
    EmptyFormSet = formset_factory(EmptyForm, min_num=3)
    formset = EmptyFormSet(prefix='emptiness')
    remote_formset = RemoteFormSet(formset)
    as_dict = remote_formset.as_dict()
    assert as_dict == {
        'management_form': management_dict(prefix='emptiness', total_forms=4, min_num=3),
        'forms': [
            empty_form_dict(prefix='emptiness-0'),
            empty_form_dict(prefix='emptiness-1'),
            empty_form_dict(prefix='emptiness-2'),
            empty_form_dict(prefix='emptiness-3'),
        ]
    }
